
# Reverse an Array
def reversearray(arr):
    end = len(arr)-1
    for i in range(len(arr)//2):
        arr[i], arr[end] = arr[end], arr[i]
        end -=1
    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    print(reversearray(arr))