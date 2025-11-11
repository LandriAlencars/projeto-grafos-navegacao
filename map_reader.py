def ler_mapa(filepath):
    """
    Lê o arquivo de mapa no formato especificado.
    Retorna: q_start (tuple), q_goal (tuple), obstaculos (lista de listas de tuplas)
    """
    obstaculos = []
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
            
            # 1. Ponto Inicial
            q_start_coords = lines[0].strip().split(',')
            q_start = (float(q_start_coords[0]), float(q_start_coords[1]))
            
            # 2. Ponto Final
            q_goal_coords = lines[1].strip().split(',')
            q_goal = (float(q_goal_coords[0]), float(q_goal_coords[1]))
            
            # 3. Número de Obstáculos
            num_obstaculos = int(lines[2].strip())
            
            line_index = 3
            for _ in range(num_obstaculos):
                # 4. Número de Quinas do Obstáculo
                num_quinas = int(lines[line_index].strip())
                line_index += 1
                
                obstaculo = []
                for _ in range(num_quinas):
                    # 5. Coordenadas das Quinas
                    coords = lines[line_index].strip().split(',')
                    obstaculo.append((float(coords[0]), float(coords[1])))
                    line_index += 1
                
                obstaculos.append(obstaculo)
                
            return q_start, q_goal, obstaculos
            
    except Exception as e:
        print(f"Erro ao ler o arquivo de mapa: {e}")
        return None, None, None
