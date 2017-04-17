def i(j):
    i=0
    y=0
    c=""
    l = []
    resto = "áéíóúÁÉÍÓÚñÑ"
    f = open("excepciones.txt","r").read().split()
    while i < len(j):
        for x in j[i]:
            if "a" <= x <= "z" or "A" <= x <= "Z" or x in resto: c += x
            else: c += " "
        i += 1
    a = c.split()
    while y < len(a):
        if not a[y] in f: l.append(a[y])
        else: pass
        if not a[y].upper() in f: l.append(a[y])
        else: pass
        y += 1
    return l
