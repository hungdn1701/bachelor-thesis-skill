"""Consistency checks for the repository itself."""

import json
import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
NAMES = ("bachelor-thesis-writing", "bachelor-thesis-review")


def read(*parts):
    with open(os.path.join(ROOT, *parts), encoding="utf-8") as handle:
        return handle.read()


def frontmatter(text):
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    fields = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields


class Skills(unittest.TestCase):
    def test_frontmatter_follows_the_convention(self):
        for name in NAMES:
            fields = frontmatter(read("skills", name, "SKILL.md"))
            self.assertEqual(fields["name"], name)
            self.assertTrue(fields["description"].startswith("Use when"), name)
            self.assertLessEqual(len(fields["name"]) + len(fields["description"]), 1024)

    def test_referenced_files_exist(self):
        for name in NAMES:
            base = os.path.join(SKILLS, name)
            for ref in re.findall(r"`((?:references|assets|scripts|profiles)/[\w./-]+)`", read("skills", name, "SKILL.md")):
                self.assertTrue(os.path.exists(os.path.join(base, ref)), f"{name}: {ref}")

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
