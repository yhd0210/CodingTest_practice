class Solution {
    public long solution(long n) {
        long num = (int) Math.pow((double)n, 0.5);
        if (num*num == n){
            return (num+1)*((num+1));
        } else {
            return -1;
        }
    }
}