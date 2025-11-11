from helpers import euclidean_distance, do_intersect, is_inside

def construir_grafo_visibilidade(q_start, q_goal, obstaculos):
    """
    Constrói o grafo de visibilidade.
    Retorna:
    - all_vertices (list): Lista de todos os vértices (q_start, q_goal, quinas).
    - edges_for_kruskal (list): Lista de arestas visíveis no formato (dist, v1, v2).
    """
    all_vertices = [q_start, q_goal]
    all_obstacle_edges = []
    
    for obs in obstaculos:
        all_vertices.extend(obs)
        for i in range(len(obs)):
            edge = (obs[i], obs[(i + 1) % len(obs)])
            all_obstacle_edges.append(edge)

    edges_for_kruskal = []
    
    # Itera sobre todos os pares de vértices
    for i in range(len(all_vertices)):
        for j in range(i + 1, len(all_vertices)):
            v1 = all_vertices[i]
            v2 = all_vertices[j]
            
            is_visible = True

            # 1. Checa se o *ponto médio* está dentro de algum obstáculo
            # (Conforme a dica do Point-In-Polygon)
            midpoint = ((v1[0] + v2[0]) / 2.0, (v1[1] + v2[1]) / 2.0)
            for obs in obstaculos:
                if is_inside(obs, midpoint):
                    is_visible = False
                    break
            if not is_visible:
                continue

            # 2. Checa se o segmento cruza *propriamente* alguma aresta de obstáculo
            for p2, q2 in all_obstacle_edges:
                # Ignora se o segmento for a própria aresta
                if (v1 == p2 and v2 == q2) or (v1 == q2 and v2 == p2):
                    continue
                
                if do_intersect(v1, v2, p2, q2):
                    # Interseção é permitida *apenas* se for em um vértice compartilhado
                    if v1 in (p2, q2) or v2 in (p2, q2):
                        continue # Aresta "fã" saindo de um vértice
                    
                    # Se não for apenas em um vértice, é uma interseção própria
                    is_visible = False
                    break
            
            if is_visible:
                dist = euclidean_distance(v1, v2)
                edges_for_kruskal.append((dist, v1, v2))
                
    return all_vertices, edges_for_kruskal
