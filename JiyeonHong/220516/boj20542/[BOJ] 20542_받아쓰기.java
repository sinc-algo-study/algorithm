package boj20542;

import java.io.BufferedReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        sc.nextLine();
        String writing=sc.nextLine();
        String result=sc.nextLine();

        System.out.println(solution(writing,result));
    }

    public static int solution(String writing,String result){
        int answer=0;
        int N=writing.length();
        int M=result.length();
        int[][] dp=new int[N+1][M+1];
        /*
        문자 같을 경우 : [i-1][j-1]
        문자 다른 경우 : 수정 - [i-1][j-1]+1
                       삭제 - [i-1][j]+1
                       삽입 - [i][j-1]+1
          0 f i s h c a k e
        0 0 1 2 3 4 5 6 7 8
        t 1 1 2
        a 2 2
        k 3
        e 4
        n 5
         */
        for(int j=0;j<dp[0].length;j++){
            dp[0][j]=j;
        }
        for(int i=0;i<dp.length;i++){
            dp[i][0]=i;
        }

        for(int i=1;i<dp.length;i++){
            for(int j=1;j<dp[i].length;j++){
                if(isSame(writing,i-1,result,j-1)){
                    dp[i][j]=dp[i-1][j-1];
                }else{
                    int min=Math.min(dp[i-1][j-1]+1,dp[i-1][j]+1);
                    min=Math.min(dp[i][j-1]+1,min);
                    dp[i][j]=min;
                }
            }
        }
        answer=dp[N][M];
        return answer;
    }

    public static boolean isSame(String writing,int wIdx,String result,int rIdx){
        if(writing.charAt(wIdx)=='i' &&
                (result.charAt(rIdx)=='j' || result.charAt(rIdx)=='l')){
            return true;
        }

        if(writing.charAt(wIdx)=='v' && result.charAt(rIdx)=='w'){
            return true;
        }

        if(writing.charAt(wIdx)==result.charAt(rIdx)){
            return true;
        }

        return false;
    }

}