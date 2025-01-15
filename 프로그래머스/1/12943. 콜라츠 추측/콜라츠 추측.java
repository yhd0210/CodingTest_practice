class Solution {
    public int solution(int num) {
        int answer = 0;
        long number = num;
        if (number == 1) return 0;
        while (number != 1) {
            if (answer >= 500) return -1;
            if (number % 2 == 0) number /= 2;
            else number = number * 3 + 1;
            answer++;
        }
        return answer;
    }
}