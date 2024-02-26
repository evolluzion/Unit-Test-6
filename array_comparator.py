class ArrayComparator:
    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2

    def compute_average(self, array):
        if len(array) == 0:
            return 0
        return sum(array) / len(array)

    def compare_arrays(self):
        avg_array1 = self.compute_average(self.array1)
        avg_array2 = self.compute_average(self.array2)

        if avg_array1 > avg_array2:
            return "Первый список имеет большее среднее значение"
        elif avg_array1 < avg_array2:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"

# Задаем массивы
array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array2 = [1, 2, 3, 4, 5]

comparator = ArrayComparator(array1, array2)
result = comparator.compare_arrays()
print(result)
