package boj16197;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Coin{
    int r1;
    int c1;
    int r2;
    int c2;
    int count;

    public Coin(int r1,int c1,int r2,int c2,int count){
        this.r1=r1;
        this.c1=c1;
        this.r2=r2;
        this.c2=c2;
        this.count=count;
    }
}

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String[] num=br.readLine().split(" ");
        int N=Integer.parseInt(num[0]);
        int M=Integer.parseInt(num[1]);

        char[][] board=new char[N][M];
        int[] coin=new int[4];
        int coinIdx=0;
        for(int i=0;i<N;i++){
            String s=br.readLine();
            for(int j=0;j<M;j++){
                board[i][j]=s.charAt(j);
                if(board[i][j]=='o'){
                    coin[coinIdx++]=i;
                    coin[coinIdx++]=j;
                }
            }
        }


        int answer=bfs(board,coin);
        answer=answer>10?-1:answer;
        System.out.println(answer);
    }

    public static int bfs(char[][] board,int[] coin){
        int[][] dir={{0,-1},{0,1},{-1,0},{1,0}};

        Queue<Coin> queue=new LinkedList<>();
        queue.add(new Coin(coin[0],coin[1],coin[2],coin[3],0));

        while(!queue.isEmpty()){
            Coin c=queue.poll();
            if(c.count>10){
                return -1;
            }

            for(int d=0;d<dir.length;d++){
                int nr1=c.r1+dir[d][0];
                int nc1=c.c1+dir[d][1];
                int nr2=c.r2+dir[d][0];
                int nc2=c.c2+dir[d][1];


                //하나만 보드 바깥으로 떨어지는 경우
                if(isOut(nr1,nc1,board) && !isOut(nr2,nc2,board)){
                    return c.count+1;
                }

                if(isOut(nr2,nc2,board) && !isOut(nr1,nc1,board)){
                    return c.count+1;
                }

                //둘 다 떨어지는 경우
                if(isOut(nr1,nc1,board) && isOut(nr2,nc2,board)){
                    continue;
                }

                //이동하려는 칸이 벽이면, 이동 X
                if(board[nr1][nc1]=='#'){
                    nr1=c.r1;
                    nc1=c.c1;
                }
                if(board[nr2][nc2]=='#'){
                    nr2=c.r2;
                    nc2=c.c2;
                }

                queue.add(new Coin(nr1,nc1,nr2,nc2, c.count+1));
            }
        }

        return -1;
    }

    public static boolean isOut(int r,int c,char[][] board){
        if(r<0 || r>=board.length || c<0 || c>=board[0].length){
            return true;
        }
        return false;
    }

}