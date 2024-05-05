import timeit
import random

# Алгоритм сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Генерація тестових даних
test_data = [random.randint(0, 1000) for _ in range(10000)]

# Вимірювання часу для сортування злиттям
merge_time = timeit.timeit("merge_sort(test_data[:])", globals=globals(), number=10)

# Вимірювання часу для сортування вставками
insertion_time = timeit.timeit("insertion_sort(test_data[:])", globals=globals(), number=10)

# Вимірювання часу для Timsort (вбудований алгоритм)
timsort_time = timeit.timeit("sorted(test_data[:])", globals=globals(), number=10)

print(f"Час сортування злиттям: {merge_time:.5f} секунд")
print(f"Час сортування вставками: {insertion_time:.5f} секунд")
print(f"Час Timsort: {timsort_time:.5f} секунд")


# За результатами експерименту можна очікувати, що Timsort буде показувати кращі результати 
# на різноманітних даних порівняно з чистими алгоритмами сортування злиттям або вставками, особливо на великих масивах або масивах з частково впорядкованими
