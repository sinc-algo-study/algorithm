package algo220321.boj2294_동전2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 동전의 개수를 최소로 하여 K원을 만들어야 한다
 * dp[K] = K원을 만들 수 있는 최소 동전 개수
 */

public class Main {

    static int N, K;
    static int[] arr;
    static int[] dp1;
    static int[][] dp2;

    public static void process1() {
        // dp[K] = K원 만드는 최소 동전 개수
        // 2차원으로는 어떻게?

        Arrays.fill(dp1, 10001);
        dp1[0] = 0;

        for(int i = 0; i < N; i++) {
            for(int j = arr[i]; j <= K; j++) {  // if(j - arr[i] >= 0) 가 필요없는 이유
                dp1[j] = Math.min(dp1[j], dp1[j - arr[i]] + 1);
            }
        }

        // K를 먼저 돌리는 건 불가능?
//        for(int i = 1; i <= K; i++) {
//            for(int j = 0; j < N; j++) {
//                if(i - arr[j] >= 0) {
//                    dp[i] = Math.min(dp[i], dp[i - arr[j]] + 1);
//                }
//            }
//        }
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        arr = new int[N];
        for(int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        dp1 = new int[K+1];
        dp2 = new int[N][K+1];
    }

    public static void output() {
        System.out.println(dp1[K] == 10001 ? -1 : dp1[K]);
    }

    public static void main(String[] args) throws IOException {
        init();
        process1();
        output();
    }
}
