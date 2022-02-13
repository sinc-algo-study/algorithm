package algo220214.pgs72414_광고삽입;

//import java.text.ParseException;
//import java.text.SimpleDateFormat;
//import java.util.ArrayList;
//import java.util.Collections;
//import java.util.Date;
//import java.util.List;


/**
 *
 * 만약, 시청자들의 누적 재생시간이 가장 많은 곳이 여러 곳이라면,
 * 그 중에서 가장 빠른 시작 시각을 return 하도록 합니다.
 * -> 가장 빨리 나오는 정답을 바로 반환하자
 *
 * 1. 브루트포스 - 00:00:00 ~ play_time 각 위치에서 adv_time을 다 넣어보고 각각의 logs의 합을 구하면?
 * ->
 * play_time 은 최대 359,999 초
 * logs는 최대 300,000
 * ->
 * 36만 * 30만 = 1080억.. 절대 불가능
 *
 *
 * 2. logs를 시작시간 기준으로 정렬
 * ->
 * 각 시작시간에 adv_time 맞추는 것으로 하여 총 재생시간 계산한다면?
 * 30만가지 경우가 나오긴 하겠지만 한가지 경우에 대해 30만번 다 체크할 필요는 없다
 * (adv_time 범위 내에 있는 것만 체크하면 되니까)
 * ->
 * 예외 케이스
 * play_time : 10:00:00
 * adv_time : 03:30:00
 * logs : [[02:00:00 ~ 04:00:00], [03:00:00 ~ 05:00:00]]
 * ans = 01:30:00 이지만 02:00:00가 나와버린다.
 *
 *
 * 3. 그럼.. logs의 종료시간을 기준으로 본다면?
 * adv_time의 끝이 각 log의 끄트머리에 걸쳐지며 검사가 이뤄지니 가능할듯?
 * -> 일단 해보자
 * -> 이것도 반례 존재..
 * -> 반드시 어떤 log의 시작점이나 끝점에 걸친다는 건 보장되지 않는다.
 *
 */

//class Log implements Comparable<Log> {
//    String begin, end;
//    long time;
//    Log(String begin, String end, long time) {
//        this.begin = begin;
//        this.end = end;
//        this.time = time;
//    }
//
//    @Override
//    public int compareTo(Log o) {
//        // end 문자열 기준 내림차순 정렬
//        return o.end.compareTo(this.end);
//    }
//}
//
//class Solution {
//
//    public String solution(String play_time, String adv_time, String[] logs) throws ParseException {
//        // answer는 adv_time의 종료 시간이다
//        // 문제의 요구사항은 adv_time의 시작시간이다
//        // 즉, answer - adv_time을 반환해야 한다
//
//        String answer = "99:59:59";
//        List<Log> list = new ArrayList<>();
//        SimpleDateFormat sdf = new SimpleDateFormat("HH:MM:SS");
//
//        for(int i = 0; i < logs.length; i++) {
//            String[] split = logs[i].split("~");
//            Date begin = sdf.parse(split[0]);
//            Date end = sdf.parse(split[1]);
//            long time = (end.getTime() - begin.getTime()) / 1000;
//            list.add(new Log(split[0], split[1], time));
//        }
//        Collections.sort(list);
//
//        return answer;
//    }
//}

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
        long max = 0;
        for(int i = 0; i < advTime; i++) {
            sum += personPerSec[i];
        }
        max = sum;

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
