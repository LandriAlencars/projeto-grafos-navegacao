import math

# --- Funções Auxiliares de Geometria ---

def euclidean_distance(p1, p2):
    """Calcula a distância Euclidiana entre dois pontos (tuplas)."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# --- Funções para Checagem de Interseção de Segmentos ---

def on_segment(p, q, r):
    """Dado 3 pontos colineares p, q, r, checa se q está no segmento pr."""
    return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

def orientation(p, q, r):
    """Encontra a orientação do trio (p, q, r).
    Retorna:
    0 --> p, q, r são colineares
    1 --> Sentido horário
    2 --> Sentido anti-horário
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0: return 0  # Colinear
    return 1 if val > 0 else 2  # Horário ou Anti-horário

def do_intersect(p1, q1, p2, q2):
    """Retorna True se os segmentos (p1, q1) e (p2, q2) se interceptam."""
    # Encontra as 4 orientações
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # --- Caso Geral ---
    # Se (p1, q1, p2) e (p1, q1, q2) têm orientações diferentes E
    # (p2, q2, p1) e (p2, q2, q1) têm orientações diferentes.
    if (o1 != o2 and o3 != o4):
        return True

    # --- Casos Especiais (Colineares) ---
    if (o1 == 0 and on_segment(p1, p2, q1)): return True
    if (o2 == 0 and on_segment(p1, q2, q1)): return True
    if (o3 == 0 and on_segment(p2, p1, q2)): return True
    if (o4 == 0 and on_segment(p2, q1, q2)): return True

    return False

# --- Função para Checagem de Ponto-Dentro-de-Polígono (Ray Casting) ---

def is_inside(polygon, p):
    """Retorna True se o ponto p está dentro do polygon."""
    n = len(polygon)
    if n < 3:
        return False

    # Cria um ponto "infinito"
    extreme = (float('inf'), p[1])
    
    count = 0  # Contador de interseções
    i = 0
    while True:
        j = (i + 1) % n
        v_i = polygon[i]
        v_j = polygon[j]

        # Checa se o segmento (p, extreme) intercepta o segmento (v_i, v_j)
        if do_intersect(v_i, v_j, p, extreme):
            # Se o ponto p é colinear com v_i e v_j, checa se ele está no segmento
            if orientation(v_i, p, v_j) == 0:
                return on_segment(v_i, p, v_j)
            count += 1
        
        i = j
        if i == 0:
            break
            
    # Retorna True se o contador for ímpar
    return count % 2 == 1
