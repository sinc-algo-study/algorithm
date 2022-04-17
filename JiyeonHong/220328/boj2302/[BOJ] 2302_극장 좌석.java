package boj2302;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
//  12 3 4 5 6 7 8 9
class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());
        int M=Integer.parseInt(br.readLine());
        int[] vips=new int[M];
        for(int i=0;i<M;i++){
            vips[i]=Integer.parseInt(br.readLine());
        }

        System.out.println(solution(N,vips));
    }

    public static int solution(int N,int[] vips){
        int answer=1;
        int[] dp=new int[N+1];
        dp[0]=1;
        dp[1]=1;
        dp[2]=2;

        for(int i=3;i<dp.length;i++){
            dp[i]=dp[i-1]+dp[i-2];
        }

        int pre=0;
        for(int i=0;i<vips.length;i++){
            answer*=dp[vips[i]-pre-1];
            pre=vips[i];
        }


        answer*=dp[N-pre];
        return answer;
    }


}