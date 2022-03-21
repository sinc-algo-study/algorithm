package algo220321.pgs92341_주차요금계산;

import java.util.*;

/**
 * 어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주합니다.
 * -> 입차된 후에 남아있는 차들에 대해 따로 계산 필요
 *
 * 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림합니다.
 * -> 초과시간 계산 후에 올림 로직 필요
 *
 * 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열에 담아서 return 하도록 solution 함수를 완성해주세요.
 * -> 차량 정렬 기준 필요
 *
 * records의 원소들은 시각을 기준으로 오름차순으로 정렬되어 주어집니다.
 * -> 출차 기록이 먼저 들어오는 경우 고려 불필요
 */

class Record {
    String inTime, outTime;
    Record(String inTime) {
        this.inTime = inTime;
    }
    public int calcTime() {
        // 분단위로 계산
        String[] inArr = inTime.split(":");
        int from = Integer.parseInt(inArr[0]) * 60 + Integer.parseInt(inArr[1]);
        String[] outArr = outTime.split(":");
        int to = Integer.parseInt(outArr[0]) * 60 + Integer.parseInt(outArr[1]);
        return to - from;
    }
}

class Car implements Comparable<Car> {
    String num;  // time == 체류시간
    int time, fee;
    Car(String num) {
        this.num = num;
    }
    @Override
    public int compareTo(Car other) {
        return this.num.compareTo(other.num);
    }
    public void calcFee(int[] fees) {
        if(time <= fees[0]) {
            fee = fees[1];
        }else {
            fee = fees[1];    // 기본요금 차징
            time -= fees[0];  // 일단 기본시간 빼고

            // 초과시간 요금 부과
            fee += time / fees[2] * fees[3];
            if(time % fees[2] != 0) {
                fee += fees[3];  // 올림 처리
            }
        }
    }
}

class Solution {
    public List<Integer> solution(int[] fees, String[] records) {
        Map<String, Record> recordMap = new HashMap<>();
        Map<String, Car> carMap = new HashMap<>();

        // calc record
        for(String record : records) {
            String[] arr = record.split(" ");
            // arr[0] == 시각
            // arr[1] == 차번호
            // arr[2] == 내역 (입차/출차)  // 필요없음

            String time = arr[0];
            String number = arr[1];

            if(!carMap.containsKey(number))
                carMap.put(arr[1], new Car(number));

            if(!recordMap.containsKey(number)) {
                recordMap.put(arr[1], new Record(time));
            }else {
                // outTime 설정한 후 totalTime 구하여 더해준다
                Record rec = recordMap.get(number);
                rec.outTime = time;
                carMap.get(number).time += rec.calcTime();
                recordMap.remove(number);  // 완료된 체류기록은 삭제
            }
        }

        // 출차 기록 없는 차들에 대한 처리
        for(String number : recordMap.keySet()) {
            Record rec = recordMap.get(number);
            rec.outTime = "23:59";
            carMap.get(number).time += rec.calcTime();

        }


        // 차량 번호 오름차순으로 요금 담아야 함
        PriorityQueue<Car> pq = new PriorityQueue<>();
        for(String key : carMap.keySet()) {
            Car car = carMap.get(key);
            car.calcFee(fees);
            pq.add(car);
        }

        List<Integer> answer = new ArrayList<>();
        while(!pq.isEmpty()) {
            answer.add(pq.poll().fee);
        }
        return answer;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] fees = {180, 5000, 10, 600};
        String[] records = {"05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"};

//        int[] fees = {120, 0, 60, 591};
//        String[] records = {"16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"};

//        int[] fees = {1, 461, 1, 10};
//        String[] records = {"00:00 1234 IN"};

        List<Integer> ans = sol.solution(fees, records);
        for(int num : ans) {
            System.out.print(num + " ");
        }
    }
}
