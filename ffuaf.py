#!/usr/bin/python3

import argparse

def process_filter_line(line):
    # Trim the line if the pattern is present
    if " copied to " in line:
        line = line.split(" copied to ")[0].strip()
    # elif "Engine version" in line:
    #     line = ""   
    # elif "SCAN SUMMARY" in line: 
    #     line = ""
    return line

def is_line_valid(line):
    invalid_phrases = ["Engine version", "SCAN SUMMARY"]
    return all(phrase not in line for phrase in invalid_phrases)

def remove_lines(input_file, filter_file, output_file):
    # Read the content of the file with lines to be removed
    with open(filter_file, 'r') as filter_file:
        filter_lines = set(process_filter_line(line) for line in filter_file if line.strip() if is_line_valid(line))
        # filter_lines = [line for line in filter_lines if "Engine version" not in line]
        # filter_lines = [line for line in filter_lines if "SCAN SUMMARY" not in line]

    # Initialize counter for removed lines
    removed_lines_count = 0
    
    # Search the input file and write the result to the output file
    with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
        for line in input_file:
            # debug(line,filter_lines)
            if any(filter_line in line for filter_line in filter_lines):
                removed_lines_count += 1
            else:
                output_file.write(line)
    return removed_lines_count

# def debug(line, filter_lines):
#     for filter_line in filter_lines:
#         if filter_line in line:
#             print(filter_line, line)
#             return

if __name__ == "__main__":
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="Remove lines from a file based on lines in another file.")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("filter_file", help="Path to the file containing lines to be removed")
    parser.add_argument("output_file", help="Path to the output file")

    # Parse the arguments
    args = parser.parse_args()

    # Call the function to remove lines
    removed_lines_count = remove_lines(args.input_file, args.filter_file, args.output_file)

    print(f"Operation completed successfully. Removed {removed_lines_count} lines.")