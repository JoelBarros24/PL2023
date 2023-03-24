import re

class cabine:
    re_moedas = re.compile(r'(?<=MOEDA\s)(?:[,\s]*[0-9]+[ce]?)*')
    re_telefone = re.compile(r'(?<=T\=)(?:[0-9]+)*')
    re_cent = re.compile(r'\d+c')
    re_euro = re.compile(r'\d+e')
    
    moedas_validas = {'1c', '2c', '5c', '10c', '20c', '50c', '1e', '2e'}
    
    def __init__(self):
        self.balance = 0 
        self.state = 'POUSAR'
        
    def process_input(self, input):
        if self.state == 'POUSAR':
            if input == 'LEVANTAR':
                self.state = 'LEVANTAR'
                print('Máquina: Introduza moedas')
        elif self.state == 'LEVANTAR':
            if 'MOEDA' in input:
                self.state = 'MOEDA'
                moedas = self.re_moedas.search(input).group(0).split(', ')
                for moeda in moedas:
                    if moeda not in self.moedas_validas:
                        pass
                    else:
                        if self.re_cent.search(moeda):
                            self.balance += int(moeda[:-1]) 
                        elif self.re_euro.search(moeda):
                            self.balance += int(moeda[:-1]) * 100
                print('Máquina: Saldo = {}e{}c'.format(self.balance // 100, self.balance % 100))
            elif input == 'ABORTAR':
                self.state = 'POUSAR'
                print('Máquina: A operação foi interrompida')
        elif self.state == 'MOEDA':
            if input == 'ABORTAR':
                self.state = 'POUSAR'
                print('Máquina: A operação foi interrompida. Troco = {}e{}c'.format(self.balance // 100, self.balance % 100))
                self.balance = 0
            elif 'T' in input:
                self.state = 'T'
                pass
        elif self.state == 'T':
            if input == 'ABORTAR':
                self.state = 'POUSAR'
                euros = self.balance // 100
                centimos = self.balance % 100
                print('Máquina: A operação foi interrompida. Troco = {}e{}c'.format(euros, centimos))
                self.balance = 0
            elif input == 'POUSAR':
                pass


def main():
    cabinete = cabine()
    while True:
        cabinete.process_input(input())
        
        
if __name__ == '__main__':
    main()
                        