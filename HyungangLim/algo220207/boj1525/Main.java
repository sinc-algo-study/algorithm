package algo220207.boj1525;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 *
 * 퍼즐조각맞추기에서는 n으로 행구분 하고 왜 여기선 안 함?
 * ->
 * 여기선 배열 전체를 문자열화하기 때문에 행구분이 필요 없다
 *
 * 퍼즐조각맞추기는 "전체 배열의 일부"인 퍼즐을 문자열화 하기 때문에
 * 퍼즐의 모양에 따라 매번 행/열이 달라지므로 n구분이 필요.
 *
 *
 * 종료조건을 어떻게 잡아야 할까...
 *
 */

public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder sb;
    static Map<String, Integer> hm;
    static int[] rArr = {-1, 1, 0, 0};
    static int[] cArr = {0, 0, -1, 1};

    // index = i * c + j
    // i = index / c
    // j = index % c

    public static void bfs(String start) {
        Queue<String> que = new ArrayDeque<>();
        que.add(start);
        hm.put(start, 0);

        while(!que.isEmpty()) {
            String now = que.poll();
            if(now.equals("123456780")) {
                return;
            }

            int indexOfZero = now.indexOf('0');
            for(int i = 0; i < 4; i++) {
                int nr = indexOfZero / 3 + rArr[i];
                int nc = indexOfZero % 3 + cArr[i];
                if(!(-1 < nr && nr < 3 && -1 < nc && nc < 3)) continue;

                int indexOfDest = nr * 3 + nc;
                sb = new StringBuilder(now);
                sb.setCharAt(indexOfZero, now.charAt(indexOfDest));
                sb.setCharAt(indexOfDest, '0');

                if(!hm.containsKey(sb.toString())) {
                    hm.put(sb.toString(), hm.get(now) + 1);
                    que.add(sb.toString());
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();
        hm = new HashMap<>();

        for(int i = 0; i < 3; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < 3; j++) {
                sb.append(st.nextToken());
            }
        }

        bfs(sb.toString());
        System.out.println(hm.containsKey("123456780") ? hm.get("123456780") : -1);
    }
}
