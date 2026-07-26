class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # # product=1
        # nums=list(map(abs,nums))
        # nums.sort()
        # return nums[-1] * nums[-2] * nums[-3]

        # nums =[-100,-98,-1,2,3,4]
        # nums=[-1,-2,-3]
        # nums=list(map(abs,nums))
        nums.sort()
        # print(nums)
        # nums[-1] * nums[-2] * nums[-3]


        # # import numpy as np
        # left,right=0,len(nums)
        # while left < len(nums) and right >0:
        #     # print(left,right)
        #     # print(nums,nums[left],nums[right-1],left,right)
        #     if abs(nums[left])> abs(nums[right-1]):
        #         nums[left],nums[right-1]=nums[right-1],nums[left]
        #     else:
        #         right-=1
        #     if  right-1== left:
        #         left+=1
        #         right=len(nums)

        #     right-=1
        # return prod(nums[len(nums)-3:])

        return max(
    nums[-1] * nums[-2] * nums[-3],
    nums[0] * nums[1] * nums[-1]
)
        