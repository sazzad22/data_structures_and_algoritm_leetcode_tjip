# TC : O(N)
# SC : O(N)

class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record_dict = dict()
        for indx in range(len(nums)):
            curr_value = nums[indx]
            remaining = target - curr_value
            
            if remaining in record_dict:
                record_indx = record_dict[remaining]
                return [record_indx,indx]
            else:
                record_dict[curr_value] = indx
        