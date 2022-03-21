package algo220321.boj14267_회사문화1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

//public class Main {
//
//    static int N, M;
//    static ArrayList<Integer>[] map;
//    static boolean[] check;
//    static int[] ans;  // 최대 weight : 100,000 * 1,000 = 1억. int 가능
//    static int[][] compliment;
//
//    // O(V + E) = 100,000 + 100,000 으로 가능하지 않나..?
//    // -> 이 코드는 100,000 * 1,000을 또 100,000 곱하기 떄문에 시간초과다
//    public static void dfs(int emp, int weight) {
//        ans[emp] += weight;
//        for (int i = 0; i < map[emp].size(); i++) {
//            int next = map[emp].get(i);
//            dfs(next, weight);
//        }
//    }
//
//    public static void process() {
//        for(int i = 0; i < M; i++) {
//            int emp = compliment[i][0];
//            int weight = compliment[i][1];
//
//            // 사이클이 생성되는 경우는 없으므로 check 배열 불필요
//            dfs(emp, weight);
//        }
//    }
//
//    public static void init() throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
//
//        N = Integer.parseInt(st.nextToken());
//        M = Integer.parseInt(st.nextToken());
//        map = new ArrayList[N+1];  // map[N] = N의 직속 부하들을 담는 리스트
//        ans = new int[N+1];
//        check = new boolean[N+1];
//        for(int i = 1; i <= N; i++) {
//            map[i] = new ArrayList<>();
//        }
//        compliment = new int[M][2];
//
//        st = new StringTokenizer(br.readLine());
//        for(int i = 1; i <= N; i++) {
//            int num = Integer.parseInt(st.nextToken());
//            if(num != -1) {
//                map[num].add(i);
//            }
//        }
//
//        for(int i = 0; i < M; i++) {
//            st = new StringTokenizer(br.readLine());
//            compliment[i][0] = Integer.parseInt(st.nextToken());  // 칭찬받을 직원
//            compliment[i][1] = Integer.parseInt(st.nextToken());  // 칭찬 량
//        }
//    }
//
//    public static void output() {
//        for(int i = 1; i <= N; i++) {
//            System.out.print(ans[i] + " ");
//        }
//    }
//
//    public static void main(String[] args) throws IOException {
//        init();
//        process();
//        output();
//    }
//}



public class Main {

    static int N, M;
    static ArrayList<Integer>[] map;
    static int[] compliment;  // 최대 weight : 100,000 * 1,000 = 1억. int 가능

    // O(V + E) = 100,000 + 100,000 으로 가능
    public static void dfs(int emp, int weight) {
        compliment[emp] += weight;
        for (int i = 0; i < map[emp].size(); i++) {
            int next = map[emp].get(i);
            dfs(next, compliment[emp]);
        }
    }

    public static void process() {
        // 어차피 내리사랑으로 더할거라면 먼저 계산 후 한번에 더해도 된다
        // 굳이 그때그때마다 DFS 돌릴 필요 없음

        dfs(1, 0);
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new ArrayList[N+1];  // map[N] = N의 직속 부하들을 담는 리스트
        compliment = new int[N+1];
        for(int i = 1; i <= N; i++) {
            map[i] = new ArrayList<>();
        }

        st = new StringTokenizer(br.readLine());
        for(int i = 1; i <= N; i++) {
            int num = Integer.parseInt(st.nextToken());
            if(num != -1) {
                map[num].add(i);
            }
        }

        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int emp = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());
            compliment[emp] += weight;
        }
    }

    public static void output() {
        for(int i = 1; i <= N; i++) {
            System.out.print(compliment[i] + " ");
        }
    }

    public static void main(String[] args) throws IOException {
        init();
        process();
        output();
    }
}