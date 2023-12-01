with open("day1.in") as f:
    data = f.read()

ans = 0
nums = ["one","two","three","four","five","six","seven","eight","nine"]

for line in data.strip().split():
    first = None
    last = None
    for i in range(len(line)):
        curr = None
        c = line[i]
        if c.isdigit():
            curr = int(c)

        for j , num in enumerate(nums):
            if line[i:(i+len(num))] == num:
                curr = j + 1
                break

        if curr:
            if first == None:
                first = curr
            last = curr
    ans += first * 10 + last


print(ans)