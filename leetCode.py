class Solution:
    def findShortestSubArray(self, nums):
        count = {}
        first_index = {}
        last_index = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
                first_index[num] = i
            last_index[num] = i

        degree = max(count.values())
        min_length = len(nums)

        for num in count:
            if count[num] == degree:
                length = last_index[num] - first_index[num] + 1
                if length < min_length:
                    min_length = length

        return min_length
