package pgs92341;
import java.util.*;

class Main{
    public static void main(String[] args) {
        String[] records={"05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT",
                "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"};
        int[] fees={180, 5000, 10, 600};
        Solution s=new Solution();
        s.solution(fees,records);
    }
}

class Solution {
    public int[] solution(int[] fees, String[] records) {
        int[] answer = {};

        Map<String,Integer> parking=new HashMap<>();//차번호 : 시간
        Map<String,Integer> sum=new HashMap<>();
        sum.clear();

        for(int i=0;i<records.length;i++){
            String[] arr=records[i].split(" ");
            String[] times=arr[0].split(":");
            int time=60*Integer.parseInt(times[0])+Integer.parseInt(times[1]);

            if(arr[2].equals("IN")){ //입차
                parking.put(arr[1],time);
            }else{ //출차
                int inTime=parking.get(arr[1]);
                parking.remove(arr[1]);
                sum.put(arr[1],sum.getOrDefault(arr[1],0)+time-inTime);
            }
        }

        //23:59분에 출차하는 경우
        if(parking.size()>0){
            for(String num : parking.keySet()){
                sum.put(num,sum.getOrDefault(num,0)+(60*23+59)-parking.get(num));
            }
        }

        answer=new int[sum.size()];
        int idx=0;
        String[] numbers= sum.keySet().toArray(new String[0]);
        Arrays.sort(numbers);

        for(int i=0;i<numbers.length;i++){
            int totalTime=sum.get(numbers[i]);
            if(totalTime<=fees[0]){
                answer[idx++]=fees[1];
            }else{
                answer[idx++]=fees[1]+fees[3]*(int)Math.ceil((double)(totalTime-fees[0])/fees[2]);
            }
        }

        return answer;
    }
}