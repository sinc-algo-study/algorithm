package other.boj19237_어른상어;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.StringTokenizer;

class Shark {
    int r, c, num, dir;
    Shark(int r, int c, int num) {
        this.r = r;
        this.c = c;
        this.num = num;
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

    public int getNum() {
        return num;
    }

    public int getDir() {
        return dir;
    }

    public void setDir(int dir) {
        this.dir = dir;
    }
}

class Smell {
    int num, time;
    Smell(int num, int time) {
        this.num = num;
        this.time = time;
    }

    public int getNum() {
        return num;
    }

    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }
}

public class Main {

    static ArrayList<Shark> sharkList = new ArrayList<>();
    static int[][] map;
    static Smell[][] smells;

    static int N, M, K, T, CNT;
    static int[][][] dArr;
    static int[] rArr = {-1, 1, 0, 0};
    static int[] cArr = {0, 0, -1, 1};

    public static void removeShark(int num) {
        for(int i = 0; i < M; i++) {
            Shark shark = sharkList.get(i);
            if(shark == null) continue;
            if(shark.getNum() == num) {
                sharkList.set(i, null);
            }
        }
    }

    public static void spraySmell() {
        for(Shark shark : sharkList) {
            if(shark == null) continue;
            int r = shark.getR();
            int c = shark.getC();
            int num = shark.getNum();
            smells[r][c] = new Smell(num, K);
        }
    }

    public static void moveShark() {
        for(Shark shark : sharkList) {
            if(shark == null) continue;

            int r = shark.getR();
            int c = shark.getC();
            int num = shark.getNum();
            int dir = shark.getDir();

            // 빈 칸
            boolean flag = false;
            for(int i = 0; i < 4; i++) {
                int nd = dArr[num - 1][dir][i];
                int nr = r + rArr[nd];
                int nc = c + cArr[nd];

                if(!(-1 < nr && nr < N && -1 < nc && nc < N)) continue;
                if(smells[nr][nc] != null) continue;

                // 다른 상어가 이동 전에 머무르는 칸은 고려할 필요 없음 ( 이미 다른 상어의 냄새가 뿌려져있기 떄문 )
                // 이미 도착한 상어가 있으면 나보다 강한 상어임 ( num 기준 오름차순 정렬함 )
                if(map[nr][nc] != 0) {
                    map[r][c] = 0;
                    CNT -= 1;
                    removeShark(num);
                }else {
                    map[r][c] = 0;
                    map[nr][nc] = num;
                    shark.setR(nr);
                    shark.setC(nc);
                    shark.setDir(nd);
                }
                flag = true;
                break;
            }

            if(flag) continue;

            // 내 냄새가 있는 칸
            for(int i = 0; i < 4; i++) {
                int nd = dArr[num - 1][dir][i];
                int nr = r + rArr[nd];
                int nc = c + cArr[nd];

                if(!(-1 < nr && nr < N && -1 < nc && nc < N)) continue;
                if(smells[nr][nc] == null) continue;
                if(smells[nr][nc].getNum() != num) continue;

                map[r][c] = 0;
                map[nr][nc] = num;
                shark.setR(nr);
                shark.setC(nc);
                shark.setDir(nd);
                break;
            }
        }
    }

    public static void reduceSmell() {
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < N; j++) {
                if(smells[i][j] == null) continue;
                if(smells[i][j].getTime() == 1) {
                    smells[i][j] = null;
                    continue;
                }
                Smell smell = smells[i][j];
                smell.setTime(smell.getTime() - 1);
            }
        }
    }

    public static void process() {
        while(CNT > 1) {
            if(T >= 1000) {
                T = -1;
                break;
            }

            spraySmell();
            moveShark();
            reduceSmell();

            T += 1;
        }
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        CNT = M;

        map = new int[N][N];
        smells = new Smell[N][N];
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) {
                int num = Integer.parseInt(st.nextToken());
                if(num != 0) {
                    map[i][j] = num;
                    sharkList.add(new Shark(i, j, num));
                }
            }
        }

        Collections.sort(sharkList, new Comparator<Shark>() {
            @Override
            public int compare(Shark o1, Shark o2) {
                return o1.num - o2.num;
            }
        });
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < M; i++) {
            int dir = Integer.parseInt(st.nextToken()) - 1;
            sharkList.get(i).setDir(dir);
        }

        dArr = new int[M][4][4];
        for(int i = 0; i < M; i++) {
            for(int j = 0; j < 4; j++) {
                st = new StringTokenizer(br.readLine());
                for(int k = 0; k < 4; k++) {
                    int dir = Integer.parseInt(st.nextToken()) - 1;
                    dArr[i][j][k] = dir;
                }
            }
        }
    }

    public static void output() {
        System.out.println(T);
    }

    public static void main(String[] args) throws IOException {
        init();
        process();
        output();
    }
}
