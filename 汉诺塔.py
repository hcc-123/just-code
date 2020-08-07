count = 0

def hanoi(n, a, b, c):
    global count
    if n > 0:
        hanoi(n - 1, a, c, b)
        print("%s --> %s" % (a, c))
        hanoi(n - 1, b, a, c)
        count += 1

hanoi(6, 'X', 'Y', 'Z')
print(count)