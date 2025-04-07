# 📊 Line of Code Counter for Django Projects

This project provides two scripts to count the number of lines of code (LOC) in a Django project:

- 🐚 Bash version: count_loc.sh
- 🐍 Python version: count_loc.py

Both scripts scan your project directory, count lines in source files (e.g. .py, .html, .css, .js), and exclude common non-source directories like venv, migrations, static, etc.

---

## 🐚 count_loc.sh (Bash Version)

count_loc.sh is a Bash script that uses Unix tools (find, grep, wc) to recursively count lines of code in specific file types within a Django project.

### ⚙️ Configuration

- File extensions scanned: py, html, css, js
- Excluded directories: venv, env, migrations, **pycache**, static, media, .git, node_modules

You can customize these inside the script by editing the EXTENSIONS and EXCLUDE_DIRS variables.

### 🚀 Usage

1. Make it executable:

   ```bash
   chmod +x count_loc.sh
   ```

2. Run it from the root of your Django project:

```bash
./count_loc.sh
```

## ⚙️ Configuration

You can customize the following variables in the script:
EXTENSIONS: Space-separated list of file extensions to include
EXCLUDE_DIRS: Pipe-separated regex pattern of directories to skip

```bash
EXTENSIONS="py js ts"
EXCLUDE_DIRS="venv|env|migrations|.git|node_modules"
```

## 🐍 count_loc.py (Python Version)

count_loc.py is a cross-platform Python 3 script that replicates the functionality of the Bash script using pathlib, regex, and manual line counting.

## 📝 Notes

- Line counts are based on wc -l (in Bash) or reading the file lines (in Python).
- This includes blank lines and comment lines.
  this will be improved in a future version to exclude non-code lines.
