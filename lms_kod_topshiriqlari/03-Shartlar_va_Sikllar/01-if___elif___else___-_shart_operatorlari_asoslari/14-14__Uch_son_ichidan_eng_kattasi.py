parts = input().split()
a = int(parts[0])
b = int(parts[1])
c = int(parts[2])
m = a
if b > m:
    m = b
if c > m:
    m = c
print(m)