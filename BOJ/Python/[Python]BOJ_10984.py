for _ in range(int(input())):
    a, b = 0, 0.0
    for _ in range(int(input())):
        aa, bb = input().split()
        a += int(aa)
        b += (float(bb)*int(aa))
    print(a, '{:.1f}'.format(b/a))