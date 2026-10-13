import timeit

def build_unique_list(data):
    unique = []
    for item in data:
        if item not in unique:
            unique.append(item)
    return unique

def build_unique_set(data):
    unique = set()
    for item in data:
        unique.add(item)
    return unique

sizes = [100, 1000, 10000]
repeats = 10

print(f"{'n':<7} | {'List in (с)':<12} | {'Set in (с)':<12} | {'Dict in (с)':<12} | {'Build List (с)':<15} | {'Build Set (с)':<14}")

list_times = []

for n in sizes:
    data = list(range(n))
    lst = list(data)
    st = set(data)
    dct = {i: i for i in data}
    target = n - 1 
    
    t_list = timeit.timeit(lambda: target in lst, number=repeats) / repeats
    t_set = timeit.timeit(lambda: target in st, number=repeats) / repeats
    t_dict = timeit.timeit(lambda: target in dct, number=repeats) / repeats
    
    t_build_list = timeit.timeit(lambda: build_unique_list(data), number=repeats) / repeats
    t_build_set = timeit.timeit(lambda: build_unique_set(data), number=repeats) / repeats
    
    list_times.append((n, t_list))
    
    print(f"{n:<7} | {t_list:<12.6f} | {t_set:<12.6f} | {t_dict:<12.6f} | {t_build_list:<15.6f} | {t_build_set:<14.6f}")

print("\nПсевдографіка залежності часу від n для пошуку в списку (List in):")
max_t = max(t for n, t in list_times)
for n, t in list_times:
    bar = "*" * max(1, int((t / max_t) * 40))
    print(f"n={n:<6} | {bar}")