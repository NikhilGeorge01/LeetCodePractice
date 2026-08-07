class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        k_factor_counts = {
            0: {}, 1: {}, 2: {2: 1}, 3: {3: 1}, 4: {2: 2}, 
            5: {5: 1}, 6: {2: 1, 3: 1}, 7: {7: 1}, 8: {2: 3}, 9: {3: 2}
        }
        def get_prime_count(n):
            count = {2: 0, 3: 0, 5: 0, 7: 0}
            for p in (2, 3, 5, 7):
                while n % p == 0:
                    count[p] += 1
                    n //= p
            return count, n == 1
        prime_count, is_divisible = get_prime_count(t)
        if not is_divisible:
            return "-1"
        def get_factor_count(count):
            res = {d: 0 for d in range(2, 10)}
            c2, c3, c5, c7 = count.get(2, 0), count.get(3, 0), count.get(5, 0), count.get(7, 0)
            res[8] = c2 // 3
            rem2 = c2 % 3
            res[9] = c3 // 2
            c3 %= 2
            res[4] = rem2 // 2
            c2 = rem2 % 2
            c6 = 0
            if c2 == 1 and c3 == 1:
                c2, c3, c6 = 0, 0, 1
            if c3 == 1 and res[4] == 1:
                c2, c6, c3, res[4] = 1, 1, 0, 0
            res[2], res[3], res[5], res[6], res[7] = c2, c3, c5, c6, c7
            return res
        def get_prime_count_from_string(s):
            count = {2: 0, 3: 0, 5: 0, 7: 0}
            for char in s:
                for p, freq in k_factor_counts[int(char)].items():
                    count[p] += freq
            return count
        def is_subset(a, b):
            return all(b.get(k, 0) >= v for k, v in a.items())
        def subtract(a, b):
            res = a.copy()
            for k, v in b.items():
                res[k] = max(0, res.get(k, 0) - v)
            return res
        def construct(count):
            return "".join(str(d) * count[d] for d in range(2, 10))
        factor_count = get_factor_count(prime_count)
        if sum(factor_count.values()) > len(num):
            ones = max(0, len(num) + 1 - sum(factor_count.values()))
            return "1" * ones + construct(factor_count)

        prime_count_prefix = get_prime_count_from_string(num)
        first_zero_index = num.find('0')
        if first_zero_index == -1:
            first_zero_index = len(num)
            if is_subset(prime_count, prime_count_prefix):
                return num
        for i in range(len(num) - 1, -1, -1):
            d = int(num[i])
            prime_count_prefix = subtract(prime_count_prefix, k_factor_counts[d])
            space_after = len(num) - 1 - i
            if i > first_zero_index:
                continue
            for bigger_digit in range(d + 1, 10):
                rem_req = subtract(prime_count, prime_count_prefix)
                rem_req = subtract(rem_req, k_factor_counts[bigger_digit])
                factors_after = get_factor_count(rem_req)
                if sum(factors_after.values()) <= space_after:
                    fill_ones = space_after - sum(factors_after.values())
                    return num[:i] + str(bigger_digit) + ("1" * fill_ones) + construct(factors_after)
        factors_after_extension = get_factor_count(prime_count)
        fill_ones = len(num) + 1 - sum(factors_after_extension.values())
        return "1" * max(0, fill_ones) + construct(factors_after_extension)