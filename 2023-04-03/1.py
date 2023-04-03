def f(s):
    if s >= 21:
        return ['-', 0]
    moves = []
    moves.append(f(s + 1))
    moves.append(f(s * 2))
    win = []
    lose = []
    for move in moves:
        if move[0] == '-':
            win.append(move[1])
        else:
            lose.append(move[1])
    if win:
        return ['+', min(win) + 1]
    return ['-', max(lose)]

for s in range(1, 21):
    print(s, *f(s))