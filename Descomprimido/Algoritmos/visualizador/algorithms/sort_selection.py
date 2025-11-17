# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual  

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i

def step():
    global items, n, i, j, min_idx, fase

    if i >= n:
        return {"done": True}

    swap = False
    a = min_idx
    b = j
    if j < n:
        if items[b] < items[a]:
            min_idx = j
        j = j + 1
        return {"a": a, "b": b, "swap": swap, "done": False}

    a = i
    b = min_idx

    if min_idx != i:
        items[i], items[min_idx] = items[min_idx], items[i]
        swap = True
    i += 1
    j = i + 1
    min_idx = i
    return {"a": a, "b": b, "swap": swap, "done": False}



