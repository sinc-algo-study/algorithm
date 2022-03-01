package algo220301.boj1208_부분수열의합2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

/**
 *
 * 모든 부분수열 만들어야 함
 * -> N 제한이 커서 시간 초과
 * -> 절반 나눠서 부분수열 구한 후 각각에 대응해서 S를 완성할 수 있는 값을 찾는다
 *
 */

public class Main {

    static int N, S;
    static long ans;
    static int[] arr;

    public static int lowerBound(ArrayList<Integer> list, int target) {
        int min = 0;
        int max = list.size();
        while(min < max) {
            int mid = (min + max) / 2;
            if(list.get(mid) >= target) {
                max = mid;
            }else {
                min = mid + 1;
            }
        }
        return max;
    }

    public static int upperBound(ArrayList<Integer> list, int target) {
        int min = 0;
        int max = list.size();
        while(min < max) {
            int mid = (min + max) / 2;
            if(list.get(mid) <= target) {
                min = mid + 1;
            }else {
                max = mid;
            }
        }
        return max;
    }

    public static void dfs(int dept, int target, int sum, ArrayList<Integer> list) {
        if(dept == target) {
            list.add(sum);
            return;
        }
        dfs(dept + 1, target, sum, list);
        dfs(dept + 1, target, sum + arr[dept], list);
    }

    public static void process() {
        ArrayList<Integer> firstList = new ArrayList<>();
        ArrayList<Integer> secondList = new ArrayList<>();

        dfs(0, N / 2, 0, firstList);
        dfs(N / 2, N, 0, secondList);

        Collections.sort(firstList);
        Collections.sort(secondList);

        for(int num : firstList) {
            int target = S - num;
            int upper = upperBound(secondList, target);
            int lower = lowerBound(secondList, target);
            ans += upper - lower;
        }
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
