# ------------------------------------------------------------
# Código-Fonte: Lexer.py - PLY Version: 3.11
# Objetivo: analisa lexicamente uma equação do 1º grau (ax + b = 0)
# Tokens: números, variáveis, +, -, *, / e =
# Base: calclex.py e MyLexer.py (Aula 09 - Análise Léxica em Python)
# ------------------------------------------------------------
import ply.lex as lex


class LexerEquacao(object):
    # Lista de nomes de tokens. Isso é sempre necessário
    tokens = (
        'NUMERO',
        'VARIAVEL',
        'SOMA',
        'SUBTRACAO',
        'MULTIPLICACAO',
        'DIVISAO',
        'IGUALDADE',
    )

    # Regras de expressão regular para tokens simples
    t_SOMA          = r'\+'
    t_SUBTRACAO     = r'-'
    t_MULTIPLICACAO = r'\*'
    t_DIVISAO       = r'/'
    t_IGUALDADE     = r'='

    # Números inteiros ou decimais (ex.: 5, 10, 2.5)
    def t_NUMERO(self, t):
        r'\d+(\.\d+)?'
        t.value = float(t.value) if '.' in t.value else int(t.value)
        return t

    # Variáveis: mesma regra do t_ID visto na aula
    def t_VARIAVEL(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        return t

    # Define uma regra para rastrear os números das linhas
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Uma string contendo caracteres ignorados (espaços e tabulações)
    t_ignore = ' \t'

    # Regra de tratamento de erros: guarda o caractere ilegal em vez de
    # imprimir, para que a interface possa exibi-lo
    def t_error(self, t):
        self.erros.append((t.value[0], t.lexpos))
        t.lexer.skip(1)

    # Constroe o lexer
    def build(self, **kwargs):
        self.erros = []
        self.lexer = lex.lex(module=self, **kwargs)

    # Tokeniza a entrada e devolve a lista de tokens
    def tokenizar(self, data):
        self.erros = []
        self.lexer.lineno = 1
        self.lexer.input(data)
        return list(self.lexer)


# Tipo e valor exibidos para cada token, conforme a tabela do enunciado
TIPOS = {
    'NUMERO':        'NÚMERO',
    'VARIAVEL':      'VARIÁVEL',
    'SOMA':          'OPERADOR',
    'SUBTRACAO':     'OPERADOR',
    'MULTIPLICACAO': 'OPERADOR',
    'DIVISAO':       'OPERADOR',
    'IGUALDADE':     'IGUALDADE',
}

VALORES = {
    'SOMA':          'SOMA',
    'SUBTRACAO':     'SUBTRAÇÃO',
    'MULTIPLICACAO': 'MULTIPLICAÇÃO',
    'DIVISAO':       'DIVISÃO',
    'IGUALDADE':     'IGUALDADE',
}


def analisar(equacao):
    # Devolve as linhas (TOKEN, TIPO, VALOR) da análise léxica, em ordem de posição na entrada. Caracteres ilegais aparecem como ERRO LÉXICO.
    m = LexerEquacao()
    m.build()
    toks = m.tokenizar(equacao)

    linhas = []
    for tok in toks:
        valor = VALORES.get(tok.type, str(tok.value))
        linhas.append((tok.lexpos, str(tok.value), TIPOS[tok.type], valor))
    for caractere, pos in m.erros:
        linhas.append((pos, caractere, 'ERRO LÉXICO',
                       'caractere ilegal na posição %d' % pos))

    linhas.sort(key=lambda linha: linha[0])
    tabela = [list(linha[1:]) for linha in linhas]

    imprimir(equacao, toks, m.erros, tabela)
    return tabela


def imprimir(equacao, toks, erros, tabela):
    # Mostra no terminal a saída do lexer (LexToken) e a tabela final.
    print('\nEntrada: %s' % equacao)

    # Saída do próprio lexer, como no calclex.py: LexToken(tipo,valor,linha,posição)
    for tok in toks:
        print(tok)
    for caractere, pos in erros:
        print("Illegal character '%s' na posição %d" % (caractere, pos))

    print('\n%-8s %-12s %s' % ('TOKEN', 'TIPO', 'VALOR'))
    for token, tipo, valor in tabela:
        print('%-8s %-12s %s' % (token, tipo, valor))


# Teste no terminal: lê equações até receber uma linha vazia
if __name__ == '__main__':
    while True:
        try:
            equacao = input('\nDigite a equação do 1º grau (Enter para sair): ')
        except EOFError:
            break
        if not equacao.strip():
            break
        analisar(equacao)
