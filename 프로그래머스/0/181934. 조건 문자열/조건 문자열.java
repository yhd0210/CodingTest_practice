class Solution {
    public int solution(String ineq, String eq, int n, int m) {
        int answer = 0;
        
        switch (ineq) {
            case ">":
                switch (eq) {
                    case "=":
                        if (n >= m) answer = 1;
                        else answer = 0;
                        break;
                    case "!":
                        if (n > m) answer = 1;
                        else answer = 0;
                        break;
                }
                break; // `>`에 대한 처리를 마친 후 switch 문 종료
                
            case "<":
                switch (eq) {
                    case "=":
                        if (n <= m) answer = 1;
                        else answer = 0;
                        break;
                    case "!":
                        if (n < m) answer = 1;
                        else answer = 0;
                        break;
                }
                break; 
        }
        return answer;
    }
}
