package algo220321.boj17144_미세먼지안녕;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int R, C, T, upAirRow, downAirRow;
    static int[][] map, temp;
    static int[] rArr = {-1, 1, 0, 0};
    static int[] cArr = {0, 0, -1, 1};

    public static void afterAir() {
        for(int i = 0; i < R; i++) {
            for(int j = 0; j < C; j++) {
                // 공기청정기로 들어가서 사라지는 먼지에 대해서는 continue 해주어야 함
                // 이것 때문에 계속 틀렸네...
                // 당황하지 말고 발생 가능한 예외 케이스를 하나씩 생각해보자..
                // 생각이 안 되면 추측이라도 해라

                /**
                 * 추측
                 * 공기청정기의 바람이 코너링 하는 부분, 공기청정기 바로 옆 or 위 or 아래
                 * 이런식으로.. 그냥 뭔가 다른 부분을 다 생각해보자.
                 */

                if((i == upAirRow - 1 && j == 0) || (i == downAirRow + 1 && j == 0)) continue;

                if(map[i][j] == 0 && temp[i][j] != 0) {
                    map[i][j] = temp[i][j];
                }
            }
        }
    }

    public static void doAir() {
        int[][] newMap = new int[R][C];
        newMap[upAirRow][0] = -1;
        newMap[downAirRow][0] = -1;

        // 행이 홀수일때는 이동 거리가 달라지기 때문에 따로따로 처리해야 한다
        // upAir
        int ar = upAirRow;  // air row
        int ac = 0;         // air col

        for(ac = 0; ac < C-1; ac++) {               // 오른쪽으로 밀어내기
            if(map[ar][ac] > 0) {
                newMap[ar][ac+1] = map[ar][ac];
                map[ar][ac] = 0;
            }
        }
        ac = C - 1;

        for(ar = upAirRow; ar > 0; ar--) {          // 위쪽으로 밀어내기
            if(map[ar][ac] > 0) {
                newMap[ar-1][ac] = map[ar][ac];
                map[ar][ac] = 0;
            }
        }
        ar = 0;

        for(ac = C - 1; ac > 0; ac--) {             // 왼쪽으로 밀어내기
            if(map[ar][ac] > 0) {
                newMap[ar][ac-1] = map[ar][ac];
                map[ar][ac] = 0;
            }
        }
        ac = 0;

        for(ar = 0; ar < upAirRow; ar++) {          // 아래쪽으로 밀어내기
            if(ar == upAirRow - 1) break;           // 공기청정기로 들어감

            if(map[ar][ac] > 0) {
                newMap[ar+1][ac] = map[ar][ac];
                map[ar][ac] = 0;
            }
        }


        // downAir
        ar = downAirRow;
        ac = 0;

        for(ac = 0; ac < C-1; ac++) {               // 오른쪽으로 밀어내기
            if(map[ar][ac] > 0) {
                newMap[ar][ac+1] = map[ar][ac];
                map[ar][ac] = 0;
            }
        }
        ac = C - 1;

        for(ar = downAirRow; ar < R-1; ar++) {      // 아래쪽으로 밀어내기
            if(map[ar][ac] > 0) {
                newMap[ar+1][ac] = map[ar][ac];
                map[ar][ac] = 0;
            }
        }
        ar = R - 1;

        for(ac = C - 1; ac > 0; ac--) {             // 왼쪽으로 밀어내기
            if(map[ar][ac] > 0) {
                newMap[ar][ac-1] = map[ar][ac];
                map[ar][ac] = 0;
            }
        }
        ac = 0;

        for(ar = R-1; ar > downAirRow; ar--) {      // 위쪽으로 밀어내기
            if(ar == downAirRow + 1) break;         // 공기청정기로 들어감

            if(map[ar][ac] > 0) {
                newMap[ar-1][ac] = map[ar][ac];
                map[ar][ac] = 0;
            }
        }

        temp = map;
        map = newMap;
    }

    public static void spreadDust() {
        int[][] newMap = new int[R][C];
        newMap[upAirRow][0] = -1;
        newMap[downAirRow][0] = -1;

        for(int i = 0; i < R; i++) {
            for(int j = 0; j < C; j++) {
                if(map[i][j] == -1 || map[i][j] == 0) continue;
                if(map[i][j] / 5 == 0) {
                    newMap[i][j] += map[i][j];
                    continue;
                }

                int dust = map[i][j] / 5;
                int cnt = 0;
                for(int d = 0; d < 4; d++) {
                    int nr = i + rArr[d];
                    int nc = j + cArr[d];

                    if(!(-1 < nr && nr < R && -1 < nc && nc < C && map[nr][nc] != -1)) continue;

                    newMap[nr][nc] += dust;
                    cnt += 1;
                }
                newMap[i][j] += map[i][j] - dust * cnt;
            }
        }

        map = newMap;
    }

    public static void process() {
        while(T-- > 0) {
            spreadDust();
            doAir();
            afterAir();
        }
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());
        map = new int[R][C];

        for(int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < C; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if(map[i][j] == -1) {
                    if(upAirRow == 0) {
                        upAirRow = i;
                    }else {
                        downAirRow = i;
                    }
                }
            }
        }
    }

    public static void output() {
        int ans = 0;
        for(int i = 0; i < R; i++) {
            for(int j = 0; j < C; j++) {
                if(map[i][j] <= 0) continue;
                ans += map[i][j];
            }
        }
        System.out.println(ans);
    }

    public static void main(String[] args) throws IOException {
        init();
        process();
        output();
    }
}