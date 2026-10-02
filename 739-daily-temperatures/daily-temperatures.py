class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        output = [0] * n
        st = [0]
        for i in range(1,n):
            if temperatures[i] < temperatures[st[-1]]:
                st.append(i)
            else:
                while st and temperatures[i] > temperatures[st[-1]]:
                    a = st.pop()
                    output[a] = i - a
                st.append(i)
        return output

