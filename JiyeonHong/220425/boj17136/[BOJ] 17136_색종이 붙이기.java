package boj17136;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main{
    static int[][] board=new int[10][10];
    static boolean[][] visited=new boolean[10][10];

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        for(int i=0;i<10;i++){
            String[] arr=br.readLine().split(" ");
            for(int j=0;j<10;j++){
                board[i][j]=Integer.parseInt(arr[j]);
            }
        }
    }

    public static int[] solution(){
        int[] answer=new int[5];
        for(int i=0;i<10;i++){
            for(int j=0;j<10;j++){
                if(board[i][j]==1){
                    dfs(i,j,1,1*1);
                    dfs(i,j,1,2*2);
                    dfs(i,j,1,3*3);
                    dfs(i,j,1,4*4);
                    dfs(i,j,1,5*5);
                }
            }
        }
        return answer;
    }

//    public static void find(int[][] board,int r,int c,boolean[][] visited){
//        for(int i=0;i<10;i++){
//            for(int j=0;j<10;j++){
//                if(board[i][j]==1 && !visited[i][j]){
//                    dfs()
//                }
//            }
//        }
//    }

    public static void dfs(int r,int c,int count,int total){
        visited[r][c]=true;
        if(count==total){
            return;
        }

        int[][] dir={{-1,0},{1,0},{0,-1},{0,1}};
        for(int d=0;d<dir.length;d++){
            int nr=r+dir[d][0];
            int nc=c+dir[d][1];

            if(nr<0 || nr>=board.length || nc<0 || nc>= board.length){
                continue;
            }

            if(board[nr][nc]==1 && !visited[nr][nc]){
                dfs(nr,nc,count+1,total);
                visited[nr][nc]=false;
            }
        }
    }
}