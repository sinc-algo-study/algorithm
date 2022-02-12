package algo220214.boj6236_용돈관리;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 *
 * 이분탐색 문제
 * -> 주어진 조건에 맞춰 인출을 거듭한다.
 * -> 인출 횟수가 M 이하로 떨어지는 K의 최소 금액을 찾아라
 *
 * 1. 어제 쓰고 남은 돈 R과 N[i]를 비교한다
 * 2. R >= N[i] 라면 추가 인출 없이 R로 충당한다
 * 3. R < N[i]일 경우 R을 집어넣고 K원을 인출한다
 *
 * 다만 현우는 M 이라는 숫자를 좋아하기 때문에,
 * 정확히 M번을 맞추기 위해서 남은 금액이 그날 사용할 금액보다 많더라도
 * 남은 금액은 통장에 집어넣고 다시 K원을 인출할 수 있다.
 * ->
 * M 미만으로 인출 가능하면 억지로 더 인출해서 M까지 맞출 수 있으니
 * M 이하의 인출 횟수만 만족하면 된다는 뜻
 *
 * 통장에 얼마가 있는지는 주어지지 않음
 * 즉, 인출할 돈이 부족한 경우는 없으므로 그냥 K원씩 인출하기만 하면 됨
 * 신경써야 할 것은 인출 횟수를 M 이하로 맞추는 것 뿐
 *
 *
 * K 의 초기값으로 10,000이 불가능한 이유
 * ->
 * 2 1
 * 10000
 * 10000
 *
 */

public class Main {

    public static int binarySearch(int M, int[] arr) {
        int K = 10000 * arr.length;
        int min = 1;
        int max = Arrays.stream(arr).sum();
        int mid = (max + min) / 2;

        while(min <= max) {

            /**
             * mid 를 어떻게 연산에 포함시킬 것인가?
             * for(arr)를 다 돈다?
             *
             * 이분탐색은 O(logN) = 대략 20
             * 20 * 10만 = 200만.. 가능!!
             */

            // for를 돌며 인출 횟수를 센다
            // K < N[i]인 경우는 어떻게?
            // -> 문제에선 무조건 K >= N[i]인 것처럼 말하는데..
            // 그럼 arr의 최대값을 mid의 최초로 잡고 시작??
            // 그럼 min, max 는??

            // mid 값만 가지고 min, max를 설정할 수 없으므로
            // mid 조건 충족 안 될 경우 재설정하고 continue 하는 것으로 한다

            int cnt = 0;    // 인출 횟수
            int now = 0;  // 현재 수중의 돈
            boolean invalid = false;
            for(int i = 0; i < arr.length; i++) {

                if (mid < arr[i]) {  // mid 원 인출해도 해결 안 되는 경우?
                    invalid = true;
                    min = mid + 1;
                    mid = (max + min) / 2;
                    break;
                }

                if (now >= arr[i]) {  // 남은 돈으로 충분
                    now -= arr[i];
                } else {
                    now = mid - arr[i];
                    cnt += 1;
                }
            }

            if(invalid) continue;

            if(cnt > M) {  // M 초과 -> mid 키운다
                min = mid + 1;
            }else {  // M 이하 -> mid 줄인다
                K = Math.min(K, mid);
                max = mid - 1;
            }
            mid = (max + min) / 2;
        }

        return K;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];
        for(int i = 0; i < N; i++) {
            int ni = Integer.parseInt(br.readLine());
            arr[i] = ni;
        }

        int answer = binarySearch(M, arr);
        System.out.println(answer);
    }
}
