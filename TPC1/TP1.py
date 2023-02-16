import csv
from prettytable import PrettyTable


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


def find_ages():
    idades = []
    data = parse()
    for linha in data:
        idades.append(int(linha[0]))
    return min(idades), max(idades)


def calculate_disease_by_age_groups():
    res = dict()
    minimum, maximum = find_ages()
    while minimum < maximum:
        res.update({'[' + str(minimum) + '-' + str(minimum + 4) + ']': 0})
        minimum += 5

    data = parse()
    for linha in data:
        for key in res.keys():
            minimo, maximo = key.strip('[]').split('-')
            if int(minimo) <= int(linha[0]) <= int(maximo):
                res[key] += 1
                break
    return res


def find_cholesterol_values():
    values = []
    data = parse()
    for linha in data:
        values.append(int(linha[3]))
    return sorted(values), min(values), max(values)


# Nesta função, foi buscar o valor mínimo e máximo de colestrol para encontrar o número de níveis.
# Para facilitar a contagem por nível de colestrol, ordenei, por ordem crescente, a lista de valores de colestrol.

def calculate_by_cholesterol_levels():
    res = dict()
    level = 1
    ordered_values, minimum, maximum = find_cholesterol_values()

    temp = minimum

    while temp < maximum:
        res.update({level: 0})
        level += 1
        temp += 10

    level = 1
    for value in ordered_values:
        while value > minimum + 9:
            level += 1
            minimum += 10
        res[level] += 1
        # print('[' + str(minimum) + '-' + str(minimum + 9) + ']' + ':' + str(res[level]))
    return res


def print_table(res):
    table = PrettyTable()

    table.field_names = res.keys()
    table.add_row(res.values())

    print(table)


def main():
    # print(calculate_disease_by_sex())
    # print(calculate_disease_by_age_groups())
    # print(calculate_by_cholesterol_levels())
    # print(find_cholesterol_values())
    print_table(calculate_disease_by_sex())
    print_table(calculate_disease_by_age_groups())
    print_table(calculate_by_cholesterol_levels())


if __name__ == '__main__':
    main()
