class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD=1000000007
        prefsum=[0]
        prefnum=[0]
        cnt=[0]
        for i in range(len(s)):
            prefsum.append((prefsum[i]+int(s[i]))%MOD)
            if s[i]=='0':
                prefnum.append(prefnum[i])
                cnt.append(cnt[i])
            else:
                prefnum.append((prefnum[i]*10+int(s[i]))%MOD)
                cnt.append(cnt[i]+1)
        m=cnt[-1]
        pow10=[1]*(m+1)
        for i in range(1,m+1):
            pow10[i]=(pow10[i-1]*10)%MOD
        op=[]
        for l,r in queries:
            sm=(prefsum[r+1]-prefsum[l])%MOD
            left=cnt[l]
            right=cnt[r+1]
            if left==right:
                num=0
            else:
                num=(prefnum[r+1]-prefnum[l]*pow10[right-left])%MOD
            op.append((num*sm)%MOD)
        return op