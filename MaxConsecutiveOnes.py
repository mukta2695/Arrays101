# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums=nums
        max_count=0
        temp=0
        for index in range(len(nums)):
            if nums[index]==1:
                temp+=1
            else:
                max_count=max(max_count,temp)
                temp=0
            #if max<temp:
                #max=temp
        return max(max_count,temp)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    soln=Solution()
    result=soln.findMaxConsecutiveOnes([1,0,1,1,0,1])
    print(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
