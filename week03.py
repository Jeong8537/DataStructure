def inters(l1 ,l2):
    s1 = set(l1)
    s2 = set(l2)

    return(s1 & s2)

l1 = [45, 5, 22, 31, 7, 19]
l2 = [2, 1, 5, 22, 31, 38, 7, 27, 19, 41]

print(inters(l1, l2))