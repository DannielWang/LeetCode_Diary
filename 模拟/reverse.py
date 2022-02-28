class Solution:
    def reverse(self, x: int) -> int:
        minu = 0
        flag = 0
        if x < 0:
            flag = 1
            x = abs(x)
        while x != 0:
            minu = int(minu * 10) + int(x % 10)
            x = int(x / 10)
        if flag == 1:
            minu = -minu
        if (-2)**31 <= minu <= 2**31 - 1:
            return minu
        return 0