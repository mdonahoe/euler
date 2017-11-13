def twoxmody(x, y):
    s = 1
    while x:
            s = (s * 2) % y
            x -= 1
    return s

print (28433 * twoxmody(7830457, 10**10) + 1) % 10**10
