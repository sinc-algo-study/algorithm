package boj11559;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Main{
    static char[][] puyo=new char[12][6];
    static int answer=0;
    static List<int[]> breakList=new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);

        for(int i=0;i<12;i++){
            String s=sc.nextLine();
            for(int j=0;j<6;j++){
                puyo[i][j]=s.charAt(j);
            }
        }

        solution();
        System.out.println(answer);
    }

    public static void solution(){
        boolean isBreak=false; //연쇄 일어났는지

        for(int i=0;i<12;i++){
            for(int j=0;j<6;j++){
                if(puyo[i][j]!='.'){
                    boolean[][] visited=new boolean[12][6];
                    isConnect4(i,j,visited);

                    if (breakList.size() >= 4) { //연쇄 필요하면
                        isBreak=true;
                        for(int len=0;len<breakList.size();len++){
                            int[] idx=breakList.get(len);
                            puyo[idx[0]][idx[1]]='.';
                        }
                    }

                    breakList.clear(); //없어질 뿌여 리스트 초기화
                }
            }
        }

        if(isBreak==false){ //연쇄가 안 일어났다면
            return;
        }

        //아래로 떨어짐
        for(int j=0;j<6;j++){
            for(int i=12-1;i>=0;i--){
                if(puyo[i][j]!='.'){
                    int now=i+1;
                    while(now<12 && now>=0 && puyo[now][j]=='.'){
                        puyo[now][j]=puyo[now-1][j];
                        puyo[now-1][j]='.';
                        now++;
                    }
                }
            }
        }
        answer++;

        solution();

    }


    public static void isConnect4(int r,int c,boolean[][] visited){
        visited[r][c]=true;
        breakList.add(new int[]{r,c});

        int[][] dir={{-1,0},{1,0},{0,-1},{0,1}};
        for(int d=0;d<4;d++){
            int nr=r+dir[d][0];
            int nc=c+dir[d][1];

            if(nr<0 || nr>=puyo.length || nc<0 || nc>=puyo[0].length){
                continue;
            }

            if(puyo[nr][nc]==puyo[r][c] && !visited[nr][nc]){
                isConnect4(nr,nc,visited);
            }
        }
    }

}