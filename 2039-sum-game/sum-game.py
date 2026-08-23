class Solution:
    def sumGame(self, num: str) -> bool:
        f = 0
        l = 0
        qf = 0
        ql = 0
        for i in range(len(num)):
            if i < len(num)//2:
                if num[i] == '?':
                    qf += 1
                else:
                    f +=  int(num[i])
            else:
                if num[i] == '?':
                    ql += 1
                else:
                    l +=  int(num[i])
        if (qf + ql) % 2 == 1:
            return True
        else:
            return not ((f - l)  == (((ql - qf)//2) * 9))

