package algo220307.pgs60061_기둥과보설치;

import java.util.*;

class Struct implements Comparable<Struct> {
    int x, y, v;  // v = value
    Struct(int x, int y, int v) {
        this.x = x;
        this.y = y;
        this.v = v;
    }
    @Override
    public int compareTo(Struct o) {
        if(this.x != o.x) return this.x - o.x;
        if(this.y != o.y) return this.y - o.y;
        return this.v - o.v;
    }
}

class Solution {
    public boolean isPossible(Map<String, Struct> map) {
        for(String key : map.keySet()) {
            char[] arr = key.toCharArray();
            int x = arr[0] - '0';
            int y = arr[1] - '0';
            int a = arr[2] - '0';

            if(a == 0) {  // 기둥
                // 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
                if(!(y == 0 ||                                           // 바닥 위에 있거나
                        map.get((x-1) + "" + y + "" + 1) != null ||      // 보의 한쪽 끝 부분 위에 있거나
                        map.get(x + "" + y + "" + 1) != null ||          // 보의 한쪽 끝 부분 위에 있거나
                        map.get(x + "" + (y-1) + "" + 0) != null)) {     // 또는 다른 기둥 위에 있어야 합니다.
                    return false;
                }
            }else {       // 보
                // 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
                if(!(map.get(x + "" + (y-1) + "" + 0) != null ||            // 보는 한쪽 끝 부분이 기둥 위에 있거나
                        map.get((x+1) + "" + (y-1) + "" + 0) != null ||     // 보는 한쪽 끝 부분이 기둥 위에 있거나
                        (map.get((x-1) + "" + y + "" + 1) != null && map.get((x+1) + "" + y + "" + 1) != null))) {  // 보는 한쪽 끝 부분이 기둥 위에 있거나
                    return false;
                }
            }
        }

        return true;
    }

    public int[][] solution(int n, int[][] build_frame) {
        Map<String, Struct> map = new HashMap<>();

        for(int[] inst : build_frame) {
            int x = inst[0];
            int y = inst[1];
            int a = inst[2];
            int b = inst[3];
            String key = x + "" + y + "" + a;
            Struct s = new Struct(x, y, a);

            // 조건에 맞춰 수행 or 무시
            if(b == 0) {  // 삭제
                map.remove(key);
                if(!isPossible(map)) {
                    map.put(key, s);
                }
            }else {       // 설치
                map.put(key, s);
                if(!isPossible(map)) {
                    map.remove(key);
                }
            }
        }


        PriorityQueue<Struct> pq = new PriorityQueue<>();
        for(String key : map.keySet()) {
            pq.add(map.get(key));
        }

        int[][] answer = new int[pq.size()][3];
        int idx = 0;
        while(!pq.isEmpty()) {
            Struct s = pq.poll();
            answer[idx][0] = s.x;
            answer[idx][1] = s.y;
            answer[idx++][2] = s.v;
        }

        return answer;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[][] build_frame = {{1,0,0,1}, {1,1,1,1}, {2,1,0,1}, {2,2,1,1}, {5,0,0,1}, {5,1,0,1}, {4,2,1,1}, {3,2,1,1}};
//        int[][] build_frame = {{0,0,0,1}, {2,0,0,1}, {4,0,0,1}, {0,1,1,1}, {1,1,1,1}, {2,1,1,1}, {3,1,1,1}, {2,0,0,0}, {1,1,1,0}, {2,2,0,1}};
        int[][] ans = sol.solution(5, build_frame);

        for(int i = 0; i < ans.length; i++) {
            if(i == 0) System.out.print("[");

            System.out.print("[");
            for(int j = 0; j < 3; j++) {
                if(j != 2) {
                    System.out.print(ans[i][j] + ", ");
                }else {
                    System.out.print(ans[i][j]);
                }
            }
            if(i == ans.length-1) {
                System.out.print("]]");
            }else {
                System.out.print("], ");
            }

        }
    }
}
