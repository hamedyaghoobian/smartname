#!/usr/bin/env python3
"""Test script to demonstrate different casing styles."""

import sys
from pathlib import Path

# Add parent directory to path to import from rename_files
sys.path.insert(0, str(Path(__file__).parent))

from rename_files import apply_casing

# Sample filename from AI
sample_name = "The Logic of Sense by Gilles Deleuze"

print("Testing Casing Styles")
print("=" * 60)
print(f"Original: {sample_name}")
print("=" * 60)

styles = {
    "snake": "snake_case (default)",
    "kebab": "kebab-case",
    "camel": "camelCase",
    "pascal": "PascalCase",
    "lower": "lowercase with spaces",
    "title": "Title Case With Spaces"
}

for style, description in styles.items():
    result = apply_casing(sample_name, style)
    print(f"{style:8} ({description:25}): {result}")

print("\n" + "=" * 60)
print("Another example: 'Python Week 04 Args Kwargs Class'")
print("=" * 60)

sample_name2 = "Python Week 04 Args Kwargs Class"
for style in styles.keys():
    result = apply_casing(sample_name2, style)
    print(f"{style:8}: {result}")
