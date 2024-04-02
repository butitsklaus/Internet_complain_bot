class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.flag = 0
        self.indices = []
        for i, i_val in enumerate(nums):
            for j, j_val in enumerate(nums):
                if i == j:
                    continue
                elif i_val + j_val == target:
                    self.indices.append(i)
                    self.indices.append(j)
                    self.flag = 1
                    break
            if self.flag == 1:
                break
        print(self.indices)

k = Solution()
k.twoSum(nums, target)