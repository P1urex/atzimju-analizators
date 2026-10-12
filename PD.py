name = input("Ievadi skolēna vārdu: ")
n = int(input("Ievadi atzīmju skaitu: "))

grades = []

for i in range(n):
    grade = input("Ievadi atzīmi no 1 līdz 10: ")

    if grade.isalpha():
        print("Kļūda! Atzīmei jābūt skaitlim no 1 līdz 10!")
        grade = input("Ievadi atzīmi vēlreiz: ")

    grade = int(grade)

    while grade < 1 or grade > 10:
        print("Kļūda! Atzīmei jābūt no 1 līdz 10!")
        grade = int(input("Ievadi atzīmi vēlreiz: "))

    grades.append(grade)

average = sum(grades) / n
highest = max(grades)
lowest = min(grades)

print("Skolēns:", name)
print("Vidējā atzīme:", round(average, 2))
print("Augstākā atzīme:", highest)
print("Zemākā atzīme:", lowest)