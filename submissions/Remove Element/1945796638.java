# Title: Remove Element
# Submission ID: 1945796638
# Status: Accepted
# Date: March 12, 2026 at 01:16:41 PM GMT+5:30

class Solution {
    public int removeElement(int[] nums, int val) {
        int slow=0;
        for(int fast=0;fast<nums.length;fast++){
            if(nums[fast]!=val){
                nums[slow]=nums[fast];
                slow++;
            }
        }
        return slow;
        
    }
}