import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] solution(int[] arr, int divisor) {
         ArrayList<Integer> list = new ArrayList<>();
        
        for (int num : arr) {
            if (num % divisor == 0) {
                list.add(num);
            }
        }
        if (list.isEmpty()) {
            list.add(-1);
        } else {
            Collections.sort(list);
        }

        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
}