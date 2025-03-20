
# Rotate an Array by d - Counterclockwise or Left Rotation
# def rotate(arr, d):
#     n = len(arr)
#     temp = [0]*n
#     first = d % n
#     for i in range(n):
#         start = first % n
#         temp[i] = arr[start]
#         first+=1
#     return temp

def rotate(arr, d):
    n = len(arr)
    d = d % n
    reverse(arr, 0, d-1)
    reverse(arr, d, n-1)
    reverse(arr, 0, n-1)
    return arr

def reverse(arr, start, end):
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start +=1
        end -=1

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    d = 1
    print(rotate(arr, d))