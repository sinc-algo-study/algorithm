package other.boj3687_성냥개비;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int[] minArr = {0, 0, 1, 7, 4, 2, 0, 8, 10};  // 0~8개로 만들 수 있는 최소 숫자들
    static long[] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        while(T-- > 0) {
            StringBuilder sb = new StringBuilder();
            int N = Integer.parseInt(br.readLine());

            // get max
            if(N % 2 == 0) {
                for(int i = 0; i < N / 2; i++) {
                    sb.append("1");
                }
            }else {
                sb.append("7");
                for(int i = 0; i < N / 2 - 1; i++) sb.append("1");
            }

            // get min
            dp = new long[101];
            Arrays.fill(dp, Long.MAX_VALUE);
            for(int i = 0; i <= 8; i++) {
                dp[i] = minArr[i];
            }
            dp[6] = 6;

            for(int i = 9; i <= 100; i++) {
                for(int j = 2; j <= 7; j++) {
                    dp[i] = Math.min(dp[i], dp[i-j] * 10 + minArr[j]);
                }
            }

            System.out.println(dp[N] + " " + sb.toString());
        }

//        for (int i = 0; i <= 100; i++) {
//            System.out.println("dp[" + i + "] : " + dp[i]);
//        }
    }
}
