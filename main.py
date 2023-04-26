# selection sort


def selection_sort(numbers: list):
    n = len(numbers)


    for i in range(n - 1, 0, -1):
        max_idx = 0
        for j in range(1, i + 1):
            if numbers[j] > numbers[max_idx]:
                max_idx = j
        numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]


numbers = [5, 6, 1, 10, 4, 3, 11]
selection_sort(numbers)
print(numbers)



# binary search

def binary_search(text: list, target: str)-> str:
    low = 0
    high = len(text) -1
    while low <= high:
        mid = (low + high) // 2
        mid_value = text[mid]
        if mid_value == target:
            return mid
        elif target < mid_value:
            high = mid - 1
        else:
            low = mid + 1
    return None


text_a = ["This", "exercise", "is", "difficult"]
target_a = "exercise"

print(binary_search(text_a, target_a))

# hash Table


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def __my_hash(self, key):
        if isinstance(key, int):
            return key % self.size
        elif isinstance(key, str):
            return len(key) % self.size
        else:
            raise KeyError


    def put(self, key, data):
        index = self.__my_hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (k, data)
                return
            bucket.append(key, data)

ht = HashTable(6)
ht.put("tomato", 2)
ht.put("lettuce", 4)
ht.put("potato", 6)

print(ht.table)

def get(self, key):
    hash_key = self.__my_hash(key)
    bucket = self.table[hash_key]
    for item in bucket:
        if item[0] == key:
            return item[1]
    return None










