import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        char[] ch = a.toCharArray();
        for(char c:ch){
            if(Character.isUpperCase(c)){
                c = Character.toLowerCase(c);
            }
            else{
                c = Character.toUpperCase(c);
            }
            System.out.print(c);
        }
    }
}

// Character.toUpperCase() : 대문자 변환
// Character.toLowerCase() : 소문자 변환
// Character.isUpperCase() : 대문자 구별