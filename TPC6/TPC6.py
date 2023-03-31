import re
import ply.lex as lex
import sys
import re

# List of token names.   This is always required
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ID',
    'LT',
    'GT',
    'ASSIGN',
    'SEMI',
    'COMMA',
    'IF',
    'WHILE',
    'FOR',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'COMMENT',
    'RANGE',
    'IN',
    'PROGRAM',
    'FUNCTION'
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'='
t_SEMI = r';'
t_COMMA = r','
t_LT = r'<'
t_GT = r'>'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_RANGE = r'\.\.'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[\w_][\w_\d]*'
    if t.value == 'if':
        t.type = 'IF'
    elif t.value == 'while':
        t.type = 'WHILE'
    elif t.value == 'for':
        t.type = 'FOR'
    elif t.value == 'in':
        t.type = 'IN'
    elif t.value == 'program':
        t.type = 'PROGRAM'
    elif t.value == 'function':
        t.type = 'FUNCTION'

    return t


def t_newline(t):
    r'\n'
    t.lexer.lineno += 1


def t_COMMENT(t):
    r'(/\*(.|\n)*?\*/)|(//.*)'
    t.lexer.lineno += t.value.count('\n')


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()


def main():
    lexer.input(r"""/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

!

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
""")

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


if __name__ == '__main__':
    main()
