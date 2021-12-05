class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums=nums
        count=0
        for number in nums:
            length=len(str(number))
            if length%2 ==0 :
                count+=1
        return count

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    soln=Solution()
    print(soln.findNumbers([555,901,4832,1771]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
