import java.util.Arrays;

class Solution {
    public int[] sortedSquares(int[] nums) {
    	int size=nums.length;
        int temp[]=new int[size];
        for(int i=0; i<size; i++) {
        	temp[i]=nums[i]*nums[i];

        	
        }
        Arrays.sort(temp);
        return temp;
    }
}
public class SquaresOfASortedArray {
	public static void main(String[] args) {
		Solution soln=new Solution();
		int nums[] = {-4,-1,0,3,10};
		System.out.println(soln.sortedSquares(nums));
	}
}
