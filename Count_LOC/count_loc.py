#!/usr/bin/env python3
import re
from pathlib import Path
from collections import defaultdict

RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
NC = "\033[0m"

PROJECT_DIR = Path.cwd()
EXTENSIONS = ["py", "html", "css", "js"]
EXCLUDE_DIRS_PATTERN = re.compile(
    r"(venv|env|migrations|__pycache__|static|media|\.git|node_modules)"
)

extension_counts = defaultdict(int)
file_counts = defaultdict(int)
total_loc = 0
total_files = 0

print(f"{GREEN}Counting lines of code in Django project at {YELLOW}{PROJECT_DIR}{NC}")
print(f"{RED}Excluding: {BLUE}{EXCLUDE_DIRS_PATTERN.pattern}{NC}")
print(f"{GREEN}{'-' * 44}{NC}")


def is_excluded(path: Path) -> bool:
    return any(EXCLUDE_DIRS_PATTERN.search(part) for part in path.parts)


for ext in EXTENSIONS:
    print(f"\n{YELLOW}{ext} files:{NC}")
    for file_path in PROJECT_DIR.rglob(f"*.{ext}"):
        if is_excluded(file_path):
            continue
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                count = sum(1 for _ in f)
            extension_counts[ext] += count
            file_counts[ext] += 1
            total_loc += count
            total_files += 1
            relative_path = file_path.relative_to(PROJECT_DIR)
            print(f"  {BLUE}{count:<6}{NC} {relative_path}")
        except Exception as e:
            print(f"{RED}Error reading {file_path}: {e}{NC}")

    print(
        f"  {GREEN}Total for .{ext}: {YELLOW}{extension_counts[ext]}{NC} lines in {YELLOW}{file_counts[ext]}{NC} files"
    )

print(f"\n{GREEN}{'-' * 44}")
print(f"Summary:{NC}")
print(f"{YELLOW}{'Extension':<10} {'Lines':>12} {'Files':>12}{NC}")
print(f"{GREEN}{'-' * 44}{NC}")
for ext in EXTENSIONS:
    print(f".{ext:<9} {extension_counts[ext]:>12} {file_counts[ext]:>12}")
print(f"{GREEN}{'-' * 44}{NC}")
print(f"{YELLOW}{'Total':<10} {total_loc:>12} {total_files:>12}{NC}")
print(f"{GREEN}{'-' * 44}{NC}")
