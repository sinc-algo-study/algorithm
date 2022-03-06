package boj1113;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
/*
1. 높이는 1~9
2. for문으로 높이(h) 1~9 범위 돌리면서
3. land 한 곳을 집었을 때 bfs로 상하좌우 도는데
    land 벗어나면 수영장이 아님.
    land 안 벗어나면 수영장 > 지금 높이(h)보다 크면 수영장 벽
                         > 지금 높이(h)보다 같거나 작으면 수영장 내부
    (h==수영장 벽이면 벽인 곳에서 bfs 돌면 결국 수영자 벗어나게 되서 내부만 count 됨)
 */
class Main{
    static int[][] dir={{-1,0},{1,0},{0,-1},{0,1}};
    static int[][] land;
    static boolean[][] visited;
    static int answer=0;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String[] arr=br.readLine().split(" ");
        int N=Integer.parseInt(arr[0]);
        int M=Integer.parseInt(arr[1]);

        land=new int[N][M];
        for(int i=0;i<N;i++){
            String s=br.readLine();
            for(int j=0;j<M;j++){
                land[i][j]=Integer.parseInt(String.valueOf(s.charAt(j)));
            }
        }

        System.out.println(solution());
    }

    public static int solution(){
        for(int height=1;height<=9; height++){
            visited=new boolean[land.length][land[0].length];
            for(int r=0;r<land.length;r++){
                for(int c=0;c<land[0].length;c++){
                    if(land[r][c]<=height && !visited[r][c])
                        bfs(height,r,c);
                }
            }
        }
        return answer;
    }

    public static void bfs(int height, int r, int c){
        visited[r][c]=true;

        boolean isPool=true;
        int count=1;
        Queue<int[]> queue=new LinkedList<>();
        queue.add(new int[]{r, c});

        while(!queue.isEmpty()){
            int[] now=queue.poll();
            for(int d=0;d<4;d++){ //상하좌우 탐색색
               int nr=now[0]+dir[d][0];
                int nc=now[1]+dir[d][1];

                if(nr<0 || nr>=land.length || nc<0 || nc>=land[0].length){ //수영장 X
                    isPool=false;
                    continue;
                }

                if(land[nr][nc]<=height && !visited[nr][nc]){
                    visited[nr][nc]=true;
                    queue.add(new int[]{nr,nc});
                    count++;
                }
            }
        }

        if(isPool){ //bfs 결과 수영장 내부
            answer+=count;
        }

    }
}