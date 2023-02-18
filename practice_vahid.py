def q1():
    d = {}
    l = [5, 3, 4, 3, 5, 5, 3,1]

    for i in l:
        if (d.get(i) is not None):
            d[i] = d[i] + 1
        else:
            d[i] = 1
    for (key, value) in d.items():
        if (value == 1):
            print(key)
q1()


