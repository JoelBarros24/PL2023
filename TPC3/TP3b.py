import re
import matplotlib.pyplot as plt

file_open = open('processos.txt', 'r')
re_names = re.compile(r'(?<!,)[A-Z][a-z]+(?!(\w*\.))')
re_dates = re.compile(r'\b\d{4}-\d{2}-\d{2}\b')

i = 0

for line in file_open:
    content = re.split('::', line)
    print(content)
    # print(re_names.match(line))
    # print(first_names)
    i += 1
    if i > 50:
        break
