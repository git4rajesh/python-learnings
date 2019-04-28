if __name__ == '__main__':
    lst_main = []
    lst_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst_temp = [name, score]
        lst_score.append(score)
        lst_main.append(lst_temp)

    lst_score.sort()
    min = lst_score[0]
    second_min = None
    index = 0

    while (index <= len(lst_score) - 1):
        if lst_score[index] == min:
            index += 1
        else:
            second_min = lst_score[index]
            break

    lst_name = []
    for student in lst_main:
        if student[1] == second_min:
            lst_name.append(student[0])

    lst_name.sort()
    for name in lst_name:
        print(name)
