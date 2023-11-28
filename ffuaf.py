#!/usr/bin/python3

import argparse

def remove_lines(input_file, filter_file, output_file):
    # Read the content of the file with lines to be removed
    with open(filter_file, 'r') as filter_file:
        filter_lines = set(filter_file.read().splitlines())

    # Search the input file and write the result to the output file
    with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
        for line in input_file:
            if line.strip() not in filter_lines:
                output_file.write(line)

if __name__ == "__main__":
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="Remove lines from a file based on the content of another file.")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("filter_file", help="Path to the file containing lines to be removed")
    parser.add_argument("output_file", help="Path to the output file")

    # Parse the arguments
    args = parser.parse_args()

    # Call the function to remove lines
    remove_lines(args.input_file, args.filter_file, args.output_file)

    print("Operation completed successfully.")