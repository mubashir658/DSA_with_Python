# Title: Minimum Distance to the Target Element
# Submission ID: 1976971328
# Status: Accepted
# Date: April 13, 2026 at 10:38:12 AM GMT+5:30

class Solution {
    public int getMinDistance(int[] nums, int target, int start) {
        int n=nums.length;
        int min=Integer.MAX_VALUE;
        for(int i=0;i<n;i++){
            if(nums[i]==target){
                int minval=Math.abs(i-start);
                if(minval < min){
                    min=minval;
                }

            }
        }
        return min;
        

        
    }
}