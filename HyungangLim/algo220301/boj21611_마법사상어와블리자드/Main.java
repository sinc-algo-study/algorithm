package algo220301.boj21611_마법사상어와블리자드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

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

    static int N, M, SR, SC;
    static int[][] arr;
    static Queue<Integer> que;
    static Deque<Pair> bombPairDeq;
    static int[] rArr = {0, -1, 1, 0, 0};
    static int[] cArr = {0, 0, 0, -1, 1};
    static int[] dArr, sArr;

    static int marble, cnt;
    static int oneCnt, twoCnt, threeCnt;
    static boolean bombStop, changeStop;

    public static void searchArr(int r, int c, int d, int len, int inst) {
        int nr = r, nc = c;
        for(int i = 0; i < len; i++) {
            nr += rArr[d];
            nc += cArr[d];

            if(!(1 <= nr && nr <= N && 1 <= nc && nc <= N)) continue;

            if(inst == 1) {     // arr to que
                if(arr[nr][nc] != 0) {
                    que.add(arr[nr][nc]);
                }
            }

            if(inst == 2) {     // que to arr
                if(que.isEmpty()) return;
                arr[nr][nc] = que.poll();
            }

            if(inst == 3) {     // 폭파 시킬 구슬의 좌표 저장
                // marble : 이전까지 체크되어왔던 구슬 번호
                // cnt : 이전까지 연속되어온 marble 의 개수

                if(arr[nr][nc] == marble) {  // 일치하면 일단 폭파 후보이므로 좌표 저장
                    bombPairDeq.addLast(new Pair(nr, nc));
                    cnt += 1;
                }else {
                    if(cnt < 4) {  // 4개 미만
                        // 4개 미만이므로 지금까지 쌓아온 좌표들 제거
                        for(int j = 0; j < cnt; j++) {
                            bombPairDeq.pollLast();
                        }
                    }

                    if(arr[nr][nc] == 0) {  // 다 당겨놨기 때문에 0이 나왔다면 더이상 진행 불필요
                        bombStop = true;
                        return;
                    }

                    bombPairDeq.addLast(new Pair(nr, nc));
                    marble = arr[nr][nc];
                    cnt = 1;  // 연속된 구슬 개수 초기화
                }
            }

            if(inst == 4) {
                // marble : 이전까지 체크되어왔던 구슬 번호
                // cnt : 이전까지 연속되어온 marble 의 개수

                if(arr[nr][nc] == marble) {
                    cnt += 1;  // 그룹을 구성하는 구슬 개수 센다
                }else {        // 다른 그룹으로 넘어감
                    if(marble != 4) {    // 최초 상어 칸에 대한 예외처리
                        que.add(cnt);
                        que.add(marble);
                    }

                    if(arr[nr][nc] == 0) {  // 다 당겨놨기 때문에 0이 나왔다면 더이상 진행 불필요
                        changeStop = true;
                        return;
                    }

                    // 새로운 그룹을 위해 초기화
                    marble = arr[nr][nc];
                    cnt = 1;
                }
            }
        }
    }

    public static void doInstruction(int inst) {
        // inst 1 : convert arr to que (구슬 이동)
        // inst 2 : convert que to arr (구슬 이동)
        // inst 3 : check explodable marble's pairs (구슬 폭파)
        // inst 4 : convert arr to que (구슬 변형)

        if(inst == 1) {
            que.clear();
        }
        if(inst == 2) {
            arr = new int[N+1][N+1];
            arr[SR][SC] = 4;  // 상어는 연속구슬 체크에서 벗어나도록 존재하지 않는 구슬 값을 준다
        }
        if(inst == 3) {
            bombPairDeq.clear();
            marble = 4;  // 최초 구슬은 상어칸이므로 포함되면 안 된다
            cnt = 1;
            bombStop = false;
        }
        if(inst == 4) {
            que.clear();
            marble = 4;
            cnt = 1;
            changeStop = false;
        }

        int len = 1;
        int nr = SR, nc = SC;

        while(true) {
            searchArr(nr, nc, 3, len, inst);
            if(inst == 3 && bombStop) break;
            if(inst == 4 && changeStop) break;
            nr += rArr[3] * len;
            nc += cArr[3] * len;

            // 범위를 벗어났다면 종료
            // 종료는 반드시 좌 이동 후
            if (!(1 <= nr && nr <= N && 1 <= nc && nc < N)) break;

            searchArr(nr, nc, 2, len, inst);
            if(inst == 3 && bombStop) break;
            if(inst == 4 && changeStop) break;
            nr += rArr[2] * len;
            nc += cArr[2] * len;

            len += 1;

            searchArr(nr, nc, 4, len, inst);
            if(inst == 3 && bombStop) break;
            if(inst == 4 && changeStop) break;
            nr += rArr[4] * len;
            nc += cArr[4] * len;

            searchArr(nr, nc, 1, len, inst);
            if(inst == 3 && bombStop) break;
            if(inst == 4 && changeStop) break;
            nr += rArr[1] * len;
            nc += cArr[1] * len;

            len += 1;
        }
    }

    public static void changeMarble() {
        // 더이상 폭파할 구슬이 없으면 구슬 변형 진행
        // 변형 될 예정인 모양으로 array to queue 진행
        doInstruction(4);

        // 변형된 모양의 que 에서 다시 queue to array
        doInstruction(2);
    }

    public static void bombMarble() {
        doInstruction(3);  // 폭파 가능 구슬 체크
        while(!bombPairDeq.isEmpty()) {  // 폭파된 구슬이 있는가? 없는가?

            while(!bombPairDeq.isEmpty()) {  // 전부 폭파
                Pair p = bombPairDeq.pollFirst();
                int r = p.getR();
                int c = p.getC();

                if(arr[r][c] == 1) oneCnt += 1;
                if(arr[r][c] == 2) twoCnt += 1;
                if(arr[r][c] == 3) threeCnt += 1;

                arr[r][c] = 0;
            }

            moveMarble();      // 폭파가 진행됐다면 구슬 이동 필요
            doInstruction(3);  // 폭파 가능 구슬 체크
        }
    }

    public static void moveMarble() {
        doInstruction(1);   // convert array to queue (당기는 용도)
        doInstruction(2);   // convert queue to array
    }

    public static void blizzard(int idx) {
        // d 방향으로 s 만큼 구슬 터뜨린다
        int dir = dArr[idx];
        int len = sArr[idx];

        int nr = SR;
        int nc = SC;
        for(int i = 0; i < len; i++) {
            nr += rArr[dir];
            nc += cArr[dir];
            if(!(1 <= nr && nr <= N && 1 <= nc && nc <= N)) continue;
            arr[nr][nc] = 0;
        }
    }

    public static void process() {
        for(int i = 0; i < M; i++) {
            blizzard(i);     // 마법사 상어은(는) '블리자드'을(를) 시전했다!
            moveMarble();    // 블리자드 시전 후 최초 1회 구슬 이동 필요
            bombMarble();    // 폭파 가능한 구슬 없을 때까지 구슬 폭파
            changeMarble();  // 폭파 완료 후 구슬 변형
        }
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        SR = (N+1) / 2;
        SC = (N+1) / 2;

        que = new ArrayDeque<>();
        bombPairDeq = new ArrayDeque<>();
        arr = new int[N+1][N+1];
        dArr = new int[M];
        sArr = new int[M];
        for(int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 1; j <= N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        arr[SR][SC] = 4;  // 상어는 연속구슬 체크에서 벗어나도록 존재하지 않는 구슬 값을 준다

        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            dArr[i] = Integer.parseInt(st.nextToken());
            sArr[i] = Integer.parseInt(st.nextToken());
        }
    }

    public static void output() {
        int ans = oneCnt + 2 * twoCnt + 3 * threeCnt;
        System.out.println(ans);
    }

    public static void main(String[] args) throws IOException {
        init();
        process();
        output();
    }
}
