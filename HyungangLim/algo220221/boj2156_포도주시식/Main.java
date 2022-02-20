package algo220221.boj2156_포도주시식;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

//public class Main {
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int N = Integer.parseInt(br.readLine());
//        int[] arr = new int[N + 1];
//        for(int i = 1; i <= N; i++) {
//            arr[i] = Integer.parseInt(br.readLine());
//        }
//
//        int[] dp = new int[N + 1];
//        dp[1] = arr[1];
//        if(N > 1) {
//            dp[2] = arr[1] + arr[2];
//        }
//
//        for(int i = 3; i <= N; i++) {
//            dp[i] = Math.max(Math.max(
//                    dp[i-1],                       // 0번 연속
//                    dp[i-2] + arr[i]),             // 1번 연속
//                    dp[i-3] + arr[i-1] + arr[i]);  // 2번 연속
//        }
//
//        int ans = Arrays.stream(dp).max().getAsInt();
//        System.out.println(ans);
//    }
//}


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N + 1];
        for(int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        int[][] dp = new int[N+1][3];
        dp[1][0] = 0;
        dp[1][1] = arr[1];
        dp[1][2] = arr[1];
        for(int i = 2; i <= N; i++) {
            dp[i][0] = Math.max(Math.max(
                    dp[i-1][0],
                    dp[i-1][1]),
                    dp[i-1][2]);
            dp[i][1] = dp[i-1][0] + arr[i];
            dp[i][2] = dp[i-1][1] + arr[i];
        }

        int ans = Arrays.stream(dp[N]).max().getAsInt();
        System.out.println(ans);
    }
}