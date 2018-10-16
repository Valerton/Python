def rangmas(a,b):
    if a > b:
        a,b = b,a
    res = []
    bool = False
    for i in range(a,b):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            res.append(i)
    try:
        print(res[0])
    except IndexError:
        bool = True

    if bool == True:
        raise NoSimpleDigits

    return res
