# Title: Remove Duplicates from Sorted Array
# Submission ID: 1945779053
# Status: Accepted
# Date: March 12, 2026 at 12:49:46 PM GMT+5:30

class Solution {
    public int removeDuplicates(int[] nums) {
        
        int k=1;
        for(int i=1;i<nums.length;i++){
            if(nums[i]!=nums[i-1]){
                nums[k]=nums[i];
                k++;
            }

        }
        return k;
        
    }
}