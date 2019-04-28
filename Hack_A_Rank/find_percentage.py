if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(student_marks)
    if query_name in student_marks:
        lst_scores = student_marks[query_name]
        avg = ("{0:.2f}".format(sum(lst_scores)/3))
        print(avg)
