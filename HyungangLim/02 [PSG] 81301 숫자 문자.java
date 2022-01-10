package programmers.pg81301;

import java.util.HashMap;
import java.util.Map;

/**
 *
 * s길이 50이하, 숫자 20억 이하(10자리)
 * 브루트 포스 가능
 *
 * key, value 이용.
 * key 간 포함관계 형성되지 않으므로 그냥 쭉 세면서 만들어도 된다.
 *
 */

class Solution {
    public int solution(String s) {
        int answer = 0;

        Map<String, String> map = new HashMap<>();
        map.put("zero", "0");
        map.put("one", "1");
        map.put("two", "2");
        map.put("three", "3");
        map.put("four", "4");
        map.put("five", "5");
        map.put("six", "6");
        map.put("seven", "7");
        map.put("eight", "8");
        map.put("nine", "9");

        StringBuilder sb = new StringBuilder();
        StringBuilder key = new StringBuilder();

        for(int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if('0' <= ch && ch <= '9') {  // 변경 필요 없음
                sb.append(ch);
            }else {  // 변경 필요
                key.append(ch);
                if(map.containsKey(key.toString())) {  // key 완성
                    // key 간 포함 관계는 형성되지 않으므로 고려 X

                    sb.append(map.get(key.toString()));  // 숫자 추가
                    key.setLength(0);  // key sb 초기화
                }
            }
        }

        answer = Integer.parseInt(sb.toString());
        return answer;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int ans = sol.solution("one4seveneight");
        System.out.println(ans);
    }
}
