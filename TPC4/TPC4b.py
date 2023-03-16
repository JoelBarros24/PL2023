import csv
import json
import re

with open('/home/joel/Documents/GitHub/PL2023/TPC4/alunos2.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    re_list = re.compile(r'^\w+{(\d+)}$')
    re_empty = re.compile(r'^\s*$')

    headers = next(reader)

    json_data = list()

    for row in reader:
        row_dict = dict()
        i = 0
        for item in row:
            res = re_list.match(headers[i])
            if re_empty.match(headers[i]):  # se o cabeçalho for vazio, ignora
                continue
            elif res:
                field_len = int(res.group(1))  # tamanho da lista
                grades = [int(x) for x in row[i:i + field_len]]
                row_dict[headers[i]] = grades
            else:
                row_dict[headers[i]] = item
            i += 1
        json_data.append(row_dict)

        print(json_data)
    # escreve os objetos JSON em um arquivo
    with open('/home/joel/Documents/GitHub/PL2023/TPC4/alunos2.json', 'w') as jsonfile:
        json.dump(json_data, jsonfile, indent=2, ensure_ascii=False)
