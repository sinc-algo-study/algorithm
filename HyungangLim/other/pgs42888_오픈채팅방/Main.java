package other.pgs42888_오픈채팅방;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public ArrayList<String> solution(String[] record) {
        ArrayList<String> answer = new ArrayList<>();
        Map<String, String> hm = new HashMap<>();  // user id, nickname

        for(String str : record) {
            String[] s = str.split(" ");
            switch(s[0]) {
                case "Enter":
                    hm.put(s[1], s[2]);
                    answer.add(s[1] + "님이 들어왔습니다.");
                    break;
                case "Leave":
                    answer.add(s[1] + "님이 나갔습니다.");
                    break;
                case "Change":
                    hm.put(s[1], s[2]);
                    break;
            }
        }

        for(int i = 0; i < answer.size(); i++) {
            String nick = answer.get(i).split("님이")[0];
            String temp = answer.get(i).replaceAll(nick, hm.get(nick));
            answer.set(i, temp);
        }

        return answer;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        String[] record = {"Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"};
        ArrayList<String> answer = sol.solution(record);

        for(String ans : answer) {
            System.out.println(ans);
        }
    }
}
