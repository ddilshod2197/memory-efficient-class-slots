import time
import random
import string

class MemoryEfficientClass:
    __slots__ = ('id', 'name', 'age')

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Age: {self.age}'

class MemoryInefficientClass:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Age: {self.age}'

def generate_random_data(num_objects):
    data = []
    for _ in range(num_objects):
        id = random.randint(1, 1000)
        name = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        age = random.randint(1, 100)
        data.append((id, name, age))
    return data

def benchmark(num_objects):
    start_time = time.time()
    memory_efficient_objects = [MemoryEfficientClass(*data) for data in generate_random_data(num_objects)]
    end_time = time.time()
    print(f'Memory efficient class: {end_time - start_time} seconds')

    start_time = time.time()
    memory_inefficient_objects = [MemoryInefficientClass(*data) for data in generate_random_data(num_objects)]
    end_time = time.time()
    print(f'Memory inefficient class: {end_time - start_time} seconds')

benchmark(100000)
```

Kodda ikkita klass mavjud: `MemoryEfficientClass` va `MemoryInefficientClass`. `MemoryEfficientClass` klassi `__slots__` yordamida memory-efficient bo'lish uchun yaratilgan. `__slots__` atribut klassga ma'lumotlar saqlash uchun foydalaniladigan joylarni belgilaydi. Bu klassda ma'lumotlar `id`, `name` va `age` atributlarida saqlanadi.

`MemoryInefficientClass` klassi esa `__slots__` atributi yo'q, shuning uchun u memory-inefficient bo'ladi.

`benchmark` funksiyasi ikkita klass uchun random ma'lumotlarni yaratib, ularni yaratish vaqtini hisoblaydi.
