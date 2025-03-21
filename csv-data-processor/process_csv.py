import csv
import datetime
import sys
import os


def process_csv(input_file):
    os.makedirs("processed_data", exist_ok=True)

    valid_prefixes = {"110", "120", "130", "140", "150"}
    inject_list = []

    with open(input_file, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader)

        out = [row[0][4:] for row in reader]
        out_set = set(out)

        for counter, value in enumerate(out, start=1):
            prefix = value[:3]
            if prefix in valid_prefixes:
                inject = f"{prefix}{counter:03}"
                if inject not in out_set:
                    inject_list.append(f"L200{inject}")

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join("processed_data", f"processed_output_{timestamp}.txt")

    with open(output_file, "w") as f:
        f.write("\n".join(inject_list))

    print(f"✅ Output saved to {output_file}")
    return output_file


if len(sys.argv) < 2:
    print("❌ Error: Please provide the input CSV file path command-line arguments.")
    print("👉 Usage: python3 process_csv.py <input_file.csv>")
    sys.exit(1)

input_file_path = sys.argv[1]

process_csv(input_file_path)
