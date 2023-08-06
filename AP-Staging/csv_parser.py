import csv
import sys

def parse_csv(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

if __name__ == "__main__":
    csv_path = sys.argv[1]
    parsed_data = parse_csv(csv_path)
    print(parsed_data)
