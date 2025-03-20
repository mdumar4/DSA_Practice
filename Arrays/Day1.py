
# Find Second largest element in an array
def second_largest(arr):
    first = second = -1
    for i in range(len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] < first:
            second = arr[i]
    return second

# smallest and second smallest
def second_smallest(arr):
    first = second = arr[0]
    for i in range(len(arr)):
        if arr[i] < first:
            second = first
            first = arr[i]
        elif arr[i] < second and arr[i] > first:
            second = arr[i]
    return second


if __name__ == "__main__":
    arr = [34, 35, 1, 10, 12, 1]
    print(f"Second Largest element is {second_largest(arr)}")
    print(f"Second smallest element is {second_smallest(arr)}")
