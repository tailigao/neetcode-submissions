class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in seen:
                result.append(seen[complement])
                result.append(i)
            
            seen[nums[i]] = i

        return result





