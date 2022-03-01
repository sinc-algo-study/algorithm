package algo220301.boj11054_가장바이토닉부분수열;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int N, ans;
    static int[] arr;
    static int[] dp1;  // dp1[n] : [n]에서 끝나는 가장 긴 증가 부분수열의 길이
    static int[] dp2;  // dp2[n] : [n]에서 시작되는 가장 긴 감소 부분수열의 길이

    public static void process() {
        // 증가 부분수열
        dp1[0] = 1;
        for(int i = 1; i < N; i++) {
            for(int j = 0; j < i; j++) {
                if(arr[i] > arr[j]) {
                    dp1[i] = Math.max(dp1[i], dp1[j]);
                }
            }
            dp1[i] += 1;
        }

        // 감소 부분수열
        dp2[N-1] = 1;
        for(int i = N-2; i >= 0; i--) {
            for(int j = N-1; j > i; j--) {
                if(arr[i] > arr[j]) {
                    dp2[i] = Math.max(dp2[i], dp2[j]);
                }
            }
            dp2[i] += 1;
        }
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        arr = new int[N];
        dp1 = new int[N];
        dp2 = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
    }

    public static void output() {
        for(int i = 0; i < N; i++) {
            ans = Math.max(ans, dp1[i] + dp2[i]);
        }
        System.out.println(ans - 1);
    }

    public static void main(String[] args) throws IOException {
        init();
        process();
        output();
    }
}
