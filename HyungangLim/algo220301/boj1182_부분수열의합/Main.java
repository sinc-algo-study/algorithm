package algo220301.boj1182_부분수열의합;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int N, S, ans;
    static int[] arr;

    public static void dfs(int dept, int sum) {
        if(dept == N) {
            if(sum == S) {
                ans += 1;
            }
            return;
        }
        dfs(dept + 1, sum);
        dfs(dept + 1, sum + arr[dept]);
    }

    public static void process() {
        dfs(0, 0);
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
    }

    public static void output() {
        System.out.println(S == 0 ? ans - 1 : ans);
    }

    public static void main(String[] args) throws IOException {
        init();
        process();
        output();
    }
}
