class Solution:

    def msbPos(self, n):

        msb_p = -1
        while (n > 0):
            n = n >> 1
            msb_p += 1

        return msb_p

    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        res = 0  # Initialize result

        while (m > 0 and n > 0):

            # Find positions of MSB in m and n
            msb_p1 = self.msbPos(m)
            msb_p2 = self.msbPos(n)

            # If positions are not same, return
            if (msb_p1 != msb_p2):
                break

            # Add 2^msb_p1 to result
            msb_val = (1 << msb_p1)
            res = res + msb_val

            # subtract 2^msb_p1 from m and n.
            m = m - msb_val
            n = n - msb_val

        return res


s = Solution();
print(s.rangeBitwiseAnd(5, 7))
