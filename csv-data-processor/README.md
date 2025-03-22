# CSV Data Processor

This Python script processes a given CSV file and generates a new file containing a set of unique, formatted strings based on specific conditions.

# Features

Reads input CSV file.
Extracts and processes data by removing the first four characters of each entry in the first column.
Validates the prefix of each entry, ensuring it belongs to a predefined set of valid prefixes.
Creates unique identifiers based on valid prefixes and appends them to a list.
Saves the generated identifiers in a new output file, which is timestamped for uniqueness.

## Usage

1. Ensure that the script and the input CSV file are in the same directory, or provide the full path to the CSV file.

2. Run the script via command line:

```bash
    python3 process_csv.py <input_file.csv>
```

3. The script will process the input CSV file, generate a new file with formatted identifiers, and save it in a directory named processed_data.

```bash
    python3 process_csv.py input_data.csv
```

The script will generate a file named processed_output_YYYYMMDD_HHMMSS.txt (where the timestamp represents the exact time the file is generated) inside the processed_data folder.

## Example of Missing Argument Error

```
    ❌ Error: Please provide the input CSV file path command-line arguments.
    👉 Usage: python3 process_csv.py <input_file.csv>
```
