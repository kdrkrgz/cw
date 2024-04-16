def binary_search(arr, item):
    if not arr:
        return False

    mid = len(arr) // 2

    if arr[mid] == item:
        return True
    elif arr[mid] < item:
        return binary_search(arr[mid+1:], item)
    else:
        return binary_search(arr[:mid], item)


arr = [11, 10, 8, 7, 6,    4, 2, 1, 0]
item = 11

if binary_search(arr, item):
    print(f"{item} arrde bulunuyor.")
else:
    print(f"{item} arrde bulunmuyor.")


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # arryi ikiye böler
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Her iki parçayı da sıralar
    left_sorted = merge_sort(sol_yarisi)
    right_sorted = merge_sort(sag_yarisi)

    # Sıralanmış parçaları birleştirir
    return merge(sol_sirali, sag_sirali)


def merge(left, right):
    sorted = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1

    sorted.extend(left[i:])
    sorted.extend(right[j:])

    return sorted


arr = [12, 3, 45, 7, 23, 1, 5]
print("Merge Sort : ", merge_sort(arr))

# 1. Iterasyon: [12] [3] --> [3, 12]
# 2. Iterasyon: [45] [7] --> [7, 45]
# 3. Iterasyon: [3, 12] [7, 45] --> [3, 7, 12, 45]
# 4. Iterasyon: [23] [1] --> [1, 23]
# 5. Iterasyon: [5] --> [5]
# 6. Iterasyon: [1, 23] [5] --> [1, 5, 23]
# 7. Iterasyon: [3, 7, 12, 45] [1, 5, 23] --> [1, 3, 5, 7, 12, 23, 45]
# Sıralı Liste: [1, 3, 5, 7, 12, 23, 45]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Orta itemı pivot olarak seç

    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)

arr = [12, 3, 45, 7, 23, 1, 5]

print("Quick Sort : ", quick_sort(arr))

# 1. Iterasyon: [3, 1, 5] (Pivot: 5) --> [3, 1] [5] []
# 2. Iterasyon: [3, 1] (Pivot: 3) --> [1] [3] []
# 3. Iterasyon: [12, 45, 23] (Pivot: 23) --> [12] [23] [45]
# 4. Iterasyon: [45] (Pivot: 45) --> [] [45] []
# Sıralı Liste: [1, 3, 5, 7, 12, 23, 45]

def max_sub_array(arr, n):
    max_sum = temp_sum = 0
    for i in range(n):
        max_sum += arr[i]
    temp_sum = max_sum
    print("Temp Sum : ", temp_sum)

    for i in range(n, len(arr)):
        temp_sum = temp_sum - arr[i-n] + arr[i]
        print("Temp Sum : ",i,  temp_sum)
        if temp_sum > max_sum:
            max_sum = temp_sum

    return max_sum


assert max_sub_array([-3,4,0,-2,6,-1], 2) == 5