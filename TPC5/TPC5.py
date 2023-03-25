import re

class cabine:
    re_moedas = re.compile(r'(?<=MOEDA\s)(?:[,\s]*[0-9]+[ce]?)*')
    re_number = re.compile(r'(?<=T\=)(?:[0-9]+)*')
    re_bloq_num = re.compile(r'^(601|641)')
    re_inter_num = re.compile(r'^00')
    re_nat_num = re.compile(r'^2\d{8}')
    re_green_num = re.compile(r'^800\d{6}')
    re_blue_num = re.compile(r'^808\d{6}')
    re_cent = re.compile(r'\d+c')
    re_euro = re.compile(r'\d+e')
    
    moedas_validas = {'1c', '2c', '5c', '10c', '20c', '50c', '1e', '2e'}
    
    def __init__(self):
        self.balance = 0 
        self.state = 'POUSAR'
        
    def process_number(self, number):
        if self.re_bloq_num.search(number):
            print('Máquina: Número Bloqueado')
        elif self.re_inter_num.search(number):
            print('Número Internacional; Tarifa = 1e50c')
            if self.balance < 150: # 1.50
                self.state = 'LEVANTAR'
                print('Máquina: Saldo Insuficiente, insira mais moedas')
            else:
                self.balance -= 150
                self.state = 'T'
                print('Máquina: Chamada em curso')
        elif self.re_nat_num.match(number):
            print('Número Nacional; Tarifa = 25c')
            if self.balance < 25:
                self.state = 'LEVANTAR'
                print('Máquina: Saldo Insuficiente, insira mais moedas')
            else:
                self.balance -= 25
                self.state = 'T'
                print('Máquina: Chamada em curso')
        elif self.re_green_num.match(number):
            print('Número Gratuito; Tarifa = 0c')
            self.state = 'T'
            print('Máquina: Chamada em curso')
        elif self.re_blue_num.match(number):
            print('Número Azul; Tarifa = 10c')
            if self.balance < 10:
                self.state = 'LEVANTAR'
                print('Máquina: Saldo Insuficiente, insira mais moedas')
            else:
                self.balance -= 10
                self.state = 'T'
                print('Máquina: Chamada em curso')
                
                
    def process_input(self, input):
        if self.state == 'POUSAR':
            if input == 'LEVANTAR':
                self.state = 'LEVANTAR'
                print('Máquina: Introduza moedas')
            else:
                print('Estados Possíveis: {}'.format('LEVANTAR'))
        elif self.state == 'LEVANTAR':
            if 'MOEDA' in input:
                self.state = 'MOEDA'
                moedas = self.re_moedas.search(input).group(0).split(', ')
                invalidas = list()
                for moeda in moedas:
                    if moeda not in self.moedas_validas:
                        invalidas.append(moeda)
                    else:
                        if self.re_cent.search(moeda):
                            self.balance += int(moeda[:-1]) 
                        elif self.re_euro.search(moeda):
                            self.balance += int(moeda[:-1]) * 100
                print('Máquina: {} - Moedas Inválidas; Saldo = {}e{}c'.format(" ".join(invalid_coin for invalid_coin in invalidas) , self.balance // 100, self.balance % 100))
            elif input == 'ABORTAR':
                self.state = 'POUSAR'
                print('Máquina: A operação foi interrompida')
            else:
                print('Estados Possíveis: {}'.format('MOEDA, ABORTAR'))
        elif self.state == 'MOEDA':
            if input == 'ABORTAR':
                self.state = 'POUSAR'
                print('Máquina: A operação foi interrompida. Troco = {}e{}c'.format(self.balance // 100, self.balance % 100))
                self.balance = 0
            elif 'T=' in input:
                telefone = self.re_number.search(input).group(0)
                self.process_number(telefone)
            else:
                print('Estado Possíveis: {}'.format('T, ABORTAR'))
        elif self.state == 'T':
            if input == 'POUSAR':
                self.state = 'POUSAR'
                euros = self.balance // 100
                centimos = self.balance % 100
                print('Máquina: A operação foi interrompida. Troco = {}e{}c'.format(euros, centimos))
                self.balance = 0
            else:
                print('Estados Possíveis: {}'.format('POUSAR'))


def main():
    cabinete = cabine()
    while True:
        cabinete.process_input(input())
        
        
if __name__ == '__main__':
    main()
                        