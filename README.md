# Prática 2 - Grafos para Navegação de Robô

Este projeto implementa um planejador de caminhos para um robô em um ambiente 2D com obstáculos poligonais, utilizando um **Grafo de Visibilidade** e uma **Árvore Geradora Mínima (MST)**.

O projeto segue os passos definidos na atividade acadêmica:
1.  **Leitura do Mapa:** Lê um arquivo `.txt` contendo as posições de início/fim e as coordenadas dos vértices dos obstáculos.
2.  **Grafo de Visibilidade:** Constrói um grafo onde os vértices são as quinas dos obstáculos e os pontos de início/fim. Uma aresta existe se houver linha de visada direta (sem cruzar obstáculos) entre dois vértices.
3.  **MST:** Aplica o algoritmo de **Kruskal** para encontrar a Árvore Geradora Mínima do grafo de visibilidade.
4.  **Vértice Mais Próximo:** Inclui uma função para encontrar o vértice da árvore mais próximo de um ponto qualquer.
5.  **Busca na Árvore:** Utiliza **BFS (Busca em Largura)** para encontrar o caminho único entre o início e o fim na MST.
6.  **Plotagem:** Usa `matplotlib` para visualizar o mapa, os obstáculos, a MST e o caminho final.

## 🚀 Instruções de Uso

### 1. Pré-requisitos

-   Python 3.x
-   `matplotlib`

### 2. Instalação

Clone o repositório e instale a dependência:

```bash
git clone [https://github.com/seu-usuario/projeto-grafos-navegacao.git](https://github.com/seu-usuario/projeto-grafos-navegacao.git)
cd projeto-grafos-navegacao
pip install matplotlib
