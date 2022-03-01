s = "+-12"
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbol = ["-", "+"]
flag = 0
minu = 0
ans = 0
for i in s:
    if i == "-":
        if flag == 0:
            flag = 1
            minu = 1
            continue
        else:
            break
    if i in numbers:
        ans = ans * 10 + int(i)
    if 2 ** 31 <= ans:
        break
    if i not in numbers and i not in symbol and i != " ":
        break
if minu == 1:
    if 2 ** 31 <= ans:
        # return -2**31
        print(-2**31)
    # return -ans
    print(-ans)
if 2 ** 31 <= ans:
    # return 2**31 + 1
    print(2**31 + 1)
# return ans
print(ans)
