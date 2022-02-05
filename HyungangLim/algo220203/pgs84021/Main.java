package algo220203.pgs84021;

import java.util.*;

class Pair {
    int r, c;
    Pair(int r, int c) {
        this.r = r;
        this.c = c;
    }
}

class Solution {
    Map<String, Integer> hm;
    ArrayList<Pair> pairs;
    boolean[][] check;
    int[] rArr = {-1, 1, 0, 0};
    int[] cArr = {0, 0, -1, 1};
    int len;

    public int[][] rotateTable(int[][] table) {
        int[][] result = new int[len][len];
        for(int i = 0; i < len; i++) {
            for(int j = 0; j < len; j++) {
                result[j][len - i - 1] = table[i][j];
            }
        }
        return result;
    }

    public String puzzleToStrig(int[][] arr) {
        int minR = 50, minC = 50;
        int maxR = -1, maxC = -1;
        for(Pair p : pairs) {
            minR = Math.min(minR, p.r);
            minC = Math.min(minC, p.c);
            maxR = Math.max(maxR, p.r);
            maxC = Math.max(maxC, p.c);
        }

        StringBuilder sb = new StringBuilder();
        for(int i = minR; i <= maxR; i++) {
            for(int j = minC; j <= maxC; j++) {
                sb.append(arr[i][j] == 0 ? "0" : "1");
            }
            sb.append("n\n");
        }
        return sb.toString();
    }

    public String[] bfs(int r, int c, int[][] arr) {
        Queue<Pair> que = new ArrayDeque<>();
        pairs = new ArrayList<>();
        Pair pair = new Pair(r, c);
        que.add(pair);
        pairs.add(pair);
        check[r][c] = true;

        int size = 1;
        while(!que.isEmpty()) {
            Pair p = que.poll();

            for(int i = 0; i < 4; i++) {
                int nr = p.r + rArr[i];
                int nc = p.c + cArr[i];

                if(!(-1 < nr && nr < len && -1 < nc && nc < len)) continue;
                if(check[nr][nc] || arr[nr][nc] != 1) continue;

                check[nr][nc] = true;
                Pair np = new Pair(nr, nc);
                que.add(np);
                pairs.add(np);
                size += 1;
            }
        }

        return new String[]{puzzleToStrig(arr), String.valueOf(size)};
    }

    public int solution(int[][] game_board, int[][] table) {
        len = game_board.length;
        hm = new HashMap<>();

        for(int i = 0; i < len; i++) {
            for(int j = 0; j < len; j++) {
                game_board[i][j] = game_board[i][j] == 0 ? 1 : 0;
            }
        }

        check = new boolean[len][len];
        for(int i = 0; i < len; i++) {
            for(int j = 0; j < len; j++) {
                if(!check[i][j] && game_board[i][j] == 1) {
                    String key = bfs(i, j, game_board)[0];
                    if(hm.containsKey(key)) {
                        hm.put(key, hm.get(key) + 1);
                    }else {
                        hm.put(key, 1);
                    }
                }
            }
        }

        int answer = 0;
        for(int rotate = 0; rotate < 4; rotate++) {
            table = rotateTable(table);
            check = new boolean[len][len];

            for(int i = 0; i < len; i++) {
                for(int j = 0; j < len; j++) {
                    if(!check[i][j] && table[i][j] == 1) {
                        String[] arr = bfs(i, j, table);
                        if(hm.containsKey(arr[0])) {
                            hm.put(arr[0], hm.get(arr[0]) - 1);
                            answer += Integer.parseInt(arr[1]);

                            if(hm.get(arr[0]) == 0) hm.remove(arr[0]);
                            for(Pair p : pairs) table[p.r][p.c] = 0;
                        }
                    }
                }
            }
        }


        return answer;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] game_board = {{1, 1, 0, 0, 1, 0}, {0, 0, 1, 0, 1, 0},
                {0, 1, 1, 0, 0, 1}, {1, 1, 0, 1, 1, 1},
                {1, 0, 0, 0, 1, 0}, {0, 1, 1, 1, 0, 0}};
        int[][] table = {{1, 0, 0, 1, 1, 0}, {1, 0, 1, 0, 1, 0},
                {0, 1, 1, 0, 1, 1}, {0, 0, 1, 0, 0, 0},
                {1, 1, 0, 1, 1, 0}, {0, 1, 0, 0, 0, 0}};
        int ans = sol.solution(game_board, table);
        System.out.println(ans);
    }
}
