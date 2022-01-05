class Solution(object):
    def calPosDups(self,index,possible_dups,arr):
        self.index=index
        self.possible_dups=possible_dups
        self.arr=arr
        for ind in range(self.index + 1):
            #self.index - self.possible_dups: --> to check the last index to be considered, rest will be discarded
            if ind > self.index - self.possible_dups:
                break
            elif self.arr[ind] == 0:
                if ind == self.index-self.possible_dups:
                    self.arr[self.index]=0 #Set last element as 0
                    self.index-=1
                    break
                self.possible_dups+=1
        return self.possible_dups, self.index, self.arr


    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        self.arr=arr
        self.possible_dups = 0
        self.left = 0
        self.index = len(self.arr) - 1
        self. possible_dups, self.index, self.arr=self.calPosDups(self.index,self.possible_dups,self.arr)

        #Start updating from last element
        self.last = self.index - self.possible_dups
        for ind in range(self.last, -1, -1):
            if self.arr[ind]==0:
                self.arr[ind+self.possible_dups]=0
                self.possible_dups-=1
                self.arr[ind+self.possible_dups]=0
            else:
                self.arr[ind+self.possible_dups]=self.arr[ind]

        print(self.arr)

if __name__=="__main__":
    arr=[1,0,2,3,0,4,5,0]
    arr1 = [1, 0, 2, 3, 0, 0, 5, 0]
    soln=Solution()
    soln2=Solution()
    soln.duplicateZeros(arr)
    soln2.duplicateZeros(arr1)
