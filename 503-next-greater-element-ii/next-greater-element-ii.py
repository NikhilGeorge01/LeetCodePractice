class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = [-1]*n
        st = [0]
        for i in range(1,n):
            while st and nums[i] > nums[st[-1]]:
                a = st.pop()
                output[a] = nums[i]
            st.append(i)
        for i in range(0,n):
            while st and nums[i] > nums[st[-1]]:
                a = st.pop()
                output[a] = nums[i]
            st.append(i)
        return output

