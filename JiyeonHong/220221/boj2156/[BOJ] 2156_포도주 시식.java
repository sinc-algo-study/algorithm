package boj2156;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        //앞 2 추가
        int[] wine=new int[n+1];
        for(int i=1;i<n+1;i++){
            wine[i]=Integer.parseInt(br.readLine());
        }
        System.out.println(soluton(n,wine));
    }

    public static int soluton(int n,int[] wine){
        int[] dp=new int[wine.length]; //포도주 i개가 주어졌을때, 가장 많이 마실 수 있는 양
        dp[1]=wine[1];
        if(n==1){
            return dp[1];
        }

        dp[2]=wine[1]+wine[2];
        for(int i=3;i<n+1;i++){
            int n0=dp[i-1];//0번 연속 마실 수 있는 경우
            int n1=dp[i-2]+wine[i];//1번 연속 마실 수 있는 경우
            int n2=dp[i-3]+wine[i-1]+wine[i];//2번 연속 마실 수 있는 경우
            dp[i]=Math.max(n0,n1);
            dp[i]=Math.max(n2,dp[i]);
        }
        return dp[n];
    }
}