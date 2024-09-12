def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


size = int(input('\nВведите количество чисел для сортировки: '))
numbers = []
for _ in range(size):
    num = float(input('Введите число: '))
    numbers.append(num)

sorted_arr = sort(numbers)
print('\nОтсортированыЙ массив:\n', ',  '.join(map(str, sorted_arr)))
