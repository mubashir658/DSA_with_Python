# Title: Maximum Subarray
# Submission ID: 1943502643
# Status: Accepted
# Date: March 10, 2026 at 09:47:33 AM GMT+5:30

class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum=nums[0];
        int currentSum=nums[0];
        for(int i=1;i<nums.length;i++){
            currentSum=Math.max(nums[i],currentSum+nums[i]);
            maxSum=Math.max(maxSum,currentSum);   
        }
        return maxSum;
        

        
    }
}