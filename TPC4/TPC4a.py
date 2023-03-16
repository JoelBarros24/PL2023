import csv
import json

def convert_csv_to_json(csv_file, json_file):
    csv_file = open(csv_file, 'r')
    json_file = open(json_file, 'w', encoding='utf-8')

    reader = csv.DictReader(csv_file)
    json_data = list()

    for row in reader:
        json_data.append(row)
        
    json.dump(json_data, json_file, indent=4, ensure_ascii=False)
        
def main():
    convert_csv_to_json('/home/joel/Documents/GitHub/PL2023/TPC4/alunos.csv', '/home/joel/Documents/GitHub/PL2023/TPC4/alunos.json')
    
if __name__ == '__main__':
    main()