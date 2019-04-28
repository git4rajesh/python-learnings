if __name__ == '__main__':
    x = 2
    y = 2
    z = 2
    n = 3

lst_final = [[i, j, k] for i in range(x) for j in range(y) for k in range(z) if i + j + k != n]

print(lst_final)