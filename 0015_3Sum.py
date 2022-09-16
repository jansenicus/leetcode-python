class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Naive
        LeetCode status: Time Limit Exceeded
        """
        ispace = [i for i in range(len(nums))]
        triplets = []
        
        for i in ispace:
            for j in ispace:
                for k in ispace:
                    if i != j and i != k and j !=k:
                        if nums[i] + nums[j] + nums[k] == 0:
                            triad = sorted([ nums[i], nums[j], nums[k] ])
                            if triad not in triplets:
                                triplets.append( triad)
                                
                
        return triplets
        
