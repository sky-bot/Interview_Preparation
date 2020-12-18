class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = 1000000000000000
        second = 1000000000000000
        third = 1000000000000000

        top = 0
        for i in range(0, len(nums)):


            if nums[i] <= first:
                first = nums[i]
                secod = third = 1000000000000000
            elif nums[i] <= second:
                second = nums[i]
                third = 1000000000000000
            elif nums[i] < third:
                third = nums[i]
                print(first, second, third)
                return True

        return False
        