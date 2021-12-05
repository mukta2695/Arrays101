class Solution {
    public int findNumbers(int[] nums) {
        int count=0;
        for(int i=0;i<nums.length;i++){
            String num_str=Integer.toString(nums[i]);
            if(num_str.length()%2==0){
                count++;
            }
        }
        return count;
    }
     
}
public class FindNumberCountWithEvenDigitsCount{
	public static void main(String[] args) {
		int soln=new Solution();
		int nums[]= {123,2654,30,6,364656}
		System.out.println(soln.findNumbers(nums))
	}
}
