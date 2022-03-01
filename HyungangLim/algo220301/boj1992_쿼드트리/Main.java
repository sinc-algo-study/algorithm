package algo220301.boj1992_쿼드트리;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * map을 4등분 해야함
 */

public class Main {
    static StringBuilder sb;
    static int N;
    static int[][] map;

    public static boolean isPossible(int r, int c, int size) {
        int target = map[r][c];
        for(int i = r; i < r + size; i++) {
            for(int j = c; j < c + size; j++) {
                if(map[i][j] != target) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void divideAndConquer(int r, int c, int size) {
        // 네개의 시작점
        // (r, c), (r, c + size/2)
        // (r + size/2, c),  (r + size/2, c + size/2)

        if(isPossible(r, c, size)) {
            sb.append(String.valueOf(map[r][c]));
        }else {
            sb.append("(");
            int half = size / 2;
            divideAndConquer(r, c, half);
            divideAndConquer(r, c + half, half);
            divideAndConquer(r + half, c, half);
            divideAndConquer(r + half, c + half, half);
            sb.append(")");
        }
    }

    public static void process() {
        sb = new StringBuilder();
        divideAndConquer(1, 1, N);
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new int[N+1][N+1];

        for(int i = 1; i <= N; i++) {
            String input = br.readLine();
            for(int j = 1; j <= N; j++) {
                map[i][j] = input.charAt(j-1) - '0';
            }
        }
    }

    public static void output() {
        System.out.println(sb.toString());
    }

    public static void main(String[] args) throws IOException {
        init();
        process();
        output();
    }
}
