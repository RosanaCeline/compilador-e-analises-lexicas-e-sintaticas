# Questão A: Analisador léxico de equações do 1º grau

Analisador léxico feito com Python + PLY que reconhece os tokens de uma equação do 1º grau (`ax + b = 0`): números, variáveis, os operadores `+ - * /` e o operador de igualdade `=`. A interface usa Gradio, com um campo de entrada, um campo de saída e o botão **Analisar lexicamente**.

## Arquivos

- `Lexer.py`: regras do lexer (PLY), no formato de classe visto no `MyLexer.py` da Aula 09, e a função `analisar()`, que monta a tabela TOKEN / TIPO / VALOR.
- `app.py`: interface Gradio.

## Como executar

Na raiz do repositório:

```bash
python3 -m venv .venv
.venv/bin/pip install ply gradio
cd QuestoesGerais/A
../../.venv/bin/python app.py        # interface em http://127.0.0.1:7860
# ou, da raiz do repositório: .venv/bin/python -m QuestoesGerais.A.app
../../.venv/bin/python Lexer.py   # só terminal: pede a equação pelo teclado
```

Nos dois modos, cada análise aparece no terminal: primeiro os `LexToken(tipo,valor,linha,posição)` produzidos pelo lexer, como no `calclex.py` da aula, depois a tabela TOKEN / TIPO / VALOR. Usando o `app.py`, a tabela também aparece na interface do Gradio.

## Tokens

| Token PLY | Expressão regular | TIPO | VALOR |
|---|---|---|---|
| `NUMERO` | `\d+(\.\d+)?` | NÚMERO | o próprio número |
| `VARIAVEL` | `[a-zA-Z_][a-zA-Z_0-9]*` | VARIÁVEL | o nome da variável |
| `SOMA` | `\+` | OPERADOR | SOMA |
| `SUBTRACAO` | `-` | OPERADOR | SUBTRAÇÃO |
| `MULTIPLICACAO` | `\*` | OPERADOR | MULTIPLICAÇÃO |
| `DIVISAO` | `/` | OPERADOR | DIVISÃO |
| `IGUALDADE` | `=` | IGUALDADE | IGUALDADE |

Espaços e tabulações são ignorados (`t_ignore`). Um caractere que não pertence a nenhum token (por exemplo `@`) aparece na tabela como **ERRO LÉXICO**, com a posição em que foi encontrado, e a análise continua no caractere seguinte (`t.lexer.skip(1)`).

## Exemplo

Entrada: `5 * x + 10 = 0`

| TOKEN | TIPO | VALOR |
|---|---|---|
| 5 | NÚMERO | 5 |
| * | OPERADOR | MULTIPLICAÇÃO |
| x | VARIÁVEL | x |
| + | OPERADOR | SOMA |
| 10 | NÚMERO | 10 |
| = | IGUALDADE | IGUALDADE |
| 0 | NÚMERO | 0 |
