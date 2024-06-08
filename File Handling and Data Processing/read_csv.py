import csv
from typing import List, Dict

def read_csv(file_path: str) -> List[Dict[str, str]]:
    
    rows = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            rows.append(dict(row))
    return rows

# Example usage:
file_path = r'C:\Users\redda\Downloads\sample1.csv' 
rows = read_csv(file_path)
print(rows)