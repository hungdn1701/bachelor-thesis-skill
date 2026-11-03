"""Consistency checks for the repository itself."""

import json
import os
import re
import unittest

try:
    import yaml
except ImportError:
    yaml = None

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
NAMES = ("bachelor-thesis-planning", "bachelor-thesis-writing", "bachelor-thesis-review")
COMMANDS = ("idea", "plan", "write", "review", "defense", "final")


def read(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as handle:
        return handle.read()


def yaml_free_metadata(text):
    block = re.search(r"^metadata:\n((?:  .+\n)+)", text, re.M).group(1)
    pairs = (line.strip().partition(":") for line in block.splitlines())
    return {key: value.strip().strip('"') for key, _, value in pairs}


def split_skill(text):
    match = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    return match.group(1), match.group(2)


def frontmatter(text):
    """Top-level fields only, which is all the checks below need."""
    fields = {}
    for line in split_skill(text)[0].splitlines():
        if line[:1].isspace():
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields


class Skills(unittest.TestCase):
    """Rules from the Agent Skills specification, https://agentskills.io/specification"""

    def test_name_follows_the_specification(self):
        for name in NAMES:
            fields = frontmatter(read("skills", name, "SKILL.md"))
            self.assertEqual(fields["name"], name, "must match the folder")
            self.assertLessEqual(len(name), 64)
            self.assertRegex(name, r"^[a-z0-9]+(-[a-z0-9]+)*$")

    def test_description_and_optional_fields_fit_their_limits(self):
        for name in NAMES:
            fields = frontmatter(read("skills", name, "SKILL.md"))
            self.assertTrue(fields["description"].startswith("Use when"), name)
            self.assertLessEqual(len(fields["description"]), 1024)
            self.assertLessEqual(len(fields["compatibility"]), 500)
            self.assertIn("CC-BY-4.0", fields["license"])

    def test_only_fields_of_the_specification_are_used(self):
        allowed = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
        for name in NAMES:
            self.assertLessEqual(set(frontmatter(read("skills", name, "SKILL.md"))), allowed, name)

    def test_frontmatter_has_no_yaml_traps(self):
        """Agents parse this as YAML; an unquoted ': ' or ' #' breaks or truncates a field."""
        for name in NAMES:
            for key, value in frontmatter(read("skills", name, "SKILL.md")).items():
                self.assertNotIn(": ", value, f"{name}: {key}")
                self.assertNotIn(" #", value, f"{name}: {key}")

    @unittest.skipIf(yaml is None, "PyYAML is not installed")
    def test_frontmatter_parses_as_yaml(self):
        for name in NAMES:
            data = yaml.safe_load(split_skill(read("skills", name, "SKILL.md"))[0])
            self.assertEqual(data["name"], name)
            for key, value in data["metadata"].items():
                self.assertIsInstance(value, str, f"{name}: metadata.{key} must be a string")

    def test_body_stays_within_the_recommended_size(self):
        for name in NAMES:
            body = split_skill(read("skills", name, "SKILL.md"))[1]
            self.assertLess(len(body.splitlines()), 500, name)
            self.assertLess(len(body.split()), 1250, f"{name}: roughly 5000 tokens")

    def test_each_skill_folder_works_alone(self):
        """An install copies only the skill's folder, so a path must resolve inside it."""
        pattern = r"`((?:references|assets|scripts|profiles|data)/[\w./-]+)`"
        for name in NAMES:
            base = os.path.join(SKILLS, name)
            texts = [("SKILL.md", read("skills", name, "SKILL.md"))]
            for folder in ("references", "profiles"):
                if not os.path.isdir(os.path.join(base, folder)):
                    continue
                for item in os.listdir(os.path.join(base, folder)):
                    if item.endswith(".md"):
                        texts.append((item, read("skills", name, folder, item)))
            for source, text in texts:
                for line in text.splitlines():
                    for ref in re.findall(pattern, line):
                        if "bachelor-thesis-" in line:
                            continue  # names the other skill's own path, with a fallback here
                        self.assertTrue(os.path.exists(os.path.join(base, ref)), f"{name}/{source}: {ref}")

    def test_no_skill_file_is_dropped_by_the_installer(self):
        """The skills CLI skips these names when it copies a skill."""
        for name in NAMES:
            for _, _, files in os.walk(os.path.join(SKILLS, name)):
                self.assertNotIn("metadata.json", files)

    def test_no_stray_skill_outside_the_skills_folder(self):
        for base, dirs, files in os.walk(ROOT):
            dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", "skills")]
            self.assertNotIn("SKILL.md", files, base)


class Commands(unittest.TestCase):
    def test_every_step_has_a_command_that_names_its_skill(self):
        for name in COMMANDS:
            text = read("commands", f"{name}.md")
            self.assertIn("disable-model-invocation: true", text, name)
            self.assertTrue(any(skill in text for skill in NAMES), name)

    def test_files_a_command_points_to_exist_in_its_skill(self):
        for name in COMMANDS:
            text = read("commands", f"{name}.md")
            skill = next(skill for skill in NAMES if skill in text)
            for ref in re.findall(r"`(references/[\w.-]+)`", text):
                self.assertTrue(os.path.exists(os.path.join(SKILLS, skill, ref)), f"{name}: {ref}")

    def test_readmes_name_every_command(self):
        for readme in ("README.md", "README.vi.md"):
            text = read(readme)
            for name in COMMANDS:
                self.assertIn(f"/{name}", text, f"{readme}: {name}")


class Marketplace(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(read(".claude-plugin", "marketplace.json"))
        self.plugin = self.data["plugins"][0]

    def test_lists_every_skill(self):
        self.assertEqual(self.plugin["skills"], [f"./skills/{name}" for name in NAMES])

    def test_versions_agree(self):
        for name in NAMES:
            metadata = yaml_free_metadata(read("skills", name, "SKILL.md"))
            self.assertEqual(metadata["version"], self.plugin["version"], name)

    def test_install_lines_in_readmes_match(self):
        repo = f"hungdn1701/{self.data['name']}"
        for readme in ("README.md", "README.vi.md"):
            text = read(readme)
            self.assertIn(f"claude plugin install {self.plugin['name']} --marketplace {repo}", text, readme)
            self.assertIn(f"npx skills add {repo}", text, readme)

    def test_all_five_gates_have_a_reference(self):
        found = os.listdir(os.path.join(SKILLS, "bachelor-thesis-review", "references"))
        for gate in ("gate-1-honesty.md", "gate-2-logic.md", "gate-3-structure.md", "gate-4-format.md", "gate-5-style.md"):
            self.assertIn(gate, found)


class Profiles(unittest.TestCase):
    def test_profile_folders_are_identical(self):
        writing = os.path.join(SKILLS, "bachelor-thesis-writing", "profiles")
        review = os.path.join(SKILLS, "bachelor-thesis-review", "profiles")
        self.assertEqual(sorted(os.listdir(writing)), sorted(os.listdir(review)))
        for name in os.listdir(writing):
            with open(os.path.join(writing, name), "rb") as first, open(os.path.join(review, name), "rb") as second:
                self.assertEqual(first.read(), second.read(), name)

    def test_structure_files_are_identical(self):
        for name in ("structure-build.md", "structure-research.md"):
            self.assertEqual(
                read("skills", "bachelor-thesis-writing", "references", name),
                read("skills", "bachelor-thesis-planning", "references", name),
            )

    def test_config_templates_are_identical(self):
        self.assertEqual(
            read("skills", "bachelor-thesis-writing", "assets", "config.json"),
            read("skills", "bachelor-thesis-review", "assets", "config.json"),
        )

    def test_each_profile_has_both_files_and_a_matching_id(self):
        folder = os.path.join(SKILLS, "bachelor-thesis-writing", "profiles")
        for name in os.listdir(folder):
            stem, ext = os.path.splitext(name)
            if ext == ".json":
                self.assertTrue(os.path.exists(os.path.join(folder, stem + ".md")), stem)
                with open(os.path.join(folder, name), encoding="utf-8") as handle:
                    self.assertEqual(json.load(handle)["id"], stem)


class Files(unittest.TestCase):
    def test_text_files_have_no_bom(self):
        for base, dirs, files in os.walk(ROOT):
            dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
            for name in files:
                if name.endswith((".md", ".py", ".json", ".yml", ".csv")):
                    with open(os.path.join(base, name), "rb") as handle:
                        self.assertFalse(handle.read(3) == b"\xef\xbb\xbf", name)

    def test_style_terms_have_every_group_for_each_language(self):
        terms = json.loads(read("skills", "bachelor-thesis-review", "data", "style-terms.json"))
        for language in ("vi", "en"):
            self.assertEqual(sorted(terms[language]), ["absolute", "chat", "hype", "slop", "tool"])

    def test_scenarios_name_existing_skills(self):
        data = json.loads(read("evals", "scenarios.json"))
        self.assertGreaterEqual(len(data["scenarios"]), 5)
        for scenario in data["scenarios"]:
            self.assertIn(scenario["skill"], NAMES)
            self.assertTrue(scenario["must"] and scenario["must_not"])


if __name__ == "__main__":
    unittest.main()
