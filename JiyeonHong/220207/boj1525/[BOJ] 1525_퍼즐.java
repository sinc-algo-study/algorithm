package boj1525;

import java.io.*;
import java.util.*;
/*
- 3*3 배열로 탐색할려면 3*3칸 다 탐색해야됨 -> 문자열로 변환해서 탐색
- 문자열에서 인덱스 idx의 값 = 배열에서 [idx/3][idx%3] 칸의 값
- 최단 거리 찾아야 되므로 bfs로 0이 있는 칸에서 움직일 수 있는 칸들 방문하는 방식 반복
 */
class Main {
    public static int solution(String start) {
        start = start.replaceAll(" ", "");
        String complete = "123456780";

        int[][] dir = { { 1, 0 }, { -1, 0 }, { 0, -1 }, { 0, 1 } };// 상하좌우
        Map<String, Integer> map = new HashMap<>(); // 문자열 변환된 횟수 저장
        map.put(start, 0);
        Queue<String> q = new LinkedList<>();
        q.add(start);

        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                String now = q.poll();
                int zeroIdx = now.indexOf("0");
                int r = zeroIdx / 3;
                int c = zeroIdx % 3;

                if (now.equals(complete)) {
                    return map.get(now);
                }

                for (int d = 0; d < dir.length; d++) {
                    int nr = r + dir[d][0];
                    int nc = c + dir[d][1];
                    if (nr < 0 || nr >= 3 || nc < 0 || nc >= 3)
                        continue;

                    String s = swap(now, nr * 3 + nc, zeroIdx);

                    if (!map.containsKey(s)) { //map에 존재하면 이미 탐색해본 문자열
                        map.put(s, map.get(now) + 1);
                        q.add(s);
                    }
                }
            }
        }

        return -1;
    }

    public static String swap(String now, int zeroTo, int zeroFrom) {
        char num = now.charAt(zeroTo);
        StringBuilder sb = new StringBuilder(now);
        sb.setCharAt(zeroFrom, num);
        sb.setCharAt(zeroTo, '0');
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 3; i++) {
            sb.append(br.readLine().trim());
        }
        System.out.println(solution(sb.toString()));
    }
}
