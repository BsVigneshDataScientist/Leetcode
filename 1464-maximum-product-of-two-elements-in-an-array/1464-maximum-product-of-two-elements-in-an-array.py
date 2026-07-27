class Solution:
    def maxProduct(self, nums: List[int]) -> int:
            # nums.sort()
            # return max((nums[-1]-1*nums[-2]-1),(nums[0]*nums[1]))
            # nums = [3,7]
            nums.sort()
            # print(nums)
            # print(nums[-1]-1)
            # print(nums[-2]-1)
            return max(((nums[-1]-1) * (nums[-2]-1)),(nums[0]-1) * (nums[1]-1))

        