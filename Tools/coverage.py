import os
import re

def sort_coverage_files(project_root):
    coverage_dir = os.path.join(project_root, "coverage")
    priorities_dir = os.path.join(project_root, "priorities")

    # Create the priorities directory if it doesn't exist
    if not os.path.exists(priorities_dir):
        os.makedirs(priorities_dir)
        print(f"Created priorities directory: {priorities_dir}")

    # Regex pattern to extract project name and ID from filename
    pattern = re.compile(r"^(.*)_lines\.txt$")

    matched_files = 0
    unmatched_files = []
    already_sorted_files = 0

    # Iterate over all coverage files
    for filename in os.listdir(coverage_dir):
        match = pattern.match(filename)
        if match:
            base_name = match.group(1)
            input_path = os.path.join(coverage_dir, filename)
            output_filename = f"{base_name}_priorities.txt"
            output_path = os.path.join(priorities_dir, output_filename)

            if os.path.exists(output_path):
                print(f"Skipping already sorted file: {output_path}")
                already_sorted_files += 1
                continue

            print(f"Processing file: {input_path}")

            # Read coverage lines from the file
            with open(input_path, 'r') as file:
                lines = file.readlines()

            # Sort indices by the number of covered lines (most to least)
            sorted_indices = sorted(range(len(lines)), key=lambda x: len(lines[x].strip().split()), reverse=True)

            # Write the sorted indices to the output file, starting from 1
            with open(output_path, 'w') as file:
                for idx in sorted_indices:
                    file.write(f"{idx + 1}\n")

            print(f"Finished processing {input_path}, results saved to {output_path}")
            matched_files += 1
        else:
            unmatched_files.append(filename)

    print(f"All files have been processed. Matched files: {matched_files}, Already sorted files: {already_sorted_files}, Unmatched files: {len(unmatched_files)}")
    if unmatched_files:
        print("Unmatched files:")
        for filename in unmatched_files:
            print(f"  {filename}")

if __name__ == "__main__":
    project_root = os.getcwd()  # Assuming the script is run from the project root
    sort_coverage_files(project_root)
