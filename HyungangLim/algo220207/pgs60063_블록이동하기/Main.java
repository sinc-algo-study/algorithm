package algo220207.pgs60063_블록이동하기;

import java.util.ArrayDeque;
import java.util.Queue;

/**
 *
 * 미완성
 *
 */

class Status {
    int r1, c1, d1;
    int r2, c2, d2;
    int cost;
    Status(int r1, int c1, int d1,
         int r2, int c2, int d2, int cost) {
        this.r1 = r1;
        this.c1 = c1;
        this.d1 = d1;
        this.r2 = r2;
        this.c2 = c2;
        this.d2 = d2;
        this.cost = cost;
    }
}

class Solution {
    int[][] map;
    boolean[][][] check;  // [r][c][d] -> d : {상, 하, 좌, 우}
    int[] rArr = {-1, 1, 0, 0};
    int[] cArr = {0, 0, -1, 1};
    int len, answer;

    public void bfs(int sr1, int sc1, int sd1,    // start row, col, dir
                    int sr2, int sc2, int sd2) {
        Queue<Status> que = new ArrayDeque<>();
        que.add(new Status(sr1, sc1, sd1, sr2, sc2, sd2, 0));
        check[sr1][sc1][sd1] = true;
        check[sr2][sc2][sd2] = true;

        while(!que.isEmpty()) {
            Status s = que.poll();
            int cost = s.cost;
            int r1 = s.r1, c1 = s.c1, d1 = s.d1;
            int r2 = s.r2, c2 = s.c2, d2 = s.d2;

            // 둘 중 한 점이라도 도착했으면 도착한 것
            if((r1 == len - 1 && c1 == len - 1) || (r2 == len - 1 && c2 == len - 1)) {
                this.answer = s.cost;
                return;
            }

            // 상하좌우 이동
            for(int i = 0; i < 4; i++) {
                int nr1 = r1 + rArr[i], nr2 = r2 + rArr[i];
                int nc1 = c1 + cArr[i], nc2 = c2 + cArr[i];

                if(!(-1 < nr1 && nr1 < len && -1 < nc1 && nc1 < len)) continue;
                if(!(-1 < nr2 && nr2 < len && -1 < nc2 && nc2 < len)) continue;
                if(check[nr1][nc1][d1] || check[nr2][nc2][d2] ||
                        map[nr1][nc1] == 1 || map[nr2][nc2] == 1) continue;  // 사실 [nr2][nc2][d2]는 안 봐도 된다

                check[nr1][nc1][d1] = true;
                check[nr2][nc2][d2] = true;
                que.add(new Status(nr1, nc1, d1, nr2, nc2, d2, cost + 1));
            }

            // 회전은 총 네가지 경우
            // 1. 로봇은 세로방향, [r1][c1]가 아래점 -> [r2][c2]를 [r1][c1]의 양옆에 놓는다
            // 2. 로봇은 세로방향, [r1][c1]가 윗점 -> [r2][c2]를 [r1][c1]의 양옆에 놓는다
            // 3. 로봇은 가로방향, [r1][c1]가 오른점 -> [r2][c2]를 [r1][c1]의 위아래에 놓는다
            // 4. 로봇은 가로방향, [r1][c1]가 왼점 -> [r2][c2]를 [r1][c1]의 위아래에 놓는다
            // -> 회전만 메서드로 따로 뽑자

            // 1. 로봇은 세로방향, [r1][c1]가 아래점
            if(d1 == 0) {
                // 윗점 [r2][c2]를 [r1][c1]의 왼쪽에 놓기
                int nr2 = r1 + rArr[2], nc2 = c1 + cArr[2];  // next row, col
                int pr = nr2 + rArr[0], pc = nc2 + cArr[0];  // path row, col
                if(-1 < nr2 && nr2 < len && -1 < nc2 && nc2 < len &&
                        -1 < pr && pr < len && -1 < pc && pc < len &&   // pr은 검사 안 해도 될 거 같긴 한데 그냥 하자
                        !check[r1][c1][2] && !check[nr2][nc2][3] &&
                        map[nr2][nc2] == 0 && map[pr][pc] == 0) {
                    check[r1][c1][2] = true;
                    check[nr2][nc2][3] = true;
                    que.add(new Status(r1, c1, 2, nr2, nc2, 3, cost + 1));
                }

                // 윗점 [r2][c2]를 [r1][c1]의 오른쪽에 놓기
                nr2 = r1 + rArr[3]; nc2 = c1 + cArr[3];
                pr = nr2 + rArr[0]; pc = nc2 + cArr[0];
                if(-1 < nr2 && nr2 < len && -1 < nc2 && nc2 < len &&
                        -1 < pr && pr < len && -1 < pc && pc < len &&
                        !check[r1][c1][3] && !check[nr2][nc2][2] &&
                        map[nr2][nc2] == 0 && map[pr][pc] == 0) {
                    check[r1][c1][3] = true;
                    check[nr2][nc2][2] = true;
                    que.add(new Status(r1, c1, 3, nr2, nc2, 2, cost + 1));
                }
                
                // 아랫점 [r1][c1]을 [r2][c2]의 왼쪽에 놓기
                int nr1 = r2 + rArr[2], nc1 = c2 + cArr[2];
                pr = nr1 + rArr[1]; pr = nc1 + cArr[1];
                if(-1 < nr1 && nr1 < len && -1 < nc1 && nc1 < len &&
                        -1 < pr && pr < len && -1 < pc && pc < len &&
                        !check[r2][c2][2] && !check[nr1][nc1][3] &&
                        map[nr1][nc1] == 0 && map[pr][pc] == 0) {
                    check[r2][c2][2] = true;
                    check[nr1][nc1][3] = true;
                    que.add(new Status(r2, c2, 2, nr1, nc1, 3, cost + 1));
                }

                // 아랫점 [r1][c1]을 [r2][c2]의 오른쪽에 놓기
                nr1 = r2 + rArr[3]; nc1 = c2 + cArr[3];
                pr = nr1 + rArr[1]; pr = nc1 + cArr[1];
                if(-1 < nr1 && nr1 < len && -1 < nc1 && nc1 < len &&
                        -1 < pr && pr < len && -1 < pc && pc < len &&
                        !check[r2][c2][3] && !check[nr1][nc1][2] &&
                        map[nr1][nc1] == 0 && map[pr][pc] == 0) {
                    check[r2][c2][3] = true;
                    check[nr1][nc1][2] = true;
                    que.add(new Status(r2, c2, 3, nr1, nc1, 2, cost + 1));
                }
            }

            // 2. 로봇은 세로방향, [r1][c1]가 윗점
            if (d1 == 1) {
                // 아래점 [r2][c2]를 [r1][c1]의 왼쪽에 놓기
                int nr2 = r1 + rArr[2], nc2 = c1 + cArr[2];
                int pr = nr2 + rArr[1], pc = nc2 + cArr[1];
                if(-1 < nr2 && nr2 < len && -1 < nc2 && nc2 < len &&
                        -1 < pr && pr < len && -1 < pc && pc < len &&
                        !check[r1][c1][2] && !check[nr2][nc2][3] &&
                        map[nr2][nc2] == 0 && map[pr][pc] == 0) {
                    check[r1][c1][2] = true;
                    check[nr2][nc2][3] = true;
                    que.add(new Status(r1, c1, 2, nr2, nc2, 3, cost + 1));
                }

                // 아래점 [r2][c2]를 [r1][c1]의 오른쪽에 놓기
                nr2 = r1 + rArr[3]; nc2 = c1 + cArr[3];
                pr = nr2 + rArr[1]; pc = nc2 + cArr[1];
                if(-1 < nr2 && nr2 < len && -1 < nc2 && nc2 < len &&
                        -1 < pr && pr < len && -1 < pc && pc < len &&
                        !check[r1][c1][3] && !check[nr2][nc2][2] &&
                        map[nr2][nc2] == 0 && map[pr][pc] == 0) {
                    check[r1][c1][3] = true;
                    check[nr2][nc2][2] = true;
                    que.add(new Status(r1, c1, 3, nr2, nc2, 2, cost + 1));
                }

                // 윗점 [r1][c1]을 [r2][c2]의 왼쪽에 놓기
                int nr1 = r2 + rArr[2], nc1 = c2 + cArr[2];
                pr = nr1 + rArr[0]; pr = nc1 + cArr[0];
                if(-1 < nr1 && nr1 < len && -1 < nc1 && nc1 < len &&
                        -1 < pr && pr < len && -1 < pc && pc < len &&
                        !check[r2][c2][2] && !check[nr1][nc1][3] &&
                        map[nr1][nc1] == 0 && map[pr][pc] == 0) {
                    check[r2][c2][2] = true;
                    check[nr1][nc1][3] = true;
                    que.add(new Status(r2, c2, 2, nr1, nc1, 3, cost + 1));
                }

                // 윗점 [r1][c1]을 [r2][c2]의 오른쪽에 놓기
                nr1 = r2 + rArr[3]; nc1 = c2 + cArr[3];
                pr = nr1 + rArr[0]; pr = nc1 + cArr[0];
                if(-1 < nr1 && nr1 < len && -1 < nc1 && nc1 < len &&
                        -1 < pr && pr < len && -1 < pc && pc < len &&
                        !check[r2][c2][3] && !check[nr1][nc1][2] &&
                        map[nr1][nc1] == 0 && map[pr][pc] == 0) {
                    check[r2][c2][3] = true;
                    check[nr1][nc1][2] = true;
                    que.add(new Status(r2, c2, 3, nr1, nc1, 2, cost + 1));
                }
            }
            
            // 3. 로봇은 가로방향, [r1][c1]가 오른점
            if (d1 == 2) {
                // 왼점 [r2][c2]를 [r1][c1]의 위쪽에 놓기
                int nr2 = r1 + rArr[0], nc2 = c1 + cArr[0];
                int pr = nr2 + rArr[2], pc = nc2 + cArr[2];
                if(-1 < nr2 && nr2 < len && -1 < nc2 && nc2 < len &&
                        -1 < pr && pr < len && -1 < pc && pc < len &&
                        !check[r1][c1][0] && !check[nr2][nc2][1] &&
                        map[nr2][nc2] == 0 && map[pr][pc] == 0) {
                    check[r1][c1][0] = true;
                    check[nr2][nc2][1] = true;
                    que.add(new Status(r1, c1, 0, nr2, nc2, 1, cost + 1));
                }

                // 왼점 [r2][c2]를 [r1][c1]의 아래쪽에 놓기
                nr2 = r1 + rArr[1]; nc2 = c1 + cArr[1];
                pr = nr2 + rArr[2]; pc = nc2 + cArr[2];
                if(-1 < nr2 && nr2 < len && -1 < nc2 && nc2 < len &&
                        -1 < pr && pr < len && -1 < pc && pc < len &&
                        !check[r1][c1][1] && !check[nr2][nc2][0] &&
                        map[nr2][nc2] == 0 && map[pr][pc] == 0) {
                    check[r1][c1][1] = true;
                    check[nr2][nc2][0] = true;
                    que.add(new Status(r1, c1, 1, nr2, nc2, 0, cost + 1));
                }
                
                // 오른점 [r1][c1]을 [r2][c2]의 위쪽에 놓기
                int nr1 = r2 + rArr[1], nc1 = c2 + cArr[1];
                pr = nr1 + rArr[3]; pr = nc1 + cArr[3];
                if(-1 < nr1 && nr1 < len && -1 < nc1 && nc1 < len &&
                        -1 < pr && pr < len && -1 < pc && pc < len &&
                        !check[r2][c2][0] && !check[nr1][nc1][1] &&
                        map[nr1][nc1] == 0 && map[pr][pc] == 0) {
                    check[r2][c2][0] = true;
                    check[nr1][nc1][1] = true;
                    que.add(new Status(r2, c2, 0, nr1, nc1, 1, cost + 1));
                }

                // 오른점 [r1][c1]을 [r2][c2]의 아래쪽에 놓기
                nr1 = r2 + rArr[1]; nc1 = c2 + cArr[1];
                pr = nr1 + rArr[3]; pr = nc1 + cArr[3];
                if(-1 < nr1 && nr1 < len && -1 < nc1 && nc1 < len &&
                        -1 < pr && pr < len && -1 < pc && pc < len &&
                        !check[r2][c2][1] && !check[nr1][nc1][0] &&
                        map[nr1][nc1] == 0 && map[pr][pc] == 0) {
                    check[r2][c2][1] = true;
                    check[nr1][nc1][0] = true;
                    que.add(new Status(r2, c2, 1, nr1, nc1, 0, cost + 1));
                }
            }

            // 4. 로봇은 가로방향, [r1][c1]가 왼점
            if (d1 == 3) {
                // 오른점 [r2][c2]를 [r1][c1]의 위쪽에 놓기
                int nr2 = r1 + rArr[0], nc2 = c1 + cArr[0];
                int pr = nr2 + rArr[3], pc = nc2 + cArr[3];
                if(-1 < nr2 && nr2 < len && -1 < nc2 && nc2 < len &&
                        -1 < pr && pr < len && -1 < pc && pc < len &&
                        !check[r1][c1][0] && !check[nr2][nc2][1] &&
                        map[nr2][nc2] == 0 && map[pr][pc] == 0) {
                    check[r1][c1][0] = true;
                    check[nr2][nc2][1] = true;
                    que.add(new Status(r1, c1, 0, nr2, nc2, 1, cost + 1));
                }

                // 오른점 [r2][c2]를 [r1][c1]의 아래쪽에 놓기
                nr2 = r1 + rArr[1]; nc2 = c1 + cArr[1];
                pr = nr2 + rArr[3]; pc = nc2 + cArr[3];
                if(-1 < nr2 && nr2 < len && -1 < nc2 && nc2 < len &&
                        -1 < pr && pr < len && -1 < pc && pc < len &&
                        !check[r1][c1][1] && !check[nr2][nc2][0] &&
                        map[nr2][nc2] == 0 && map[pr][pc] == 0) {
                    check[r1][c1][1] = true;
                    check[nr2][nc2][0] = true;
                    que.add(new Status(r1, c1, 1, nr2, nc2, 0, cost + 1));
                }
                
                // 왼점 [r1][c1]을 [r2][c2]의 위쪽에 놓기
                int nr1 = r2 + rArr[0], nc1 = c2 + cArr[0];
                pr = nr1 + rArr[2]; pr = nc1 + cArr[2];
                if(-1 < nr1 && nr1 < len && -1 < nc1 && nc1 < len &&
                        -1 < pr && pr < len && -1 < pc && pc < len &&
                        !check[r2][c2][0] && !check[nr1][nc1][1] &&
                        map[nr1][nc1] == 0 && map[pr][pc] == 0) {
                    check[r2][c2][0] = true;
                    check[nr1][nc1][1] = true;
                    que.add(new Status(r2, c2, 0, nr1, nc1, 1, cost + 1));
                }
                
                // 왼점 [r1][c1]을 [r2][c2]의 아래쪽에 놓기
                nr1 = r2 + rArr[1]; nc1 = c2 + cArr[1];
                pr = nr1 + rArr[2]; pr = nc1 + cArr[2];
                if(-1 < nr1 && nr1 < len && -1 < nc1 && nc1 < len &&
                        -1 < pr && pr < len && -1 < pc && pc < len &&
                        !check[r2][c2][1] && !check[nr1][nc1][0] &&
                        map[nr1][nc1] == 0 && map[pr][pc] == 0) {
                    check[r2][c2][1] = true;
                    check[nr1][nc1][0] = true;
                    que.add(new Status(r2, c2, 1, nr1, nc1, 0, cost + 1));
                }
            }
        }
    }


    public int solution(int[][] board) {
        len = board.length;
        map = board;
        check = new boolean[len][len][4];

        bfs(0, 0, 3, 0, 1, 2);

        return answer;
    }
}

public class Main {
    public static void main(String[] args) {
//        String input = "[[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]";
//        input = input.replace('[', '{');
//        input = input.replace(']', '}');
//        System.out.println(input);

        Solution sol = new Solution();
        int[][] board = {{0, 0, 0, 0, 0, 0, 1}, {1, 1, 1, 1, 0, 0, 1}, {0, 0, 0, 0, 0, 0, 0}, {0, 0, 1, 1, 1, 1, 0}, {0, 1, 1, 1, 1, 1, 0}, {0, 0, 0, 0, 0, 1, 1}, {0, 0, 1, 0, 0, 0, 0}};

        int ans = sol.solution(board);
        System.out.println(ans);
    }
}
