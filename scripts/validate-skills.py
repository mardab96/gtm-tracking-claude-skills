#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDERS = ["Add the inputs", "Step one", "Step two", "Step three", "Column 1", "Column 2", "Column 3"]
TEMPLATED_PHRASES = [
    "diagnosing, planning, reviewing",
    "asks for help with",
    "provides data, screenshots",
    "needs an approval-ready diagnosis",
    "Can you check this",
]
REQUIRED_SECTIONS = [
    "## Use this skill when",
    "## Required input",
    "## Analysis workflow",
    "## Decision rules",
    "## Output format",
    "## Practical example",
    "## Guardrails",
]


def section(text, heading):
    match = re.search(rf"## {re.escape(heading)}\n\n(.*?)(?=\n## |\Z)", text, re.S)
    return match.group(1).strip() if match else ""


def main():
    errors = []
    for path in sorted(ROOT.glob("*/SKILL.md")):
        text = path.read_text()
        rel = path.relative_to(ROOT)
        for token in PLACEHOLDERS:
            if token in text:
                errors.append(f"{rel}: placeholder token: {token}")
        for phrase in TEMPLATED_PHRASES:
            if phrase in text:
                errors.append(f"{rel}: templated phrase: {phrase}")
        for heading in REQUIRED_SECTIONS:
            if heading not in text:
                errors.append(f"{rel}: missing section: {heading}")
        frontmatter = text.split("---", 2)[1] if text.startswith("---") and text.count("---") >= 2 else ""
        description = next((line for line in frontmatter.splitlines() if line.startswith("description:")), "")
        if "Use when" not in description:
            errors.append(f"{rel}: description should include an activation phrase with 'Use when'")
        workflow_steps = re.findall(r"^\d+\.\s+", section(text, "Analysis workflow"), re.M)
        if len(workflow_steps) < 5:
            errors.append(f"{rel}: analysis workflow should have at least 5 steps")
        if len(text.split()) < 280:
            errors.append(f"{rel}: SKILL.md is too short to be useful")

    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print("OK: all skills passed validation")


if __name__ == "__main__":
    main()
