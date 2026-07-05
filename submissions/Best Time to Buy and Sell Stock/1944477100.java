# Title: Best Time to Buy and Sell Stock
# Submission ID: 1944477100
# Status: Wrong Answer
# Date: March 11, 2026 at 07:23:11 AM GMT+5:30

class Solution {
    public int maxProfit(int[] prices) {
      
        int cheap=prices[0];
        int profit=Integer.MIN_VALUE;
        for(int i=1;i<prices.length;i++){
            cheap=Math.min(cheap,prices[i]);
            profit=Math.max(profit,prices[i]-cheap);
            

        }
        return profit;
        
    }
}