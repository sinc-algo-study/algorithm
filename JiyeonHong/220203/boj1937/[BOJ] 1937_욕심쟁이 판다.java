package boj1937;

import java.io.*;

/*
우상단부터 시작해서 상하좌우로 움직이면서
이전칸 대나무<다음칸 대나무면 dfs로 이동
이동하면서 각 칸의 최대 이동수 dp에 저장
-> 시간초과....
-> 이동해서 dp에다가 값 저장하니 결국 메모이제이션이 아니게 되버림

1. (0,0) 부터 시작 
2. dfs로 탐색하다가 갈 곳이 없으면 원래 처음 시작함수로 return 되니까
    dp[r][c]=(r,c)점을 시작점으로 했을때 최대 이동가능한 칸 수로 설정

ex.forest          dp                                (3>2이니까)  
14 9 12 10          1 0 0 0         1 3 0 0         1 3 1 0
1 11 5 4            0 0 0 0         0 2 0 0         0 2 0 0
7 15 2 13           0 0 0 0    ->   0 1 0 0   ->    0 1 0 0
6 3 16 8            0 0 0 0         0 0 0 0         0 0 0 0
*/
class Solution {
    // 상, 하, 좌, 우
    int[][] dir = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
    int[][] dp; // dp[r][c]=(r,c)점을 시작점으로 했을 때 최대 이동 칸 수

    public int solution(int[][] forest) {
        int answer = 0;
        dp = new int[forest.length][forest.length];
        for (int r = 0; r < forest.length; r++) {
            for (int c = 0; c < forest.length; c++) {
                move(forest, r, c);
            }
        }

        for (int r = 0; r < forest.length; r++) {
            for (int c = 0; c < forest.length; c++) {
                answer = Math.max(answer, dp[r][c]);
            }
        }
        return answer;
    }

    public int move(int[][] forest, int r, int c) {
        if (dp[r][c] != 0) {
            return dp[r][c];
        }

        dp[r][c] = 1;
        for (int i = 0; i < dir.length; i++) {
            int nr = r + dir[i][0];
            int nc = c + dir[i][1];
            if (nr < 0 || nr >= forest.length || nc < 0 || nc >= forest.length) {
                continue;
            }

            if (forest[nr][nc] > forest[r][c]) { // 다음 칸 대나무 수>이전 칸 대나무 수
                dp[r][c] = Math.max(dp[r][c], move(forest, nr, nc) + 1);
            }
        }
        return dp[r][c];
    }

}

class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] forest = new int[n][n];

        for (int i = 0; i < n; i++) {
            String[] str = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                forest[i][j] = Integer.parseInt(str[j]);
            }
        }

        Solution s = new Solution();
        System.out.println(s.solution(forest));
    }
}