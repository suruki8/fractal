def compute_color(c, thrash = 4., max_iter = 50):
    z = 0 + 0j
    i = 0
    while (abs(z) < thrash) and (i < max_iter):
        z = z * z + c
        i += 1
        print(f"{i=}\t{z=}")
    if i < 50:
        return (0, 255 - 2 * i, 0)
    return (0, 0, 0)