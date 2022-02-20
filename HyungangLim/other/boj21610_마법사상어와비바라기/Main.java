package other.boj21610_마법사상어와비바라기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

class Pair {
    private int r, c;
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
class Order {
    private int d, s;
    Order(int d, int s) {
        this.d = d;
        this.s = s;
    }
    public int getD() {
        return this.d;
    }
    public int getS() {
        return this.s;
    }
}

public class Main {
    static int[][] map;
    static ArrayList<Order> orderList = new ArrayList<>();
    static ArrayList<Pair> clouds = new ArrayList<>();

    static int N, M;

    static int[] rArr = {0, 0, -1, -1, -1, 0, 1, 1, 1};  // 1부터 시작하기 위해 0, 0 추가
    static int[] cArr = {0, -1, -1, 0, 1, 1, 1, 0, -1};

    // 구름의 이동 후 좌표를 반환
    public static ArrayList<Pair> moveCloud(Order order) {
        ArrayList<Pair> result = new ArrayList<>();

        int d = order.getD();
        int s = order.getS();

        for(Pair p : clouds) {
            int nr = p.getR();
            int nc = p.getC();
            for(int i = 0; i < s; i++) {
                nr = nr + rArr[d];
                nc = nc + cArr[d];
                if(nr == N) nr = 0;
                if(nc == N) nc = 0;
                if(nr == -1) nr = N-1;
                if(nc == -1) nc = N-1;
            }
            result.add(new Pair(nr, nc));
        }

        return result;
    }

    public static void getRain(ArrayList<Pair> afterMove) {
        for(Pair p : afterMove) {
            int r = p.getR();
            int c = p.getC();
            map[r][c] += 1;
        }
    }

    public static void copyWaterBug(ArrayList<Pair> afterMove) {
        for(Pair p : afterMove) {
            int r = p.getR();
            int c = p.getC();

            // 대각 방향은 2, 4, 6, 8
            int cnt = 0;
            for(int i = 2; i <= 8; i+=2) {
                int nr = r + rArr[i];
                int nc = c + cArr[i];

                // 여기선 범위 넘어가지 않음
                if(!(-1 < nr && nr < N && -1 < nc && nc < N)) continue;
                if(map[nr][nc] > 0)
                    cnt += 1;
            }
            map[r][c] += cnt;
        }
    }

    public static void subtractWater(ArrayList<Pair> afterMove) {
        clouds.clear();
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                boolean isValid = true;
                if(map[i][j] >= 2) {
                    for(Pair p : afterMove) {
                        if(i == p.getR() && j == p.getC()) { // 이전 구름 좌표와 겹친다
                            isValid = false;
                            break;
                        }
                    }
                    if(isValid) {
                        map[i][j] -= 2;
                        clouds.add(new Pair(i, j));
                    }
                }
            }
        }
    }

    public static void process() {
        for(Order order : orderList) {
            ArrayList<Pair> afterMove = moveCloud(order);
            getRain(afterMove);
            copyWaterBug(afterMove);
            subtractWater(afterMove);
        }
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][N];
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            orderList.add(new Order(d, s));
        }

        // [N-2][0] [N-2][1]
        // [N-1][0] [N-1][1]
        clouds.add(new Pair(N-2, 0));
        clouds.add(new Pair(N-2, 1));
        clouds.add(new Pair(N-1, 0));
        clouds.add(new Pair(N-1, 1));
    }

    public static void output() {
        int ans = 0;
        for(int i = 0; i < N; i++) {
            ans += Arrays.stream(map[i]).sum();
        }
        System.out.println(ans);
    }

    public static void main(String[] args) throws IOException {
        init();
        process();
        output();
    }
}
