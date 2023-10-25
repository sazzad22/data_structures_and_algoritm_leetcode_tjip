# TC : O(N2)
# TC : O(N)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # the idea is for finding my desired triplets
        # i go to every element as prefix ,make it's negative as the target
        # apply sorted two sum on the element on the right (suffix)
        # within this we handle to prevent dupicate results
        res_triplets = []
        nums.sort()

        for i in range(len(nums)):

            # skip duplicate on the outer loop too
            # if ((i+1) < len(nums)) and (nums[i] == nums[i-1]):
            #     # i+=1
            #     continue
            
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            a = nums[i]
            target = -a
            # applying sorted two sum
            # define pointers
            L = i + 1
            R = len(nums) - 1
            while(L<R):

                if((nums[L] + nums[R]) < target):
                    L+=1
                elif((nums[L] + nums[R]) > target):
                    R-=1
                else:
                    b = nums[L]
                    c = nums[R]
                    while((L < R) and (b == nums[L+1])):
                        L+=1
                    while((R > L) and (c == nums[R-1])):
                        R-=1
                    
                    res_triplets.append([a,b,c])
                    # change both of the position of L and R
                    L+=1
                    R-=1

            
                
        return res_triplets





