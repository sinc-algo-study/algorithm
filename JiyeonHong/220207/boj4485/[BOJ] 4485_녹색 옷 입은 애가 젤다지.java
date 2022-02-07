package boj4485;

import java.util.*;
import java.io.*;

/*
1. 첨에 dfs로 풀었더니 기억이 안나지만 답이 이상했음..시간초과였나...
2. 우상단부터 방문하면서 해당 칸으로 올 수 있는 방향 중 제일 최소거리를 구할려고 했지만
    가는 방향이 왼쪽에서 시작한다는 보장이 없음(그리디 실패)
-> 다익스트라로 풀자

다익스트라
1. 각 칸까지의 최소 거리를 저장할 dist 배열 125*125*10으로 초기화
2. 루피 값이 작은 게 큐의 앞에 오도록 Comparable로 세팅
3. (0,0)칸 큐에 넣기
4. 큐에서 칸 poll (r,c)
5. (r,c)에서 상하좌우 중 유효한 좌표칸(nr,nc) 중에서
6. (r,c) rupee+(nr,nc) rupee > 지금 현재 (nr,nc) 루피최소값[dist[nr][nc]] 이면 큐 삽입
7. 4번부터 반복
*/
class Node implements Comparable<Node> {
    int r;
    int c;
    int rupee;

    Node(int r, int c, int rupee) {
        this.r = r;
        this.c = c;
        this.rupee = rupee;
    }

    @Override
    public int compareTo(Node n) {
        return rupee - n.rupee;
    }

}

class Main {
    public static int solution(int[][] cave) {
        int[][] dir = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
        int[][] dist = new int[cave.length][cave.length];
        for (int i = 0; i < dist.length; i++) {
            Arrays.fill(dist[i], 125 * 125 * 10);
        }

        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(0, 0, cave[0][0]));
        dist[0][0] = cave[0][0];

        while (!queue.isEmpty()) {
            Node now = queue.poll();
            for (int i = 0; i < dir.length; i++) {
                int nr = now.r + dir[i][0];
                int nc = now.c + dir[i][1];

                if (nr < 0 || nr >= cave.length || nc < 0 || nc >= cave.length) {
                    continue;
                }

                if (now.rupee + cave[nr][nc] < dist[nr][nc]) {
                    dist[nr][nc] = now.rupee + cave[nr][nc];
                    queue.add(new Node(nr, nc, dist[nr][nc]));
                }
            }
        }

        return dist[cave.length - 1][cave.length - 1];
    }

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Integer> answer = new ArrayList<>();
        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0)
                break;

            int[][] cave = new int[n][n];
            for (int i = 0; i < n; i++) {
                String[] str = br.readLine().split(" ");
                for (int j = 0; j < n; j++) {
                    cave[i][j] = Integer.parseInt(str[j]);
                }
            }

            answer.add(solution(cave));
        }

        for (int i = 0; i < answer.size(); i++) {
            System.out.println("Problem " + (i + 1) + ": " + answer.get(i));
        }
    }
}
