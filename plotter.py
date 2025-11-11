import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plotar_caminho(q_start, q_goal, obstaculos, mst_edges, caminho, output_filename="caminho_gerado.png"):
    """
    (Passo 6) Plota o mapa, os obstáculos, a MST e o caminho encontrado.
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # 1. Plotar Obstáculos
    for obs in obstaculos:
        ax.add_patch(patches.Polygon(obs, closed=True, facecolor='gray', alpha=0.6))

    # 2. Plotar MST (Arestas em azul tracejado)
    for dist, v1, v2 in mst_edges:
        ax.plot([v1[0], v2[0]], [v1[1], v2[1]], 'b--', alpha=0.4)

    # 3. Plotar Caminho (Linha vermelha sólida)
    if caminho:
        for i in range(len(caminho) - 1):
            p1 = caminho[i]
            p2 = caminho[i+1]
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'r-', linewidth=2.5)

    # 4. Plotar Ponto Inicial (Verde) e Final (Vermelho 'X')
    ax.plot(q_start[0], q_start[1], 'go', markersize=12, label='Início (q_start)')
    ax.plot(q_goal[0], q_goal[1], 'rx', markersize=12, mew=3, label='Objetivo (q_goal)')

    ax.set_title('Grafo de Visibilidade, MST e Caminho Encontrado')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    ax.set_aspect('equal', 'box')
    ax.grid(True, linestyle=':', alpha=0.5)
    
    # Salva e mostra a imagem
    plt.savefig(output_filename)
    print(f"\n[Plotter] Caminho salvo em '{output_filename}'")
    plt.show()
