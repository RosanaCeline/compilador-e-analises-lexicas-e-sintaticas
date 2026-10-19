# ------------------------------------------------------------
# Código-Fonte: MyLexer.py (módulo) - PLY Version: 3.11
# Objetivo: Exemplifica que o módulo também pode ser usada
# para definir lexers de instâncias de uma classe.
# Tokens: numbers and +,-,*,/
# Autor: David M. Beazley (dave@dabeaz.com)
# URL: https://www.dabeaz.com/ply/ply.html#ply_nn17
# ------------------------------------------------------------

import ply.lex as lex

class MyLexer(object):
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
    # Observe a adição do parâmetro próprio, pois estamos em uma classe
    def t_NUMBER(self,t):
        r'\d+'
        t.value = int(t.value)    
        return t
 
    # Defina uma regra para que possamos rastrear os números das linhas
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)
 
    # Uma string contendo caracteres ignorados (espaços e tabulações)
    t_ignore  = ' \t'
 
    # Regra de tratamento de erros
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
 
    # Constroe o lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
     
    # Teste de saída
    def test(self,data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok: 
                break
            print(tok)
 
# Constroe o lexer e experimenta
m = MyLexer()
m.build()           # Constroe o lexer
m.test("3 + 4")     # Testa com uma expressão
