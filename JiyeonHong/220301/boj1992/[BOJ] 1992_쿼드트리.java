package boj1992;

import java.io.*;

class Main {
    static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        board = new int[N][N];
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            for (int j = 0; j < str.length(); j++) {
                board[i][j] = (int) (str.charAt(j) - '0');
            }
        }

        divide(0, 0, N);

    }

    public static void divide(int is, int js, int N) {
        if (check(is, js, N)) {
            return;
        }

        System.out.print("(");
        divide(is, js, N / 2);
        divide(is, js + N / 2, N / 2);
        divide(is + N / 2, js, N / 2);
        divide(is + N / 2, js + N / 2, N / 2);
        System.out.print(")");
    }

    public static boolean check(int is, int js, int N) {
        int stat = board[is][js];
        for (int i = is; i < is + N; i++) {
            for (int j = js; j < js + N; j++) {
                if (stat != board[i][j])
                    return false;
            }
        }
        System.out.print(stat);
        return true;
    }
}
