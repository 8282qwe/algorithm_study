n = int(input())

student_list = []

for _ in range(n):
    data = input().split()
    student_list.append((data[0],int(data[1])))

student_list.sort(key=lambda student: student[1])

print(student_list)