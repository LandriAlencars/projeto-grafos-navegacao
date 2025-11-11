from collections import deque
from helpers import euclidean_distance

def vertice_mais_proximo(posicao, arvore_mst):
    """
    (Passo 4) Encontra o vértice na árvore MST mais próximo da 'posicao'.
    """
    vertices = list(arvore_mst.keys())
    if not vertices:
        return None
        
    # Encontra o vértice com a menor distância
    vertice_prox = min(vertices, key=lambda v: euclidean_distance(posicao, v))
    return vertice_prox

def buscar_na_arvore_bfs(v_inicial, v_final, arvore_mst):
    """
    (Passo 5) Encontra o caminho único entre v_inicial e v_final na árvore MST.
    Usa BFS para encontrar o caminho e reconstrói-lo.
    """
    if v_inicial == v_final:
        return [v_inicial]

    queue = deque([v_inicial])
    visited = {v_inicial}
    parent = {v_inicial: None} # Dicionário para rastrear os pais

    path_found = False
    while queue:
        u = queue.popleft()
        
        if u == v_final:
            path_found = True
            break
            
        for v, dist in arvore_mst[u]:
            if v not in visited:
                visited.add(v)
                parent[v] = u
                queue.append(v)
                
    # Reconstrói o caminho
    path = []
    if path_found:
        curr = v_final
        while curr is not None:
            path.append(curr)
            curr = parent[curr]
        path.reverse() # O caminho é de v_final para v_inicial, então invertemos
        
    return path
