package baekjoon.bruteforce.boj2615;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 문제 좀 잘 읽자.. ㅜㅜ
 * 주의 1. 한 방향으로만 탐색 가능.
 * 주의 2. 6목 이상은 이긴 것이 아니다.
 *
 * 출력 타겟 좌표는 항상 양끝점
 * -> 끝점, 시작점 비교하여 winner 좌표 결정
 *
 * 맵 크기는 19*19로 고정,
 * 진행방향 총 8가지 경우
 * -> 19*19*8 브루트 포스 가능
 *
 * 질문 : check 배열 2차원으로도 가능?
 *
 * 19 19 체크배열 생성. 비트마스킹
 * 어지럽네..
 *
 *
 */


public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder sb;
    static int[][] map;
    static boolean[][][] check;
    static int[] rArr = {-1, 1, 0, 0, -1, -1, 1, 1};  // 대각선까지 체크
    static int[] cArr = {0, 0, -1, 1, 1, -1, -1, 1};

    static boolean isFinish = false;  // 승패 판결 여부
    static int winnerColor;
    static int winnerRow;
    static int winnerCol;

    // 이전 좌표에서 온 진행방향까지 받아야 한다
    public static void dfs(int color, int dept, int r, int c, int dir) {
        check[r][c][dir] = true;
        if(dept >= 5) {
            if(dept == 5) {
                isFinish = true;
                winnerColor = color;
                winnerRow = r;
                winnerCol = c;
                // 여기서 return 하면 안 됨. 6목 이상인지 검사 필요.
            }else {
                isFinish = false;
            }
        }

        int nr = r + rArr[dir];
        int nc = c + cArr[dir];
        if(!(-1 < nr && nr < 19 && -1 < nc && nc < 19)) return;
        if(map[nr][nc] != map[r][c] || check[nr][nc][dir]) return;
        dfs(color, dept+1, nr, nc, dir);

        // winner 좌표 체크
        if(dept == 1 && isFinish) {
            if(winnerCol != c) {
                if(winnerCol > c) {  // 1. 왼쪽 열
                    winnerRow = r;
                    winnerCol = c;
                }
            }else {
                if(winnerRow > r) {  // 2. 위쪽 행
                    winnerRow = r;
                    winnerCol = c;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();
        map = new int[19][19];  // 맵 크기는 고정
        check = new boolean[19][19][8];

        // input
        for(int i = 0; i < 19; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < 19; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 모든 좌표를 시작점으로 탐색 수행
        // dept 체크 위해서 DFS 사용
        for(int i = 0; i < 19; i++) {
            for(int j = 0; j < 19; j++) {
                for(int dir = 0; dir < 8; dir++) {
                    if(map[i][j] == 0 || check[i][j][dir]) continue;
                    dfs(map[i][j], 1, i, j, dir);

                    // 승패 체크
                    if(isFinish) {
                        sb.append(winnerColor + "\n");
                        sb.append(winnerRow+1).append(" ").append(winnerCol+1);
                        System.out.println(sb.toString());
                        return;
                    }
                }
            }
        }

        // 끝까지 판결 안 나면 무승부
        System.out.println(0);
    }
}
