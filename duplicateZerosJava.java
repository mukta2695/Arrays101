class Solution {	
    public void duplicateZeros(int[] arr) {
         
    	int possible_dups=0;
    	int index= arr.length-1;
    	
    	for(int i=0; i<index+1;i++) {
    		if (i > index-possible_dups){
    			break;
    		}
    		if(arr[i]==0) {
    			if(i==index-possible_dups) {
    				arr[index]=0;
    				index--;
    				break;
    			}
    			possible_dups++;
    		}
    	}
    	
    	int last=index-possible_dups;
    	for(int i=last;i>=0;i-- ) {
    		if(arr[i]==0) {
    			arr[i+possible_dups]=0;
    			possible_dups--;
    			arr[i+possible_dups]=0;
    		}
    		else {
    			arr[i+possible_dups]=arr[i];
    		}
    		}
        System.out.println(arr);
        
    	
    
    }
}
public class DupZero {
	public static void main(String[] args) {
		int arr[]= {1,0,2,3,0,4,5,0};
		new Solution().duplicateZeros(arr);
	}
}
