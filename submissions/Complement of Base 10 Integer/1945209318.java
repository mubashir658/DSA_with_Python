# Title: Complement of Base 10 Integer
# Submission ID: 1945209318
# Status: Wrong Answer
# Date: March 11, 2026 at 10:05:17 PM GMT+5:30

class Solution {
    public int bitwiseComplement(int n) {
        int temp=n;
        int i=0;
        while(temp>0){
            n=n^(1<<i);
            temp=temp>>1;
            i++;
        }
        return n;
        
    }
}