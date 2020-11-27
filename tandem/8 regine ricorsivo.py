def is_safe(queens, row, col):
    # ritorna true se la posizione (row, col) e' sicura, dato un array con le colonne delle regine
    #controlla le diagonali
    # si può fare come in un piano cartesiano, trovando dy/dx e verificando che m != +/- 1
    for _row, _col in enumerate(queens):
        if row != _row:
            dy = col - _col
            dx = row - _row
            if abs(dy/dx) == 1:
                return False 

    return True

def is_valid(queens):
    for row,col in enumerate(queens):
        if not is_safe(queens, row, col):
            return False
    return True

def main(n):
    queens = []
    count = 1
    for q1 in [i for i in range(n)]:
        queens.append(q1)
        for q2 in [i for i in range(n) if i not in queens]:
            queens.append(q2)
            for q3 in [i for i in range(n) if i not in queens]:
                queens.append(q3)
                for q4 in [i for i in range(n) if i not in queens]:
                    queens.append(q4)
                    for q5 in [i for i in range(n) if i not in queens]:
                        queens.append(q5)
                        for q6 in [i for i in range(n) if i not in queens]:
                            queens.append(q6)
                            for q7 in [i for i in range(n) if i not in queens]:
                                queens.append(q7)
                                for q8 in [i for i in range(n) if i not in queens]:
                                    queens.append(q8)
                                    if is_valid(queens):
                                        print(count, ":", queens)
                                        count += 1
                                    queens.pop()
                                queens.pop()
                            queens.pop()
                        queens.pop()
                    queens.pop()
                queens.pop()
            queens.pop()
        queens.pop()

if __name__ == "__main__":
    main(8)