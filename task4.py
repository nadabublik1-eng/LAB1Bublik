# Вхідні дані задані як параметри на початку скрипта для відтворюваності
collection1 = [101, 102, 102, 103, 104, 105, 105]
collection2 = [104, 105, 106, 107, 107, 108]
collection3 = [101, 102]

set1 = set(collection1)
set2 = set(collection2)
set3 = set(collection3)

print("--- Унікальні значення (відсортовано) ---")
print(f"Множина 1 (з collection1): {sorted(set1)}")
print(f"Множина 2 (з collection2): {sorted(set2)}")
print(f"Множина 3 (з collection3): {sorted(set3)}\n")

print("--- Операції над наборами (set1 та set2) ---")
print(f"Перетин: {sorted(set1 & set2)}")
print(f"Об'єднання: {sorted(set1 | set2)}")
print(f"Симетрична різниця: {sorted(set1 ^ set2)}\n")

print("--- Перевірка підмножини ---")
# Один приклад істинного твердження та один хибного
print(f"Чи є Множина 3 підмножиною Множини 1? {set3 <= set1}")
print(f"Чи є Множина 2 підмножиною Множини 1? {set2 <= set1}\n")

print("--- Використання frozenset ---")
# Демонстрація frozenset як ключа у словнику
access_rules = {
    frozenset(['admin', 'editor']): "Повний доступ до редагування",
    frozenset(['guest']): "Доступ лише для читання"
}
user_roles = frozenset(['admin', 'editor'])
print(f"Права для комбінації ролей {list(user_roles)}: {access_rules.get(user_roles)}")