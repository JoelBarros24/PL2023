import csv


def parse():
    data = []  # lista que armazena todas as linhas do ficheiro csv
    with open('myheart.csv', 'r') as f:
        leitor = csv.reader(f)
        next(leitor)  # ignora a primeira linha do ficheiro
        for linha in leitor:
            data.append(linha)
    return data


def calculate_disease_by_sex():
    res = {'M': 0, 'F': 0}
    data = parse()
    for linha in data:
        key = linha[1]
        if key in res:
            res[key] += 1
    return res


def find_min_max_age():
    idades = []
    data = parse()
    for linha in data:
        idades.append(linha[0])
    return idades


def calculate_disease_by_age_groups():
    minimum = int(min(find_min_max_age()))
    maximum = int(max(find_min_max_age()))
    i = 0


def main():
    print(calculate_disease_by_sex())
    # print(calculate_disease_by_age_groups())


if __name__ == '__main__':
    main()
