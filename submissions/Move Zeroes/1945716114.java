# Title: Move Zeroes
# Submission ID: 1945716114
# Status: Accepted
# Date: March 12, 2026 at 11:34:47 AM GMT+5:30

class Solution {
    public void moveZeroes(int[] nums) {

        int left=0;
        for(int right=0;right<nums.length;right++){
            if(nums[right]!=0){
                int temp=nums[left];
                nums[left]=nums[right];
                nums[right]=temp;
                left++;
                
            }
        }
        
    }
}