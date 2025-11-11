class UnionFind:
    """Estrutura de dados Union-Find para o Kruskal."""
    def __init__(self, vertices):
        # Mapeia vértices (tuplas) para um ID inteiro para facilitar
        self.vertex_map = {vertex: i for i, vertex in enumerate(vertices)}
        self.reverse_map = {i: vertex for i, vertex in enumerate(vertices)}
        self.parent = list(range(len(vertices)))
        self.rank = [0] * len(vertices)

    def find(self, v):
        """Encontra o representante do conjunto de v com compressão de caminho."""
        i = self.vertex_map[v]
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.reverse_map[self.parent[i]]) # Compressão
        return self.parent[i]

    def union(self, v1, v2):
        """Une os conjuntos de v1 e v2 usando 'union by rank'."""
        root1 = self.find(v1)
        root2 = self.find(v2)
        
        if root1 != root2:
            # Union by rank
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1
            return True
        return False

def gerar_mst_kruskal(vertices, edges_for_kruskal):
    """
    Gera a Árvore Geradora Mínima (MST) usando o algoritmo de Kruskal.
    Retorna:
    - mst_graph (dict): A MST como um grafo (lista de adjacência).
    - mst_edges (list): A lista de arestas da MST no formato (dist, v1, v2).
    """
    # Ordena as arestas pelo peso (distância)
    edges_for_kruskal.sort()
    
    uf = UnionFind(vertices)
    mst_edges = []
    
    for dist, v1, v2 in edges_for_kruskal:
        if uf.union(v1, v2):
            mst_edges.append((dist, v1, v2))
            
    # Constrói a lista de adjacência da MST
    mst_graph = {v: [] for v in vertices}
    for dist, v1, v2 in mst_edges:
        mst_graph[v1].append((v2, dist))
        mst_graph[v2].append((v1, dist))
        
    return mst_graph, mst_edges
