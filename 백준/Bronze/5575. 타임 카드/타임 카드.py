for _ in range(3):
    h1, m1, s1, h2, m2, s2 = map(int, input().split())
    n1 = (m1 * 60) + (h1 * 3600) + s1
    n2 = (m2 * 60) + (h2 * 3600) + s2
    t = n2 - n1
    h = t // 3600
    m = (t % 3600) // 60
    s = (t % 3600) % 60
    print("%d %d %d" %(h, m, s))