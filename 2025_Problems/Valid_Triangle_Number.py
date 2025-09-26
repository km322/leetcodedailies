class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        total = 0
        for i in range(len(sorted_nums) - 2):
            k = i + 2
            for j in range(i + 1, len(sorted_nums) - 1 ):
                while k < len(sorted_nums) and sorted_nums[i] + sorted_nums[j] > sorted_nums[k]:
                    k += 1
                if sorted_nums[i] > 0 and sorted_nums[j] > 0:
                    total += k - j - 1
        return total
