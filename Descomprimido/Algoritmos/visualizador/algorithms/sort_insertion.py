# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # común: arrancar en el segundo elemento
    j = None

def step():
    global items, n, i, j
    if i >= n:
        return {"done": True}
    
    if j == None:
        j = i 
        return {"highlight": True}
    
    a = j
    b = j-1
    swap = False

    if j > 0 and items[b] > items[a]:
        items[b], items[a] = items[a], items[b]
        swap = True

    if j > 0: 
        j = j-1
        return {"a": a, "b": b, "swap": swap, "done": False}
    i += 1
    j = None
    return {"a": a, "b": b, "swap": swap, "done": False}