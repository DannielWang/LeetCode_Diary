class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        maxnum = -1
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    if maxnum < nums[j] - nums[i]:
                        maxnum = nums[j] - nums[i]
        if maxnum == -1:
            return -1
        if maxnum != -1:
            return maxnum