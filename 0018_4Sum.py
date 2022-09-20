class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        Q = []                                                  # Quadruplets placeholder
        nums.sort()                                             # sort first the array
        n = len(nums)                                           # the length of the array

        for i in range(n - 3):                                  # last index on len(nums)-3

            if i > 0 and nums[i] == nums[i - 1]:                # skip if current number equals previous number
                continue

            for j in range(i + 1, n - 2):                       # next number loop begins with i+1 to len(nums)-2

                l, r = j + 1, n - 1                             # two pointers l and r, begins with j+1 to len(nums)-1

                while l < r:                                    # while l < r then keep looping

                    q = (nums[i], nums[j],
                         nums[l], nums[r])                      # quadruplet

                    qsum = sum(q)                               # Sum of quadruplet

                    if qsum < target:                           # if qsum < target -> increase the `l` index
                        l += 1

                    elif qsum > target:                         # if qsum > target -> decrease the `r` index
                        r -= 1

                    else:
                        Q.append(q)                             # add quadruplet into Quadruplets
                        l += 1                                  # increase the `l` index

                        while nums[l] == nums[l-1] and l<r:     # keep skipping if current number equals previous number
                            l += 1                              # increase `l` index

        return list(set(Q))                                     # unique set of Quadruplets
