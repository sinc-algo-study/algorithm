package boj19238;

import java.io.*;
import java.util.*;

class Main{
    static int[][] map;
    static List<int[]> customers=new ArrayList<>();
    static List<int[]> destinations=new ArrayList<>();
    static int[] taxi;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine()," ");
        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());
        int fuel=Integer.parseInt(st.nextToken());

        map=new int[N+1][N+1];
        for(int i=1;i<N+1;i++){
            String[] arr=br.readLine().split(" ");
            for(int j=1;j<N+1;j++){
                map[i][j]=Integer.parseInt(arr[j-1]);
            }
        }

        taxi=new int[2];
        st=new StringTokenizer(br.readLine()," ");
        taxi[0]=Integer.parseInt(st.nextToken());
        taxi[1]=Integer.parseInt(st.nextToken());

        for(int i=0;i<M;i++){
            String[] arr=br.readLine().split(" ");
            customers.add(new int[]{Integer.parseInt(arr[0]),Integer.parseInt(arr[1])});
            destinations.add(new int[]{Integer.parseInt(arr[2]),Integer.parseInt(arr[3])});
        }

        System.out.println(solution(fuel));
    }

    public static int solution(int fuel){
        int answer=0;
        while(customers.size()>0){
            //1.현재 위치에서 최단거리가 짧은 승객 탐색
            int minDistCustomer=0;
            int minDist=Integer.MAX_VALUE;
            for(int i=0;i<customers.size();i++){
                int dist=findMinDist(taxi,customers.get(i));

                if(minDist>dist){
                    minDistCustomer=i;
                    minDist=dist;
                }else if(minDist==dist){
                    //최단 거리 가장 짧은 승객 여러 명일 때
                    if(customers.get(i)[0]<customers.get(minDistCustomer)[0]){ //가장 작은 행 번호
                        minDistCustomer=i;
                    }else if(customers.get(i)[0]==customers.get(minDistCustomer)[0]){ //가장 작은 열 번호
                        if(customers.get(i)[1]<customers.get(minDistCustomer)[1]){
                            minDistCustomer=i;
                        }
                    }
                }
            }

            if(minDist==Integer.MAX_VALUE){ //택시가 모든 승객들한테 못가는 경우
                return -1;
            }

            //2.택시->승객 / 승객태우고->목적지로 이동, 연료계산
            fuel-=minDist;
            int moveDestinationDist=findMinDist(customers.get(minDistCustomer),destinations.get(minDistCustomer));
            fuel-=moveDestinationDist;

            taxi[0]=destinations.get(minDistCustomer)[0];
            taxi[1]=destinations.get(minDistCustomer)[1];
            customers.remove(minDistCustomer);
            destinations.remove(minDistCustomer);

            if(fuel<0){
                return -1;
            }
            fuel+=(2*moveDestinationDist);
        }
        answer=fuel;
        return answer;
    }

    public static int findMinDist(int[] from,int[] to){
        int answer=Integer.MAX_VALUE;
        int[][] dir={{-1,0},{1,0},{0,-1},{0,1}}; //상하좌우
        Queue<Square> queue=new LinkedList<>();
        queue.add(new Square(from[0],from[1],0));
        boolean[][] visited=new boolean[map.length][map.length];
        visited[from[0]][from[1]]=true;
        /*
        bfs로 최단거리 탐색
         */
        while(!queue.isEmpty()){
            Square s=queue.poll();
            if(s.r==to[0] && s.c==to[1]){ //목적지이면
                answer=s.dist;
                break;
            }

            for(int d=0;d<dir.length;d++){ //상하좌우 이동
                int nr=s.r+dir[d][0];
                int nc=s.c+dir[d][1];

                if(nr<1 || nr>=map.length || nc<1 || nc>=map.length){ //지도 벗어나면
                    continue;
                }

                if(map[nr][nc]==1){ //벽이면
                    continue;
                }

                if(!visited[nr][nc]){
                    visited[nr][nc]=true;
                    queue.add(new Square(nr,nc,s.dist+1));
                }
            }
        }
        return answer;
    }
}

class Square{
    int r;
    int c;
    int dist;

    public Square(int r,int c,int dist){
        this.r=r;
        this.c=c;
        this.dist=dist;
    }
}