import re

from ply import lex, yacc


tokens = ('LEVANTAR', 'POUSAR', 'MOEDA', 'T', 'ABORTAR')

t_LEVANTAR = r'LEVANTAR'
t_POUSAR = r'POUSAR'
t_MOEDA = r'MOEDA'
t_T = r'T'
t_ABORTAR = r'ABORTAR'

    