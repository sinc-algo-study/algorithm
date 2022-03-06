package algo220307.boj11559_PuyoPuyo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

/**
 * R G B P Y
 */

class Pair {
    int r, c;
    Pair(int r, int c) {
        this.r = r;
        this.c = c;
    }
    public int getR() {
        return this.r;
    }
    public int getC() {
        return this.c;
    }
}

public class Main {

    static int N, M, ans;
    static char[][] map;
    static boolean[][] check;
    static int[] rArr = {-1, 1, 0, 0};
    static int[] cArr = {0, 0, -1, 1};

    public static void goDownPuyo() {
        for(int j = 0; j < M; j++) {
            for(int i = N-2; i >= 0; i--) {
                if (map[i][j] == '.') continue;

                int nr = 0;
                for(int ii = i + 1; ii < N; ii++) {  // 내려갈 수 있는 가장 아래 좌표를 찾는다
                    if(map[ii][j] != '.') {  // '.'이 아닌 칸을 만났다면 그 위칸이 목적지
                        nr = ii - 1;
                        break;
                    }
                    if(ii == N-1) {  // 마지막칸까지 찾지 못했다면 그곳이 목적지
                        nr = ii;
                    }
                }

                if(nr != i) {  // 예외처리
                    map[nr][j] = map[i][j];
                    map[i][j] = '.';
                }
            }
        }
    }

    public static int bfs(int startR, int startC) {
        int cnt = 1;

        Queue<Pair> que = new ArrayDeque<>();
        Queue<Pair> temp = new ArrayDeque<>();

        que.add(new Pair(startR, startC));
        check[startR][startC] = true;

        while(!que.isEmpty()) {
            Pair p = que.poll();
            temp.add(p);

            int r = p.getR();
            int c = p.getC();

            for(int i = 0; i < 4; i++) {
                int nr = r + rArr[i];
                int nc = c + cArr[i];

                if(!(-1 < nr && nr < N && -1 < nc && nc < M)) continue;
                if(check[nr][nc] || map[r][c] != map[nr][nc]) continue;

                cnt += 1;
                check[nr][nc] = true;
                que.add(new Pair(nr, nc));
            }

        }

        if(cnt >= 4) {
            while(!temp.isEmpty()) {
                Pair p = temp.poll();
                map[p.getR()][p.getC()] = '.';
            }
        }

        return cnt;
    }

    public static void process() {
        while(true) {
            boolean isValid = false;

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    char ch = map[i][j];
                    if (ch != '.' && !check[i][j]) {
                        int component = bfs(i, j);
                        if(component >= 4) isValid = true;
                    }
                }
            }

            // 초기화 및 map 재배치
            if(isValid) ans += 1;
            else break;
            check = new boolean[N][M];
            goDownPuyo();
        }
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = "";
        N = 12;
        M = 6;

        map = new char[N][M];
        check = new boolean[N][M];
        for(int i = 0; i < N; i++) {
            input = br.readLine();
            for(int j = 0; j < M; j++) {
                map[i][j] = input.charAt(j);
            }
        }

    }

    public static void output() {
        System.out.println(ans);
    }

    public static void main(String[] args) throws IOException {
        init();
        process();
        output();
    }
}
