def nb_year(p0, percent, aug, p):
    percentage = percent / 100
    i = 0
    while (p0 < p):
        p0 = p0 + p0 * percentage + aug
        i+= 1
    return i


print(nb_year(1500000, 0.25, 1000, 2000000))
