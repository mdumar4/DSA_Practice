 # Move all zeros to the end of the array

def move_zeros(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1
    return arr

if __name__ == "__main__":
    arr = [1, 0, 2, 0, 3, 0, 4, 5, 6, 7]
    print(f"Array after moving zeros to the end is {move_zeros(arr)}")
