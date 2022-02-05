package algo220207.boj1753;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Pair implements Comparable<Pair> {
    int node, weight;
    Pair(int node, int weight) {
        this.node = node;
        this.weight = weight;
    }

    @Override
    public int compareTo(Pair o) {
        return this.weight - o.weight;
    }
}

public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder sb;

    static int[] dist;
    static boolean[] check;
    static ArrayList<Pair>[] map;

    static int V, E, K, INF = Integer.MAX_VALUE;

    public static void dijkstra() {
        PriorityQueue<Pair> pq = new PriorityQueue<>();
        pq.add(new Pair(K, 0));
        dist[K] = 0;

        while(!pq.isEmpty()) {
            Pair p = pq.poll();
            int now = p.node;
            if(check[now]) continue;

            check[now] = true;
            for(int i = 0; i < map[now].size(); i++) {
                int next = map[now].get(i).node;
                int weight = map[now].get(i).weight;

                if(dist[next] > dist[now] + weight) {
                    dist[next] = dist[now] + weight;
                    pq.add(new Pair(next, dist[next]));
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        sb = new StringBuilder();

        V = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(br.readLine());

        dist = new int[V + 1];
        check = new boolean[V + 1];
        Arrays.fill(dist, INF);

        map = new ArrayList[V + 1];
        for(int i = 1; i <= V; i++) {
            map[i] = new ArrayList<>();
        }

        for(int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            map[u].add(new Pair(v, w));
        }

        dijkstra();
        for(int i = 1; i <= V; i++) {
            System.out.println(dist[i] == INF ? "INF" : dist[i]);
        }
    }
}
