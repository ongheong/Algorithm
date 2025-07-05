def cantor(tmp):
    if tmp == 1:
        return "-"
    line = cantor(tmp // 3)
    return line + " "*(tmp // 3) + line

while True:
    try:
        N = input()
        N = int(N)
        print(cantor(3**N))
    except EOFError:
        break