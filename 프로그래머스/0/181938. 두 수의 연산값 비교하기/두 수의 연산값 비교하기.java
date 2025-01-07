class Solution {
    public int solution(int a, int b) {
        int answer = Integer.parseInt(""+a+b);
        int result = (answer >= (2*a*b))?answer:2*a*b;
        return result;
    }
}