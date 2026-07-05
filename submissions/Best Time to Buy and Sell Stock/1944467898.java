# Title: Best Time to Buy and Sell Stock
# Submission ID: 1944467898
# Status: Time Limit Exceeded
# Date: March 11, 2026 at 07:02:53 AM GMT+5:30

class Solution {
    public int maxProfit(int[] prices) {
        int maxDiff=0;
        int currentMax=0;
        for(int i=0;i<prices.length;i++){
            for(int j=i+1;j<prices.length;j++){
                int Diff=prices[j]-prices[i];
                currentMax=Math.max(currentMax,Diff);
            }
            maxDiff=Math.max(maxDiff,currentMax);

        }
        return maxDiff;
        
    }
}