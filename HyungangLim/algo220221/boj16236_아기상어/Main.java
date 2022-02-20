package algo220221.boj16236_아기상어;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 *
 * (물고기 잡아먹는 기준)
 * 1. 거리
 * 2. 위치
 *   - 위쪽 행
 *   - 왼쪽 열
 *
 * 1. 모든 칸에 대해 BFS를 돌면서 모든 물고기들의 정보를 파악한다
 * (크기, 거리, 위치)
 * 2. 기준에 따라 우선순위대로 물고기를 먹는다
 * 3. 먹을 수 없으면 종료
 *
 * (참고)
 * 1. 소요시간은 모든 BFS에서 누적하여 관리해야함
 * 2. eatable fish 를 찾은 후엔 바로 bfs 탈출해도 되지만 N 제한이 작으므로 그냥 구현
 *
 */

class Pair {
    int r, c, dept;
    Pair(int r, int c, int dept) {
        this.r = r;
        this.c = c;
        this.dept = dept;
    }

    public int getR() {
        return r;
    }
    public int getC() {
        return c;
    }
    public int getDept() {
        return dept;
    }
}

class Fish implements Comparable<Fish> {
    int r, c, dist;
    Fish(int r, int c, int dist) {
        this.r = r;
        this.c = c;
        this.dist = dist;
    }
    @Override
    public int compareTo(Fish o) {
        if(this.dist != o.dist) return this.dist - o.dist;
        if(this.r != o.r) return this.r - o.r;
        return this.c - o.c;
    }
    public int getR() {
        return r;
    }
    public void setR(int r) {
        this.r = r;
    }
    public int getC() {
        return c;
    }
    public void setC(int c) {
        this.c = c;
    }
    public int getDist() {
        return dist;
    }
}

public class Main {

    static PriorityQueue<Fish> fishHeap = new PriorityQueue<>();
    static Fish shark;
    static boolean[][] check;
    static int[][] map;
    static int[] rArr = {-1, 1, 0, 0};
    static int[] cArr = {0, 0, -1, 1};
    static int N, TIME, CNT, sharkVal = 2;

    public static void bfs(int startR, int startC) {
        Queue<Pair> que = new ArrayDeque<>();
        que.add(new Pair(startR, startC, 0));
        check[startR][startC] = true;

        while(!que.isEmpty()) {
            Pair p = que.poll();
            int r = p.getR();
            int c = p.getC();
            int d = p.getDept();

            for(int i = 0; i < 4; i++) {
                int nr = r + rArr[i];
                int nc = c + cArr[i];

                if(!(-1 < nr && nr < N && -1 < nc && nc < N)) continue;
                if(check[nr][nc] || map[nr][nc] > sharkVal) continue;

                que.add(new Pair(nr, nc, d + 1));
                check[nr][nc] = true;
                if(map[nr][nc] != 0 && map[nr][nc] < sharkVal) {
                    fishHeap.add(new Fish(nr, nc, d + 1));
                }
            }
        }

        que.clear();
    }

    public static void eatFish(Fish fish) {
        int sr = shark.getR();
        int sc = shark.getC();
        int fr = fish.getR();
        int fc = fish.getC();

        map[sr][sc] = 0;
        map[fr][fc] = 9;
        TIME += fish.getDist();
        CNT += 1;

        if(CNT == sharkVal) {
            sharkVal += 1;
            CNT = 0;
        }
        shark.setR(fr);
        shark.setC(fc);
        fishHeap.clear();
        check = new boolean[N][N];
    }

    public static void process() {
        while(true) {
            bfs(shark.getR(), shark.getC());
            if(fishHeap.isEmpty()) break;
            eatFish(fishHeap.poll());
        }
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        map = new int[N][N];
        check = new boolean[N][N];
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if(map[i][j] == 9)
                    shark = new Fish(i, j, 0);
            }
        }
    }

    public static void output() {
        System.out.println(TIME);
    }

    public static void main(String[] args) throws IOException {
        init();
        process();
        output();
    }
}
