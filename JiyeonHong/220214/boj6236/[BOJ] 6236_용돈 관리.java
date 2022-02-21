package boj6236;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
/*
통장에서 K원을 인출
통장에서 뺀 돈으로 하루를 보낼 수 있으면 그대로 사용
모자라게 되면 남은 금액은 통장에 집어넣고 다시 K원을 인출
정확히 M번을 맞추기 위해서 남은 금액이 그날 사용할 금액보다 많더라도 남은 금액은 통장에 집어넣고 다시 K원을 인출
 */
class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String[] arr=br.readLine().split(" ");
        int N=Integer.parseInt(arr[0]);
        int M=Integer.parseInt(arr[1]);

        int[] money=new int[N];
        int maxMoney=0;
        for(int i=0;i<N;i++){
            money[i]=Integer.parseInt(br.readLine());
            maxMoney=Math.max(maxMoney,money[i]);
        }

        System.out.println(solution(money,maxMoney,M));
    }

    public static int solution(int[] money,int maxMoney,int M){
        int answer=100000*10000;
        int low=maxMoney; //하루 이용 금액 중 최대 금액
        int high=100000*10000;
        int mid=0;
        while(low<=high){
            mid=(low+high)/2;

            int remain=mid;
            int count=1;
            for(int i=0;i<money.length;i++){
                if(remain<money[i]){
                    remain=mid;
                    count++;
                }
                remain-=money[i];
            }

            if(count>M){
                low=mid+1;
            }else{
                /*
                남은 금액>사용할 금액이면 다시 인출 가능
                -> count는 count~(count+N) 범위 가능
                 */
                answer=Math.min(answer,mid);
                high=mid-1;
            }
        }

        return answer;
    }
}