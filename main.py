# Para la solucion de este ejercicio puedo realizar un recorrido deepthfirst
# Ya que necesito recorrer en una direccion hasta el fondo antes de cambiar

def get_next(array, i, j, visited_nodes, direction):
    next = None
    
    # izquierda
    if j-1 >= 0 and (i, j-1) not in visited_nodes and direction == "l":
        next = (i, j-1) # si puedo moverme en esa direccion, lo hago
        
    # abajo
    if i+1 < len(array) and (i+1, j) not in visited_nodes and direction == "d":
        next = (i+1, j)
    
    # derecha
    if j+1 < len(array[i]) and (i, j+1) not in visited_nodes and direction == "r":
        next = (i, j+1)
    
    # arriba
    if i-1 >= 0 and (i-1, j) not in visited_nodes and direction == "u": 
        next = (i-1, j)
    print(next)
    return next

def change_direction(prev_direction):
    if prev_direction == "r":
        return "d"
    if prev_direction == "d":
        return "l"
    if prev_direction == "l":
        return "u"
    return "r"

def snail(snail_map):
    # para el caso de un mapa vacio, retorno array vacio
    if len(snail_map) == 1 and len(snail_map[0]) == 0: return []

    visited_nodes = [] # para no repetir nodos que ya visite anteriormente
    direction = "r"
    next = (0,0)
    while next:
        visited_nodes.append(next) # Proceso el nodo actual antes de pasar al siguiente
        aux = get_next(snail_map, next[0], next[1], visited_nodes, direction)
        if not aux: # si no es Verdadero, es decir, si es None, intento en la siguiente direccion
            direction = change_direction(direction)
            next = get_next(snail_map, next[0], next[1], visited_nodes, direction)
            # Si esta direccion tambien es none, Saldra del while
            # significa que ya estoy encerrado
        else:
            next = aux #aux no es None, por lo que existe un siguiente en esa direccion
    
    
    return list(map(lambda x: snail_map[x[0]][x[1]], visited_nodes))
