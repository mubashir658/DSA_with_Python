# Title: Best Time to Buy and Sell Stock II
# Submission ID: 1945308426
# Status: Accepted
# Date: March 11, 2026 at 11:28:25 PM GMT+5:30

class Solution {
    public int maxProfit(int[] prices) {
        int profit=0;
        for(int i=1;i<prices.length;i++){
            if(prices[i]>prices[i-1]){
                profit+=prices[i]-prices[i-1];
            }
        }
        return profit;
        
    }
}