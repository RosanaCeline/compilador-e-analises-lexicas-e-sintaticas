# ------------------------------------------------------------
# Código-Fonte: calclex.py - PLY Version: 3.11
# Objetivo: analisa lexicamente uma expressão aritmética simples
# Tokens: numbers and +,-,*,/
# Autor: David M. Beazley (dave@dabeaz.com)
# URL: https://www.dabeaz.com/ply/ply.html#ply_nn17
# ------------------------------------------------------------
import ply.lex as lex
 
# Lista de nomes de tokens. Isso é sempre necessário
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)
 
 # Regras de expressão regular para tokens simples
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
 
# Uma regra de expressão regular com algum código de ação
def t_NUMBER(t):
     r'\d+'
     t.value = int(t.value)    
     return t
 
# Define uma regra para rastrear os números das linhas
def t_newline(t):
     r'\n+'
     t.lexer.lineno += len(t.value)
 
# Uma string contendo caracteres ignorados (espaços e tabulações)
t_ignore  = ' \t'
 
# Regra de tratamento de erros
def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)
 
# Constroe o lexer
lexer = lex.lex()
 
# Entrada de teste do analisador léxico
data = '''
 3 + 4 * 10
   + -20 *2
 '''
 
# Dá ao lexer alguma informação
lexer.input(data)


# Tokeniza
while True:
     tok = lexer.token()
     if not tok: 
         break     # Não há mais entrada
     print(tok)

'''
for tok in lexer:
     print(tok)
'''
