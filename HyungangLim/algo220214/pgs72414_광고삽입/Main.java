package algo220214.pgs72414_광고삽입;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.TimeZone;

/**
 *
 * 74.2 / 100.0
 *
 * 1. play_time 의 최대값 99:59:59 를 초로 환산하면 359,999 초
 * 각 초마다 시청자의 수를 계산한다.
 *
 * 2. adv_time 가 시작 가능한 모든 위치에 대해 반복문
 * -> adv 가 위치할 수 있는 각 구간마다 초당 시청자 수의 누적값을 구한다
 *
 */

class Solution {

    public String solution(String play_time, String adv_time, String[] logs) throws ParseException {
        SimpleDateFormat sdf = new SimpleDateFormat("hh:mm:ss");
        sdf.setTimeZone(TimeZone.getTimeZone("GMT"));
        int playTime = (int)sdf.parse(play_time).getTime() / 1000;
        int advTime = (int)sdf.parse(adv_time).getTime() / 1000;

        // 30만 * 36만 = 최대 1080억... 이게 맞아? 일단 해보자..
        int[] personPerSec = new int[playTime + 1];
        for(int i = 0; i < logs.length; i++) {
            String[] split = logs[i].split("-");
            int startTime = (int)sdf.parse(split[0]).getTime() / 1000;
            int endTime = (int)sdf.parse(split[1]).getTime() / 1000;

            // endTime은 포함하지 않는다
            for(int j = startTime; j < endTime; j++) {
                personPerSec[j] += 1;
            }
        }

        // 누적값이 동일할 경우 가장 빠른 시간이 정답
        // -> 같을 때는 갱신하지 않는다
        // 여기서 시간초과 방지 위해 슬라이딩 윈도우 사용?

        // 슬라이딩 윈도우 사용을 위해 일단 00:00:00 시작은 그냥 구해준다
        int ansTime = 0;
        long sum = 0;
        for(int i = 0; i < advTime; i++) {
            sum += personPerSec[i];
        }
        long max = sum;

        int startTime = 0;
        int endTime = advTime;

        while(startTime <= playTime-advTime) {  // 슬라이딩 윈도우. <, <= 결과가 똑같다? <=가 맞을 거 같긴 한데
            sum -= personPerSec[startTime++];
            sum += personPerSec[endTime++];
            if(sum > max) {
                max = sum;
                ansTime = startTime;
            }
        }

        int h = ansTime / 3600; ansTime %= 3600;
        int m = ansTime / 60;
        int s = ansTime % 60;
        String answer = (h < 10 ? "0" + h : h) + ":" +
                (m < 10 ? "0" + m : m) + ":" +
                (s < 10 ? "0" + s : s);
        return answer;
    }
}

public class Main {

    public static void main(String[] args) throws ParseException {
        Solution sol = new Solution();

        // return "01:30:59"
        String play_time = "02:03:55";
        String adv_time = "00:14:15";
        String[] logs = { "01:20:15-01:45:14", "00:25:50-00:48:29",
                "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29" };

        // return "01:00:00"
//        String play_time = "99:59:59";
//        String adv_time = "25:00:00";
//        String[] logs = { "69:59:59-89:59:59", "01:00:00-21:00:00",
//                "79:59:59-99:59:59", "11:00:00-31:00:00" };

        // return "00:00:00"
//        String play_time = "50:00:00";
//        String adv_time = "50:00:00";
//        String[] logs = { "15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45" };

        String ans = sol.solution(play_time, adv_time, logs);
        System.out.println(ans);
    }
}
