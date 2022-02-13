package algo220214.boj1113_수영장만들기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 *
 * (3, 5) -> (5, 7)
 * -> 15
 * 0 0 0 0 0 0 0
 * 0 1 6 6 6 1 0
 * 0 6 1 1 1 6 0
 * 0 1 6 6 6 1 0
 * 0 0 0 0 0 0 0
 *
 *
 * (4, 6) -> (6, 8)
 * -> 48
 * 0 0 0 0 0 0 0 0
 * 0 9 9 9 9 9 9 0
 * 0 9 5 5 1 1 9 0
 * 0 9 5 5 1 1 9 0
 * 0 9 9 9 9 9 9 0
 * 0 0 0 0 0 0 0 0
 *
 *
 * (5, 9) -> (7, 11)
 * -> 7
 * 0 0 0 0 0 0 0 0 0 0 0
 * 0 1 1 1 1 1 1 1 1 1 0
 * 0 1 1 5 1 1 1 6 1 1 0
 * 0 1 3 1 5 1 6 1 6 1 0
 * 0 1 1 5 1 1 1 6 1 1 0
 * 0 1 1 1 1 1 1 1 1 1 0
 * 0 0 0 0 0 0 0 0 0 0 0
 *
 *
 * (9, 13) -> (11, 15)
 * -> 151
 * 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 * 0 1 1 1 1 1 1 1 1 1 1 1 1 1 0
 * 0 1 5 5 5 5 5 5 5 5 5 5 5 1 0
 * 0 1 5 1 1 1 1 1 1 1 1 1 5 1 0
 * 0 1 5 1 1 1 9 9 9 1 1 1 5 1 0
 * 0 1 5 1 1 1 9 2 9 1 1 1 5 1 0
 * 0 1 5 1 1 1 9 9 9 1 1 1 5 1 0
 * 0 1 5 1 1 1 1 1 1 1 1 1 5 1 0
 * 0 1 5 5 5 5 5 5 5 5 5 5 5 1 0
 * 0 1 1 1 1 1 1 1 1 1 1 1 1 1 0
 * 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 *
 *
 * 아 진짜 이거인듯??
 * 일단 나랑 같은 칸으로만 탐색을 함
 * 여기서 나를 둘러싼 칸 중에 나보다 작은 칸이 있으면 바로 탐색 빠져나오고 패스
 * ( 여기서 바로 빠져나오기 위해서 BFS를 해야함 재귀로 하면 빠져나오기 위해 flag 써야하면서 좀 복잡해짐 )
 *
 *
 * 1. 일단 0 으로 둘러싸야 할 것 같은 느낌적인 느낌.
 * 2. 1~9의 val 반복을 돌며 해당 값을 갖는 좌표들 탐색
 * 3. 탐색에서 0이랑 만난다면 어차피 여긴 채울 수 없는 칸이므로 바로 탐색 종료.
 * 4. 꼭 0이 아니더라도 이번 탐색의 val 보다 작으면 채울 수 없는 건 마찬가지. 그냥 val 미만 조건으로 빠져나오면 된다.
 * 5. 그럼 어디까지 채울건데? 이번 탐색에서 만난 나보다 큰 칸 중 가장 작은 높이까지!
 * 6. 이런식으로 1~9를 돌면서 채우는 양의 누적합을 구하면 됨
 *
 */

class Pair {
    int r, c;
    Pair(int r, int c) {
        this.r = r;
        this.c = c;
    }
}

public class Main {
    static int N, M, ans;
    static int[][] map;
    static int[][] check;
    static int[] rArr = {-1, 1, 0, 0};
    static int[] cArr = {0, 0, -1, 1};

//    public static void bfs(int r, int c, int val) {
//        int min = 9;  // 나를 둘러싼 나보다 큰 수들 중 가장 작은 수
//
//        Queue<Pair> que = new ArrayDeque<>();
//        ArrayList<Pair> list = new ArrayList<>();
//        Pair start = new Pair(r, c);
//        que.add(start);
//        list.add(start);
//        check[r][c] = val;
//
//        while(!que.isEmpty()) {
//            Pair p = que.poll();
//
//            for(int i = 0; i < 4; i++) {
//                int nr = p.r + rArr[i];
//                int nc = p.c + cArr[i];
//
//                // 범위 체크는 할 필요가 없다. 어차피 0으로 다 둘러놔서 val 검사로 다 커버됨.
//                if(map[nr][nc] < val) return;
//                if(map[nr][nc] > val) {
//                    min = Math.min(min, map[nr][nc]);
//                    continue;
//                }
//                if(check[nr][nc] == val) continue;
//
//                Pair next = new Pair(nr, nc);
//                que.add(next);
//                list.add(next);
//                check[nr][nc] = val;
//            }
//        }
//
//        // 여기까지 무사히 도착했으면 이번 탐색에서 방문한 곳들은 채울 수 있는 칸이라는 것
//        ans += (min - val) * list.size();
//        for(Pair p : list) {
//            map[p.r][p.c] = min;
//        }
//    }

    public static void bfs(int r, int c, int val) {
        int min = 9;  // 나를 둘러싼 나보다 큰 수들 중 가장 작은 수
        boolean isValid = true;

        Queue<Pair> que = new ArrayDeque<>();
        ArrayList<Pair> list = new ArrayList<>();
        Pair start = new Pair(r, c);
        que.add(start);
        list.add(start);
        check[r][c] = val;

        while(!que.isEmpty()) {
            Pair p = que.poll();

            for(int i = 0; i < 4; i++) {
                int nr = p.r + rArr[i];
                int nc = p.c + cArr[i];

                // 범위 체크는 할 필요가 없다. 어차피 0으로 다 둘러놔서 val 검사로 다 커버됨.
                if(check[nr][nc] == val) continue;
                if(map[nr][nc] != val) {
                    if(map[nr][nc] > val) {
                        min = Math.min(min, map[nr][nc]);
                    }else {
                        isValid = false;
                    }
                    continue;
                }

                Pair next = new Pair(nr, nc);
                que.add(next);
                list.add(next);
                check[nr][nc] = val;
            }
        }

        // 여기까지 무사히 도착했으면 이번 탐색에서 방문한 곳들은 채울 수 있는 칸이라는 것
        if(isValid) {
            ans += (min - val) * list.size();
            for(Pair p : list) {
                map[p.r][p.c] = min;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N+2][M+2];
        check = new int[N+2][M+2];

        // 바깥이랑 닿지 않는 칸이 생길 수 있는 최소 크기
        if(N < 3 && M < 3) {
            System.out.println(0);
            return;
        }

        // 0으로 둘러싸기
        for(int i = 1; i <= N; i++) {
            char[] input = br.readLine().toCharArray();
            int idx = 0;
            for(int j = 1; j <= M; j++) {
                map[i][j] = input[idx++] - '0';
            }
        }

        // 50 * 50 * 9
        for(int val = 1; val <= 9; val++) {
            for(int i = 1; i <= N; i++) {
                for(int j = 1; j <= M; j++) {
                    if(check[i][j] != val && map[i][j] == val) {
                        bfs(i, j, val);
                    }
                }
            }
        }

        System.out.println(ans);
    }
}
