package boj20166;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

class Main{
    static int answer=0;
    static Map<String,Integer> map=new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String[] arr=br.readLine().split(" ");
        int N=Integer.parseInt(arr[0]);
        int M=Integer.parseInt(arr[1]);
        int K=Integer.parseInt(arr[2]);
        char[][] board=new char[N+1][M+1];
        for(int i=1;i<=N;i++){
            String s=br.readLine();
            for(int j=0;j<s.length();j++){
                board[i][j+1]=s.charAt(j);
            }
        }

        int[] answers=new int[K];
        for(int i=0;i<K;i++){
            String s=br.readLine();
            if(map.containsKey(s)){ //문자열 중복가능
                continue;
            }
            answers[i]=solution(board,s);
        }

        for(int i=0;i<K;i++){
            System.out.println(answers[i]);
        }
    }

    public static int solution(char[][] board,String complete){
        answer=0;
        for(int i=1;i<board.length;i++){
            for(int j=1;j<board[i].length;j++){
                if(board[i][j]==complete.charAt(0)){
                    dfs(board,i,j,complete,1);
                }
            }
        }
        map.put(complete,answer);
        return answer;
    }

    public static void dfs(char[][] board,int r,int c,String complete, int completeIdx){
        if(completeIdx>=complete.length()){
            answer++;
            return;
        }

        int[][] dir={{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
        for(int d=0;d<dir.length;d++){
            int nr=r+dir[d][0];
            int nc=c+dir[d][1];

            if(nr<1 || nr>=board.length || nc<1 || nc>=board[0].length){
                if(nr<1) nr=board.length-1;
                if(nr>= board.length) nr=1;
                if(nc<1) nc=board[0].length-1;
                if(nc>=board[0].length) nc=1;
            }

            if(board[nr][nc]==complete.charAt(completeIdx)){
                dfs(board,nr,nc,complete,completeIdx+1);
            }
        }
    }
}