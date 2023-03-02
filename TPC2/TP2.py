# Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
# Prepare o programa para ler o texto do canal de entrada: stdin;
# Sempre que encontrar a ‘string’ “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
# Sempre que encontrar a ‘string’ “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
# Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

import sys
import re


def main():
    total = 0
    on_off_pattern = re.compile(r'on(.+?)off')
    is_digit_pattern = re.compile(r'\d+')
    # print_pattern = re.compile(r'=')

    for line in sys.stdin:
        line = line.lower()
        res = on_off_pattern.search(line).group(1)  # devolve o conteúdo dentro dos limites [ON, OFF].
        print(res)
        digit_sequence = is_digit_pattern.findall(res)  # devolve uma lista com as sequências de dígitos no conteúdo.
        print(digit_sequence)
        total += sum(map(int, digit_sequence))  # converte uma lista de dígitos em inteiros e faz o somatório.


if __name__ == '__main__':
    main()
