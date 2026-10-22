import os
import re
import unittest

from _load import ROOT, PROJECT_ROOT

SKILLS = [
    "replica-recon", "replica-architect", "replica-design", "replica-build",
    "replica-backend", "replica-test", "replica-diff", "replica-entrepreneur",
    "replica-brand", "replica-launch", "replica-deploy"
]


def frontmatter(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return (m.group(1) if m else ""), text


class Repo(unittest.TestCase):
    def test_eleven_skill_folders_installed(self):
        for s in SKILLS:
            skill_md = os.path.join(ROOT, s, "SKILL.md")
            self.assertTrue(os.path.isfile(skill_md), f"Skill ausente: {skill_md}")

    def test_frontmatter_name_and_description(self):
        for s in SKILLS:
            fm, text = frontmatter(os.path.join(ROOT, s, "SKILL.md"))
            self.assertIn("name: %s\n" % s, fm + "\n", s)
            self.assertRegex(fm, r"description: ", s)
            self.assertGreater(len(fm), 200, "%s description is too thin" % s)
            self.assertGreater(len(text.splitlines()), 60, s)

    def test_skills_mirrored_in_agents(self):
        agents_skills = os.path.join(PROJECT_ROOT, ".agents", "skills")
        for s in SKILLS:
            skill_md = os.path.join(agents_skills, s, "SKILL.md")
            self.assertTrue(os.path.isfile(skill_md), f"Skill não espelhada em .agents: {skill_md}")

    def test_no_em_dashes_in_replica_skills(self):
        bad = []
        for s in SKILLS:
            skill_dir = os.path.join(ROOT, s)
            for dirpath, dirnames, filenames in os.walk(skill_dir):
                dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__")]
                for fn in filenames:
                    if fn.endswith((".md", ".py", ".json", ".ts", ".csv")):
                        path = os.path.join(dirpath, fn)
                        with open(path, encoding="utf-8") as fh:
                            if chr(0x2014) in fh.read():
                                bad.append(os.path.relpath(path, ROOT))
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main()
