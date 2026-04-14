# Processamento Digital de Imagens — UNEMAT / BCC

Repositório das atividades práticas da disciplina **Processamento Digital de Imagens**
(Bacharelado em Ciência da Computação — UNEMAT), ministrada pelo
**Prof. Dr. Carlos Alex Sander J. Gulo** no semestre **2026/1**.

**Aluno:** Lucas Tiago Siqueira

---

## Atividade Prática 1.2 — Implementação e Governança

A atividade está em [`lista_1/`](lista_1/) e resolve os **20 exercícios** propostos
usando **OpenCV**, **NumPy** e **Matplotlib** sobre fotografias autorais
(capturadas com celular).

### Abrir direto no Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1IiQ0_6jrdW9O6I4nwELJv-1-1M2LeFC4?usp=sharing)

Link direto:
<https://colab.research.google.com/drive/1IiQ0_6jrdW9O6I4nwELJv-1-1M2LeFC4?usp=sharing>

> O notebook executa **de ponta a ponta** no Colab sem ajuste manual de caminhos.
> As imagens autorais são baixadas automaticamente do próprio repositório via
> `!wget` a partir das URLs *raw* do GitHub.

### Estrutura da pasta `lista_1/`

```
lista_1/
├── Atividade_Avaliativa_1 (Lucas Tiago Siqueira).ipynb   # Notebook principal com os 20 exercícios
├── build_notebook.py             # Script que gera o .ipynb a partir do código-fonte
└── pics/                         # Imagens autorais usadas nos exercícios
    ├── IMG_1443.jpg
    ├── IMG_1834.jpg
    ├── IMG_2433.jpg
    ├── IMG_2520.jpg
    └── IMG_6574.jpg
```


```bash
# 1. Clonar o repositório
git clone https://github.com/LucasTiagoUNEMAT/PDI_lucas_tiago_siqueira.git
cd PDI_lucas_tiago_siqueira/lista_1

# 2. Instalar as bibliotecas
pip install opencv-python numpy matplotlib jupyter

# 3. Abrir o notebook
jupyter notebook Atividade_Avaliativa_1 (Lucas Tiago Siqueira).ipynb
```

As imagens já estão versionadas em `lista_1/pics/`, portanto o notebook
roda tanto localmente quanto no Colab sem nenhum ajuste manual.

### Bibliotecas utilizadas

| Biblioteca | Versão mínima | Função |
|------------|---------------|--------|
| `opencv-python` | 4.x | Leitura, escrita e operações sobre imagens |
| `numpy`         | 1.20+ | Manipulação das matrizes de pixels |
| `matplotlib`    | 3.x | Exibição de imagens e plotagem de histogramas |

No Colab essas bibliotecas já vêm pré-instaladas — ainda assim, a primeira
célula do notebook executa `pip install --quiet opencv-python numpy matplotlib`
para garantir funcionamento em qualquer ambiente limpo.

### Lista dos 20 exercícios implementados

| # | Exercício |
|---|-----------|
| 1 | Carregar imagem colorida e exibir com correção BGR → RGB |
| 2 | Atributos `shape`, `size` e `dtype` |
| 3 | Salvar cópia em formato de compressão diferente (JPG → PNG) |
| 4 | Pixel central: valores R, G, B |
| 5 | Pintar região 100×100 no canto superior |
| 6 | Recorte (ROI) de um detalhe |
| 7 | Separar canais B, G e R |
| 8 | Canal Verde isolado em escala de cinza |
| 9 | `merge` com troca de R e B |
| 10 | Conversão para tons de cinzento |
| 11 | Conversão para HSV e extração do canal S |
| 12 | Aumento de brilho (+50) com `cv2.add` (saturação) |
| 13 | Mesclagem de duas imagens com `addWeighted` |
| 14 | Negativo fotográfico em escala de cinza |
| 15 | Máscara binária circular com `bitwise_and` |
| 16 | Redução para 30% do tamanho original |
| 17 | Cálculo e impressão dos valores do histograma |
| 18 | Histograma dos três canais no mesmo gráfico |
| 19 | Equalização de histograma (imagem escura) |
| 20 | Threshold binário simples |

### Governança e autoria

- Todas as fotografias em `lista_1/pics/` são de **autoria do próprio aluno**,
  capturadas com celular.
- O código está organizado em um único Jupyter Notebook, com células de
  texto em **Markdown** separando e explicando cada exercício, e comentários
  no código.
- O notebook é gerado a partir do script [`lista_1/build_notebook.py`](lista_1/build_notebook.py),
  que facilita a manutenção do conteúdo sem precisar editar o JSON `.ipynb`
  diretamente. Para regenerar o notebook após qualquer alteração no script:

  ```bash
  cd lista_1
  python build_notebook.py
  ```
