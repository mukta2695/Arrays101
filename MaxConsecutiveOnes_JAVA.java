class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max_count=0;
        int temp=0;
        for(int i=0;i<nums.length;i++ ){
            if(nums[i]==1){
                temp++;
            }
            else{
                max_count=Math.max(max_count,temp);
                temp=0;
            }
        }
        return Math.max(max_count,temp);
    }
}
public class MaxConsecutiveOnes {
	public static void main(String[] args) {
		Solution soln=new Solution();
		int nums[]= {1,0,1,1,0,1};
		System.out.println(soln.findMaxConsecutiveOnes(nums));
	}
	
