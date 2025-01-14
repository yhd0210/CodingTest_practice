class Solution {
    public int solution(String str1, String str2) {
        return isSubstring(str1, str2) ? 1 : 0;
    }
    public static boolean isSubstring(String str1, String str2) {
        for (int i = 0; i <= str2.length() - str1.length(); i++) {
            if (str2.substring(i, i + str1.length()).equals(str1)) {
                return true;
            }
        }
        return false; 
    }
}

// 7 - 3
// 0000000