class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        st = []
        lg = [-1]*len(nums2)
        for i in range(len(nums2)):
            if not st:
                st.append((nums2[i],i))
            elif nums2[i] < st[-1][0]:
                st.append((nums2[i], i))
            else:
                while st and st[-1][0] < nums2[i]:
                    a1,a2 = st.pop()
                    lg[a2] = nums2[i]
                st.append((nums2[i], i))
        op = []
        dic = {}
        for i in range(len(nums2)):
            dic[nums2[i]] = lg[i]

        return [dic[x] for x in nums1]

            
            