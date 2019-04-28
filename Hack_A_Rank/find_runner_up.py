if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    max = arr[-1]
    last_index = len(arr) -1
    while(last_index >= 0):
        if arr[last_index] == max:
            last_index -=1
        else:
            print(arr[last_index])
            break