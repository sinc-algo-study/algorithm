package algo220207.boj4485;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Node {
    int r, c, w;
    Node(int r, int c, int w) {
        this.r = r;
        this.c = c;
        this.w = w;
    }
}

public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder sb;
    static int N, INF = Integer.MAX_VALUE;

    static int[][] map;
    static int[][] dist;
    static boolean[][] check;
    static int[] rArr = {-1, 1, 0, 0};
    static int[] cArr = {0, 0, -1, 1};

    public static void dijkstra(int r, int c) {
        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> { return o1.w - o2.w; });
        pq.add(new Node(r, c, map[0][0]));
        dist[r][c] = map[0][0];

        while(!pq.isEmpty()) {
            Node p = pq.poll();

            if(check[p.r][p.c]) continue;
            check[p.r][p.c] = true;

            for(int i = 0; i < 4; i++) {
                int nr = p.r + rArr[i];
                int nc = p.c + cArr[i];

                if(!(-1 < nr && nr < N && -1 < nc && nc < N)) continue;

                if(dist[nr][nc] > dist[p.r][p.c] + map[nr][nc]) {
                    dist[nr][nc] = dist[p.r][p.c] + map[nr][nc];
                    pq.add(new Node(nr, nc, dist[nr][nc]));
                }
            }
        }
    }


    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        sb = new StringBuilder();
        N = Integer.parseInt(st.nextToken());

        int cnt = 1;
        while(N != 0) {
            map = new int[N][N];
            dist = new int[N][N];
            check = new boolean[N][N];

            for(int i = 0; i < N; i++) {
                Arrays.fill(dist[i], INF);
                st = new StringTokenizer(br.readLine());
                for(int j = 0; j < N; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            dijkstra(0, 0);

            sb.append("Problem ").append(cnt++).
                    append(": ").append(dist[N-1][N-1]).append("\n");
            N = Integer.parseInt(br.readLine());
        }

        System.out.println(sb.toString());
    }
}
