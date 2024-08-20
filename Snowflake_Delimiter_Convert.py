import csv

def convert_to_csv(input_file_path, output_file_path):
    """Converts a space-delimited text file to a CSV with custom delimiter and quotechar."""
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w', newline='') as outfile:
        for line in infile:
            # Split the line by space, strip whitespace, and surround each element with single quotes
            elements = ["'{}'".format(element.strip()) for element in line.split()]
            # Write each element in the desired format with a trailing comma
            outfile.write(','.join(elements) + ',\n')
if __name__ == "__main__":
    print("--Please make sure you cd into the folder your text Input and Output files are if needed. Also please make sure to exit the files before conversion--")
    input_file = input("Enter the path to your space-delimited text file: ")
    output_file = input("Enter the desired path for the output CSV file: ")
    convert_to_csv(input_file, output_file)
    print("Conversion complete!")