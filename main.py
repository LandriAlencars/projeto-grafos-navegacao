import sys
import map_reader
import visibility_graph
import mst
import path_finding
import plotter

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo_do_mapa>")
        print("Exemplo: python main.py mapa.txt")
        return

    map_file = sys.argv[1]

    # --- Passo 2 (Leitura) ---
    print(f"[Passo 2] Lendo o mapa de '{map_file}'...")
    q_start, q_goal, obstaculos = map_reader.ler_mapa(map_file)
    if q_start is None:
        return
    print("... Leitura do mapa concluída.")
    
    # --- Passo 2 (Grafo de Visibilidade) ---
    print("[Passo 2] Construindo o Grafo de Visibilidade...")
    all_vertices, vis_edges = visibility_graph.construir_grafo_visibilidade(
        q_start, q_goal, obstaculos
    )
    print(f"... Grafo de Visibilidade criado com {len(all_vertices)} vértices e {len(vis_edges)} arestas visíveis.")

    # --- Passo 3 (MST com Kruskal) ---
    print("[Passo 3] Gerando a Árvore Geradora Mínima (MST) com Kruskal...")
    mst_graph, mst_edges = mst.gerar_mst_kruskal(all_vertices, vis_edges)
    print(f"... MST gerada com {len(mst_edges)} arestas.")

    # --- Passo 5 (Busca na Árvore) ---
    print(f"[Passo 5] Buscando caminho de {q_start} para {q_goal} na MST...")
    caminho = path_finding.buscar_na_arvore_bfs(q_start, q_goal, mst_graph)
    
    if caminho:
        print("... Caminho encontrado!")
        print(" -> ".join(map(str, caminho)))
    else:
        print("... Nenhum caminho encontrado na MST.")

    # --- Passo 4 (Teste do verticeMaisProximo) ---
    # Apenas para demonstrar a função
    ponto_teste = (5.0, 5.0)
    vertice_prox = path_finding.vertice_mais_proximo(ponto_teste, mst_graph)
    print(f"\n[Passo 4 - Teste] O vértice da MST mais próximo de {ponto_teste} é {vertice_prox}")

    # --- Passo 6 (Plotar) ---
    print("[Passo 6] Plotando o resultado...")
    plotter.plotar_caminho(q_start, q_goal, obstaculos, mst_edges, caminho)

if __name__ == "__main__":
    main()
