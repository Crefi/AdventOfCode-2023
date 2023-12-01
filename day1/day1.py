with open("day1.in") as f:
    data = f.read()

ans = 0

for line in data.strip().split():
    first = None
    last = None
    for c in line:
        if c.isdigit() and first == None:
            first = c
        if c.isdigit():
            last = c


    num = int(first + last)
    ans += num

print(ans)