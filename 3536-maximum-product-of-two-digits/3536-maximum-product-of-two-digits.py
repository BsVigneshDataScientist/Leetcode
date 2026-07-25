class Solution:
    def maxProduct(self, n: int) -> int:

        # product=1
        # for num in str(n):
        #     product*=int(num)
        # return product           
        temp_list=list(map(int,str(n)))
        temp_list.sort(reverse=True)
        # print(temp_list)
        return temp_list[0]*temp_list[1]
        