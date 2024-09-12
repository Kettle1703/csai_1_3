def sort(arr, ascending=True):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if (ascending and arr[j] > arr[j+1]) or (not ascending and arr[j] < arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


size = int(input('\nВведите количество чисел для сортировки: '))
numbers = []
for _ in range(size):
    num = float(input('Введите число: '))
    numbers.append(num)

order = input('Введите "возрастание" или "убывание" ').strip().lower()
increasing = order == 'возрастание'
sorted_arr = sort(numbers, increasing)
print('\nОтсортированный массив:\n', ',  '.join(map(str, sorted_arr)))
