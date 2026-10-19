# Compiladores: Trabalho Computacional 02

Repositório da **Equipe 02** para o Trabalho Computacional 02 (Análise Léxica, Análise Sintática e Compilador Básico) da disciplina de Compiladores, do curso de Bacharelado em Ciência da Computação do **IFCE, Campus Tianguá**.

| | |
|---|---|
| **Disciplina** | Compiladores |
| **Professor** | Adonias Caetano de Oliveira |
| **Equipe** | 02 |
| **Prazo de entrega** | 18/12/2026 |

## Integrantes

- Laís Coutinho
- Rosana Celine
- Cláudia Ferreira
- Thaís Araújo
- Thalyta Lima

## Sobre este repositório

Este repositório reúne, em um só lugar, tudo o que a equipe produz para o trabalho: os códigos, as simulações e os arquivos das ferramentas utilizadas (JFLAP, GALS, Verto, C, Java e Python).

Ele serve para:

- **Centralizar o trabalho da equipe**, para que todas tenham acesso à versão mais recente de cada solução.
- **Dividir as tarefas** entre as integrantes, com cada questão em sua própria pasta e o histórico de quem fez o quê.
- **Servir como entrega oficial**: o link deste repositório é enviado ao professor pelo Classroom junto com o link do vídeo de apresentação.

## Enunciados

Os enunciados do trabalho **não estão replicados aqui**. Para ver as questões gerais (todas as equipes) e as questões específicas da Equipe 02, consulte o PDF oficial:

📄 [`docs/N2_Trabalho Computacional 02.pdf`](docs/N2_Trabalho% Computacional 02.pdf)

O PDF também traz as regras de apresentação, os critérios de avaliação e as instruções para a entrega em vídeo.

## Estrutura do repositório

```
.
├── docs/
│   └── N2_Trabalho Computacional 02.pdf   # enunciado oficial do trabalho
├── QuestoesGerais/                        # questões resolvidas por todas as equipes
│   └── q1/
└── README.md
```

- **`docs/`**: documentos de referência, como o enunciado em PDF. Materiais de apoio também ficam aqui.
- **`QuestoesGerais/`**: soluções das questões gerais, uma subpasta por questão.
- À medida que as questões da equipe forem sendo resolvidas, cada uma ganha a sua própria pasta, mantendo o mesmo padrão.

## Como organizamos o trabalho

- **Uma pasta por questão**, com o código-fonte, os arquivos de entrada e de teste e, quando necessário, um `README` curto explicando como executar.
- Cada integrante trabalha na sua parte e envia por **commits pequenos e com mensagens claras** (por exemplo, `Adiciona analisador léxico da questão A`).
- Antes de começar a trabalhar, rodar `git pull` para não gerar conflitos. Antes de enviar, conferir com `git status`.
- Para mudanças maiores, usar uma **branch** própria e unir com a `main` depois que a equipe revisar.
- **Não versionar arquivos executáveis** (`.exe`, binários compilados, `.class` etc.), pois o enunciado proíbe compartilhá-los. Só o código-fonte entra no repositório.

## Ferramentas utilizadas

| Ferramenta | Uso |
|---|---|
| **JFLAP** | Construção e simulação de autômatos e gramáticas |
| **GALS** | Geração e teste de analisadores léxicos e sintáticos |
| **Verto** | Observação das etapas do processo de compilação |
| **C** | Analisadores léxicos |
| **Java + JFlex** | Analisadores léxicos |
| **Python + PLY** | Analisador léxico e compilador básico |
| **Gradio** | Interface gráfica das soluções em Python |

## Como executar

Cada pasta de questão traz suas próprias instruções. De forma geral:

```bash
# Python (PLY e Gradio)
pip install ply gradio
python main.py

# C
gcc arquivo.c -o programa && ./programa

# Java + JFlex
jflex arquivo.flex && javac *.java && java Main
```

## Entrega

Resumo do que será entregue pelo Classroom até **18/12/2026**:

1. Link público ou não listado do **vídeo de apresentação** (Google Drive, OneDrive ou YouTube).
2. Link deste **repositório no GitHub**, com todos os códigos.
3. Slides (opcional).

Cada integrante apresenta a sua parte com a **própria voz**, e o tempo máximo é de **45 minutos**. Todos os detalhes estão no PDF da pasta `docs/`.

## Checklist da equipe

- [ ] Equipe registrada no mural do Classroom (número da equipe e nomes das integrantes)
- [ ] Questões gerais concluídas
- [ ] Questões da Equipe 02 concluídas
- [ ] Divisão das partes da apresentação definida
- [ ] Ensaio cronometrado (máximo de 45 min)
- [ ] Vídeo gravado e link conferido (acesso liberado)
- [ ] Entrega feita no Classroom