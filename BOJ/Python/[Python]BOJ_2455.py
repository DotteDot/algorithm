x = 0
people = 0
for _ in range(4):
    a, b = map(int, input().split())
    people = people + b - a
    x = max(people, x)
print(x)