# Title: Squares of a Sorted Array
# Submission ID: 1945873212
# Status: Accepted
# Date: March 12, 2026 at 02:57:15 PM GMT+5:30


class Solution {
    public int[] sortedSquares(int[] nums) {
        
        
        int left=0;

        int right=nums.length-1;
        int[] res=new int[nums.length];
        int pos=right;

       while(left<=right){
        if(Math.abs(nums[left])>Math.abs(nums[right])){
            res[pos]=nums[left]*nums[left];
            left++;
        }else{
            res[pos]=nums[right]*nums[right];
            right--;
        }
        pos--;

       }
       return res;
    }
}