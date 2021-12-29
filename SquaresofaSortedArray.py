class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.nums=nums
        self.arr=[]
        for number in self.nums:
            self.arr.append(number**2)
        self.arr.sort()
        return self.arr
if __name__=="__main__":
    soln=Solution()
    nums = [-4, -1, 0, 3, 10]
    print(soln.sortedSquares(nums))
