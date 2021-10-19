from functions import *
import sys
import argparse


# Asks user how many e-mails the program should generate and what output.
def main():
    intro()

    # Add arguments for number of e-mails and output format
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", help="Number of emails")
    parser.add_argument("-o", "--output", help="Output format")

    # Initialise
    args = parser.parse_args()

    # Assign values to variables
    max_email = int(args.number)
    layout = args.output

    # Execute functions to generate e-mails
    names, surnames = read_json()
    generated = generate(names, surnames, max_email)

    # Check the value of layout for output format
    if layout == "txt" or layout == "text":
        write_txt(generated, max_email)
    elif layout == "csv" or layout == "CSV":
        write_csv(generated, max_email)
    else:
        output(generated, max_email)


if __name__ == "__main__":
    main()
