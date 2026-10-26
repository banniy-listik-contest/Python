N = 365

left, right = 0, 1000
count = 0
while (ans := (left + right) / 2) != N:
    if ans > N:
        right = ans
    else:
        left = ans
    count += 1

print(ans, count)