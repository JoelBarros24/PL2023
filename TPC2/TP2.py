# Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
# Prepare o programa para ler o texto do canal de entrada: stdin;
# Sempre que encontrar a ‘string’ “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
# Sempre que encontrar a ‘string’ “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
# Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

import sys
import re


def main():
    on_off_pattern = re.compile(r'on(.+?)off')
    print_pattern = re.compile(r'(.+?)=')
    is_digit_pattern = re.compile(r'\d')

    for line in sys.stdin:
        total = 0
        line = line.lower()

        content = on_off_pattern.search(line).group(1)  # devolve o conteúdo dentro dos limites [ON, OFF].
        break_content = print_pattern.findall(content)  # encontra todas as substrings que terminam em =.
        print(content)
        print(break_content)
        for item in break_content:
            digit_sequence = is_digit_pattern.findall(
                item)  # devolve uma lista com as sequências de dígitos no conteúdo.
            total += sum(map(int, digit_sequence))  # converte uma lista de dígitos em inteiros e faz o somatório.
            print(total)


if __name__ == '__main__':
    main()
