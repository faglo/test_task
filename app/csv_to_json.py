import csv
import os
from typing import Dict, List


def parse (csv_content: str) -> List[Dict]:
    """
    This function takes a csv string and returns a json string.
    """
    with open("temp.csv", "w") as temp_file:
        temp_file.write(csv_content)
        temp_file.close()
    
    with open("temp.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data = []
        column_names = []
        for row in csv_reader:
            if line_count == 0:
                column_names = row
                line_count += 1
            else:
                json_dict = {}
                for index, k in enumerate(column_names):
                    json_dict.update({k: row[index]})
                data.append(json_dict)
                line_count += 1
        csv_file.close()

    os.remove("temp.csv")
    return data