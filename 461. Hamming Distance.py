class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xbin = format(x, 'b').zfill(32)
        ybin = format(y, 'b').zfill(32)
        return len(list(filter(lambda xy: xy[0] != xy[1], zip(xbin, ybin))))


# Runtime: 24 ms, faster than 95.74% of Python3 online submissions for Hamming Distance.
# Memory Usage: 14.4 MB, less than 12.59% of Python3 online submissions for Hamming Distance.