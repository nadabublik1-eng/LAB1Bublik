def print_student(student):
    name, group, grades = student
    print(f"Студент: {name}, Група: {group}, Оцінки: {grades}")

def calculate_avg(students_list):
    total = sum(sum(s[2]) for s in students_list)
    count = sum(len(s[2]) for s in students_list)
    return round(total / count, 2)

students = [
    ("Григорієвська", "БІКСб-2-25-40д", [90, 85, 95]),
    ("Ярчук", "БІКСб-2-25-40д", [75, 80, 70]),
    ("Лусникова", "БІКСб-2-25-40д", [100, 95, 98])
]

for s in students:
    print_student(s)

print("Середній бал усіх студентів:", calculate_avg(students))

try:
    students[0][0] = "Коваленко"
except TypeError as e:
    print("Заборонено змінювати елементи кортежу:", e)

students[0][2].append(100)
print("Після зміни вкладеного мутабельного списку:", students[0])