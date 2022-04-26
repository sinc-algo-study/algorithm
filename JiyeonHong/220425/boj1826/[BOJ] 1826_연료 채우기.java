package boj1826;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
class Station{
    int dist;
    int fuel;

    public Station(int dist,int fuel){
        this.dist=dist;
        this.fuel=fuel;
    }
}

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());

        Integer[][] station=new Integer[N][2];
        for(int i=0;i<N;i++){
            String[] arr=br.readLine().split(" ");
            station[i][0]=Integer.parseInt(arr[0]);
            station[i][1]=Integer.parseInt(arr[1]);
        }

        Arrays.sort(station, new Comparator<Integer[]>() {
            @Override
            public int compare(Integer[] o1, Integer[] o2) {
                return o1[0]-o2[0];
            }
        });

        String s= br.readLine();
        int L=Integer.parseInt(s.split(" ")[0]);
        int P=Integer.parseInt(s.split(" ")[1]);
        System.out.println(solution(L,P,station));
    }

    public static int solution(int L,int P,Integer[][] station){
        int answer=0;

        /*
        1. 현재 연료양으로 도착지점 갈 수 있는지 확인 (now<L)
        2. 갈 수 없다면 현재 연료로 갈 수 있는 주요소 pq에 push
        3. pq에서 가장 연료 많이 주는 곳 pop
        */
        PriorityQueue<Station> pq=new PriorityQueue<>(new Comparator<Station>() {
            @Override
            public int compare(Station o1, Station o2) {
                return o2.fuel-o1.fuel;
            }
        });

        int possibleIdx=0;
        int fuelNow=P;
        while(fuelNow<L){
            while(possibleIdx<station.length && station[possibleIdx][0]<=fuelNow){
                pq.add(new Station(station[possibleIdx][0],station[possibleIdx][1]));
                possibleIdx++;
            }

            if(!pq.isEmpty()){
                Station s=pq.poll();
                fuelNow+=s.fuel;
                answer++;
            }else{
                answer=-1;
                break;
            }

        }

        return answer;
    }
}