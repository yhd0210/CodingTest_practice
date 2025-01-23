import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] solution(int[] arr, int divisor) {
         ArrayList<Integer> tempList = new ArrayList<>();
        for (int num : arr) {
            if (num % divisor == 0) {
                tempList.add(num);
            }
        }
        if (tempList.isEmpty()) {
            tempList.add(-1);
        } else {
            Collections.sort(tempList);
        }

        int[] answer = new int[tempList.size()];
        for (int i = 0; i < tempList.size(); i++) {
            answer[i] = tempList.get(i);
        }

        return answer;
    }
}