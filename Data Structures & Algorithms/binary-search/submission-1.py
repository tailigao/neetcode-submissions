class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = len(nums)-1
        left = 0
        right = i
        k = (left + right) //2
        while left <= right:
            if nums[k] == target:
                return k
            elif nums[k] < target:
                left = k + 1
            elif nums[k] > target:
                right = k-1
            k = (left + right) // 2
            
        return -1
