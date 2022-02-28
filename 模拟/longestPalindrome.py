s = "accddada"
ss = ""
ans = []
r = s[::-1]
maxnum = 1
res = 1
n = len(s)
dp = [[False] * n for _ in range(n)]
print(dp)
if len(r) == 1:
    print(r)
if len(r) == 0:
    print([])
else:
    for i in range(len(r) - 1):
        if r[i] + r[i + 1] in s:
            ss = r[i] + r[i + 1]
            num = i + 2
            while True:
                if num < len(r):
                    ss = ss + r[num]
                    if ss in s:
                        num += 1
                    else:
                        ss = ss[:-1]
                        ans.append(ss)
                        break
                else:
                    break
        else:
            if i + 1 ==len(r) - 1:
                print(r[i])
    for i, num in enumerate(ans):
        if len(num) > maxnum:
            maxnum = len(num)
            res = i
    print(ans[res])

