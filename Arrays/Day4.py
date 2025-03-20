def rotate(arr, d):
    n = len(arr)
    temp = [0]*n
    first = d % n
    for i in range(n):
        start = first % n
        temp[i] = arr[start]
        first+=1
    return temp

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    d = 6
    print(rotate(arr, d))