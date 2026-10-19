# ------------------------------------------------------------
# Código-Fonte: app.py
# Objetivo: interface Gradio para o analisador léxico de equações
# do 1º grau (Lexer.py)
# Execução: python app.py  (abre em http://127.0.0.1:7860)
#   ou, a partir da raiz do repositório: python -m QuestoesGerais.A.app
# ------------------------------------------------------------
import gradio as gr

try:
    from .Lexer import analisar   # executado como módulo (python -m ...)
except ImportError:
    from Lexer import analisar    # executado como script (python app.py)

COLUNAS = ['TOKEN', 'TIPO', 'VALOR']

with gr.Blocks(title='Analisador Léxico - Equação do 1º Grau') as demo:
    gr.Markdown('# Analisador Léxico de Equações do 1º Grau\n'
                'Digite uma equação no formato `ax + b = 0` e clique em '
                '**Analisar lexicamente**.')

    entrada = gr.Textbox(label='Equação do 1º grau', placeholder='Ex.: 5 * x + 10 = 0')
    botao = gr.Button('Analisar lexicamente', variant='primary')
    saida = gr.Dataframe(label='Análise léxica', headers=COLUNAS, column_count=(3, 'fixed'), interactive=False)

    gr.Examples(['5 * x + 10 = 0', '3x - 7 = 0', '2.5 * y / 4 = 0'], inputs=entrada)

    botao.click(analisar, inputs=entrada, outputs=saida)
    entrada.submit(analisar, inputs=entrada, outputs=saida)

if __name__ == '__main__':
    demo.launch()
