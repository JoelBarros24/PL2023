from collections import OrderedDict
import re
import matplotlib.pyplot as plt

file_open = open('processos.txt', 'r')

re_dates = re.compile(r'\b\d{4}-\d{2}-\d{2}\b')
datas = list()
res = dict()

for line in file_open:
    conteudo = re.split('::', line)
    if len(conteudo) > 1:
        if re_dates.match(conteudo[1]) is not None:
            datas.append(conteudo[1])

for data in datas:
    year = int(data.split('-')[0])
    if year in res:
        res[year] += 1
    else:
        res[year] = 1

sorted_list = list(sorted(res.items()))
print(sorted_list)

figure, axle = plt.subplots()
x_axle = res.keys()
y_axle = res.values()
plt.title('Processos por Ano')
plt.xlabel('Year')
plt.ylabel('Frequency')

axle.bar(x_axle, y_axle)
plt.show()
