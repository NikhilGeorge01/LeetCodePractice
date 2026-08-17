class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n=len(stoneValue); prefix=[0]*(n+1)
        for i in range(n): prefix[i+1]=prefix[i]+stoneValue[i]

        @cache
        def dp(left,right):
            if left==right: return 0
            answer=leftSum=0; rightSum=prefix[right+1]-prefix[left]
            for split in range(left,right):
                leftSum+=stoneValue[split]; rightSum-=stoneValue[split]
                if leftSum<rightSum:
                    if answer>=2*leftSum: continue
                    answer=max(answer,leftSum+dp(left,split))
                elif leftSum>rightSum:
                    if answer>=2*rightSum: break
                    answer=max(answer,rightSum+dp(split+1,right))
                else:
                    answer=max(answer,leftSum+dp(left,split),rightSum+dp(split+1,right))
            return answer

        return dp(0,n-1)