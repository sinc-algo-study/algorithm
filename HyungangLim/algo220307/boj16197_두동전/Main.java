package algo220307.boj16197_두동전;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

class Status {
    int dept;
    Pair p1, p2;
    Status(int dept, Pair p1, Pair p2) {
        this.dept = dept;
        this.p1 = p1;
        this.p2 = p2;
    }
}

class Pair {
    int r, c;
    Pair(int r, int c) {
        this.r = r;
        this.c = c;
    }
}

public class Main {

    static int N, M, ans = 11;
    static char[][] map;
    static boolean[][][][] check;
    static int[] rArr = {-1, 1, 0, 0};
    static int[] cArr = {0, 0, -1, 1};

    public static void bfs(int sr1, int sc1, int sr2, int sc2) {
        Queue<Status> que = new ArrayDeque<>();
        que.add(new Status(0, new Pair(sr1, sc1), new Pair(sr2, sc2)));
        check[sr1][sc1][sr2][sc2] = true;

        while(!que.isEmpty()) {
            Status s = que.poll();

            int r1 = s.p1.r;
            int c1 = s.p1.c;
            int r2 = s.p2.r;
            int c2 = s.p2.c;
            int dept = s.dept;
            if(dept == 10) return;

            for(int i = 0; i < 4; i++) {
                int nr1 = r1 + rArr[i];
                int nc1 = c1 + cArr[i];
                int nr2 = r2 + rArr[i];
                int nc2 = c2 + cArr[i];

                // 이동 전에는 두 동전 모두 살아있음이 반드시 보장된다
                int cnt = 0;  // 떨어진 동전 개수
                if (!(-1 < nr1 && nr1 < N && -1 < nc1 && nc1 < M)) {
                    cnt += 1;
                }else if(map[nr1][nc1] == '#') {
                    nr1 = r1;
                    nc1 = c1;
                }
                if (!(-1 < nr2 && nr2 < N && -1 < nc2 && nc2 < M)) {
                    cnt += 1;
                }else if(map[nr2][nc2] == '#') {
                    nr2 = r2;
                    nc2 = c2;
                }

                if(cnt == 1) {
                    ans = dept + 1;
                    return;
                }
                if(cnt == 0 && !check[nr1][nc1][nr2][nc2]) {
                    check[nr1][nc1][nr2][nc2] = true;
                    que.add(new Status(dept + 1, new Pair(nr1, nc1), new Pair(nr2, nc2)));
                }
            }
        }
    }

    public static void process() {
        int r1 = 0, c1 = 0, r2 = 0, c2 = 0;
        boolean find = false;

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                if(map[i][j] == 'o') {
                    if(!find) {
                        r1 = i;
                        c1 = j;
                        find = true;
                    }else {
                        r2 = i;
                        c2 = j;
                        break;
                    }
                }
            }
        }

        bfs(r1, c1, r2, c2);
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String NM = br.readLine();
        N = Integer.parseInt(NM.split(" ")[0]);
        M = Integer.parseInt(NM.split(" ")[1]);

        map = new char[N][M];
        check = new boolean[N][M][N][M];
        for(int i = 0; i < N; i++) {
            String input = br.readLine();
            for(int j = 0; j < M; j++) {
                map[i][j] = input.charAt(j);
            }
        }
    }

    public static void output() {
        System.out.println(ans > 10 ? -1 : ans);
    }

    public static void main(String[] args) throws IOException {
        init();
        process();
        output();
    }
}
