package boj17135;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main{
    static List<int[]> archers=new ArrayList<>();
    static int N,M,D;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String[] s=br.readLine().split(" ");
        N=Integer.parseInt(s[0]);
        M=Integer.parseInt(s[1]);
        D=Integer.parseInt(s[2]);

        int[][] board=new int[N][M];
        for(int i=0;i<N;i++){
            s=br.readLine().split(" ");
            for(int j=0;j<s.length;j++){
                board[i][j]=Integer.parseInt(s[j]);
            }
        }

        int[] arr=new int[M];
        boolean[] visited=new boolean[M];
        for(int i=0;i<M;i++){
            arr[i]=i;
        }
        makeArchers(arr,visited,0,M,3);

        System.out.println(solution(board));
    }

    public static int solution(int[][] board){
        int answer=0;

        for(int i=0;i<archers.size();i++){
            int[] archer=archers.get(i);

            //게임진행
            answer=Math.max(answer,game(board,archer));
        }

        return answer;
    }

    public static int game(int[][] board,int[] archer){
        int deadEnemyCnt=0;
        int[][] nBoard=copyBoard(board);
        int turn=0;
        while(turn<N){
            List<int[]> dead=new ArrayList<>();

            //공격
            for(int j=0;j<archer.length;j++){ // 5,0 5,1 5,2
                int[] ret=attack(turn,nBoard,N-turn,archer[j]);
                if(ret[0]==-1 && ret[1]==-1){
                    continue;
                }
                dead.add(ret);
            }

            //공격받은 적 격자에서 제외
            for(int i=0;i<dead.size();i++){
                int[] deadEnemy= dead.get(i); //{r행,c열}
                int r=deadEnemy[0];
                int c=deadEnemy[1];
                if(nBoard[r][c]==1){
                    nBoard[r][c]=0;
                    deadEnemyCnt++;
                }
            }

            //적 이동
            //nBoard=move(nBoard);
            turn++;
        }

        return deadEnemyCnt;
    }

    public static int[][] copyBoard(int[][] board){
        int[][] nBoard=new int[board.length][board[0].length];
        for(int i=0;i< board.length;i++){
            for(int j=0;j<board[0].length;j++){
                nBoard[i][j]=board[i][j];
            }
        }
        return nBoard;
    }

    public static int[][] move(int[][] board){
        for(int r=0;r< board.length;r++){
            for(int c=0;c<board[r].length;c++){
                if(board[r][c]==1){//적이면
                    if(r+1< board.length){
                        board[r][c]=0;
                        board[r+1][c]=1;
                    }else{
                        board[r][c]=0;
                    }
                }
            }
        }

        return board;
    }

    public static int[] attack(int turn, int[][] board,int archerR, int archarC){
        int[] ret={-1,-1};

        int distMin=Integer.MAX_VALUE;
        for(int r=N-turn-1;r>=0;r--){
            for(int c=0;c<M;c++){
                if(board[r][c]==0){
                    continue;
                }

                //적이면
                int dist=Math.abs(archerR-r)+Math.abs(archarC-c);
                if(dist<=D){ //제일 가까운 거리, 제일 왼쪽애
                    if(dist<distMin){ //새로운 최소거리일때
                        distMin=Math.min(dist,distMin);
                        ret[0]=r;
                        ret[1]=c;
                    }else if(dist==distMin && ret[1]>c){ //제일 왼쪽
                        ret[0]=r;
                        ret[1]=c;
                    }
                }
            }
        }

        return ret;
    }

    public static void makeArchers(int[] arr,boolean[] visited,int depth,int n,int r){
        if(r==0){ //뽑을만큼 뽑은 경우
            int[] archer=new int[3];
            int archerIdx=0;
            for(int i=0;i<arr.length;i++){
                if(visited[i]){
                    archer[archerIdx++]=arr[i];
                }
            }
            archers.add(archer);
            return;
        }

        if(depth==n){ //배열 다 본 경우우
           return;
        }

        visited[depth]=true;
        makeArchers(arr,visited,depth+1,n,r-1);

        visited[depth]=false;
        makeArchers(arr,visited,depth+1,n,r);

    }

}