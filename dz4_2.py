import heapq

def merge_k_lists(lists):
    if not lists:
        return []

    # Ініціалізуємо мінімальну купу
    min_heap = []
    # Вставляємо перший елемент кожного списку разом з індексом списку та індексом елементу в списку
    for i in range(len(lists)):
        if lists[i]:  # перевірка чи список не порожній
            heapq.heappush(min_heap, (lists[i][0], i, 0))

    merged_list = []
    # Поки в купі є елементи
    while min_heap:
        # Вибираємо мінімальний елемент
        val, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(val)
        # Додаємо наступний елемент з того ж списку в купу, якщо він існує
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)

    return merged_list

# Тестування функції
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)

