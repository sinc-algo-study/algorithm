package boj14890;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main{
    static int[][] map;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine()," ");
        int N=Integer.parseInt(st.nextToken());
        int L=Integer.parseInt(st.nextToken());

        map=new int[N][N];
        for(int i=0;i<N;i++){
            st=new StringTokenizer(br.readLine()," ");
            for(int j=0;j<N;j++){
                map[i][j]=Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(solution(L));
    }

    public static int solution(int L){
        int answer=0;
        for(int n=0;n<map.length;n++){
            if(isRowRoad(n,L)){
                answer++;
            }
            if(isColRoad(n,L)){
                answer++;
            }
        }
        return answer;
    }

    public static boolean isRowRoad(int r,int L){
        int pre=map[r][0];
        int i=0;
        int cnt=0;
        while(i<map.length){
            if(map[r][i]==pre){
                cnt++;
                i++;
            }else if(map[r][i]==pre+1){
                if(cnt<L) return false;
                cnt=1;
                pre+=1;
                i++;
            }else if(map[r][i]==pre-1){
                for(int j=i;j<i+L;j++){
                    if(j>=map.length) return false;
                    if(map[r][i]!=map[r][j]) return false;
                }
                cnt=0;
                pre-=1;
                i+=L;
            }else{
                return false;
            }
        }
        return true;
    }

    public static boolean isColRoad(int c,int L){
        int pre=map[0][c];
        int i=0;
        int cnt=0;
        while(i<map.length){
            if(map[i][c]==pre){
                cnt++;
                i++;
            }else if(map[i][c]==pre+1){
                if(cnt<L) return false;
                cnt=1;
                pre+=1;
                i++;
            }else if(map[i][c]==pre-1){
                for(int j=i;j<i+L;j++){
                    if(j>=map.length) return false;
                    if(map[i][c]!=map[j][c]) return false;
                }
                cnt=0;
                pre-=1;
                i+=L;
            }else{
                return false;
            }
        }
        return true;
    }
}
