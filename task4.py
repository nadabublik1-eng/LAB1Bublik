collection1 = [101, 102, 102, 103, 104, 105, 105]
collection2 = [104, 105, 106, 107, 107, 108]
collection3 = [101, 102]

set1 = set(collection1)
set2 = set(collection2)
set3 = set(collection3)

print("Множина 1:", sorted(set1))
print("Множина 2:", sorted(set2))
print("Множина 3:", sorted(set3))

print("Перетин set1 та set2:", sorted(set1 & set2))
print("Об'єднання set1 та set2:", sorted(set1 | set2))
print("Симетрична різниця set1 та set2:", sorted(set1 ^ set2))

print("Чи є set3 підмножиною set1:", set3 <= set1)
print("Чи є set2 підмножиною set1:", set2 <= set1)

access_rules = {
    frozenset(['admin', 'editor']): "Повний доступ",
    frozenset(['guest']): "Читання"
}
user_roles = frozenset(['admin', 'editor'])
print("Права доступу за frozenset ключем:", access_rules.get(user_roles))