import sys
import csv
from statistics import mean

def main():
    assert len(sys.argv) > 1, "No input file path specified."

    input_file_path = sys.argv[1]
    print(f"Processing input file: {input_file_path}")

   # TODO: Fill in the actual logic here!
    with open(input_file_path) as file:
        reader =csv.reader(file, delimiter = ',')

        for line in reader:
            new_list = []
            for item in line:
                new_list.append(float(item))
            print(mean(new_list))


if __name__ == "__main__":
    main()
