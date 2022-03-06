package other.pgs72410_신규아이디추천;

class Solution {
    public String solution(String new_id) {
        StringBuilder sb = new StringBuilder();

        // 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
        String lowerStr = new_id.toLowerCase();

        // 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
        for(int i = 0; i < lowerStr.length(); i++) {
            char ch = lowerStr.charAt(i);
            if(('a' <= ch && ch <= 'z') ||
                    ('0' <= ch && ch <= '9') ||
                    ch == '-' || ch == '_' || ch == '.') {
                sb.append(ch);
            }
        }

        // 3단계 new_id 에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
        String temp = "";
        for(int i = 0; i < sb.length(); i++) {
            if(i == 0) {
                temp += sb.charAt(i);
            }else {
                if(!(temp.charAt(temp.length() - 1) == '.' && sb.charAt(i) == '.')) {
                    temp += sb.charAt(i);
                }
            }
        }

        // 4단계 new_id 에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
        sb = new StringBuilder(temp);
        if(sb.length() != 0 && sb.charAt(0) == '.')
            sb.deleteCharAt(0);
        if(sb.length() != 0  && sb.charAt(sb.length() - 1) == '.')
            sb.deleteCharAt(sb.length() - 1);

        // 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
        if(sb.toString().equals(""))
            sb = new StringBuilder("a");

        // 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
        //        만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
        if(sb.length() >= 16) {
            sb = new StringBuilder(sb.substring(0, 15));
            if(sb.charAt(sb.length() - 1) == '.') {
                sb.deleteCharAt(sb.length() - 1);
            }
        }

        // 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
        if(sb.length() <= 2) {
            char ch = sb.charAt(sb.length() - 1);
            while(sb.length() != 3) {
                sb.append(ch);
            }
        }

        return sb.toString();
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        String new_id = "=.=";
        String ans = sol.solution(new_id);
        System.out.println(ans);
    }
}
