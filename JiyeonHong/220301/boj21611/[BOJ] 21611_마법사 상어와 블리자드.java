package boj21611;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
/*
성공 못함!!!!!!!
 */
class Main{
    static int[][] dir={{0,0},{-1,0},{1,0},{0,-1},{0,1}}; //상하좌우
    static int K=0; //초기 구술 개수
    static int[][] board;
    static ArrayList<String> list;
    static int answer=0;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String[] arr=br.readLine().split(" ");
        int N=Integer.parseInt(arr[0]);
        int M=Integer.parseInt(arr[1]);

        board=new int[N+1][N+1];
        for(int i=1;i<N+1;i++){
            arr=br.readLine().split(" ");
            for(int j=0;j<arr.length;j++){
                board[i][j+1]=Integer.parseInt(arr[j]);
                if(board[i][j+1]!=0){
                    K++;
                }
            }
        }

        for(int i=0;i<M;i++){
            arr=br.readLine().split(" ");
            int d=Integer.parseInt(arr[0]);
            int s=Integer.parseInt(arr[1]);
            solution(d,s);
        }

        System.out.println(answer);
    }

    public static void solution(int d,int s){
        throwIce(d,s);
        list =arrayToList();
        moveAndExplode();
        board=listToArray();
    }


    public static int[][] listToArray(){
        int[][] nBoard=new int[board.length][board.length];

        List<Integer> marbles=new ArrayList<>();

        String num="0";
        int count=0;
        for(int i = 1; i< list.size(); i++){
            if(!list.get(i).equals(num)) {
                if(!num.equals("0") && marbles.size()<=(board.length-1)*(board.length-1)-2){
                    marbles.add(count); //A-구슬 개수
                    marbles.add(Integer.parseInt(num));//B-구슬 번호
                }
                num= list.get(i);
                count=1;
            }else{
                count++;
            }
        }

        if(marbles.size()<=(board.length-1)*(board.length-1)-2) {
            marbles.add(count);
            marbles.add(Integer.parseInt(num));
        }


        int idx=0; //marbles 인덱스
        int[] move={3,2,4,1}; //좌하우상 순으로
        int moveLen=0; //움직일 거리

        int nr=(board.length)/2;
        int nc=(board.length)/2;
        while(idx< marbles.size()){
            for(int m=0;m<move.length;m++) {
                if (m == 0 || m == 2) {
                    moveLen++;
                }

                int moveCount = 0;
                while (moveCount < moveLen) {
                    nr += dir[move[m]][0];
                    nc += dir[move[m]][1];

                    nBoard[nr][nc] = marbles.get(idx);
                    idx++;
                    moveCount++;
                    K=idx;

                    if (idx >= marbles.size()) {
                        return nBoard;
                    }
                }
            }
        }

        return nBoard;
    }

    public static void moveAndExplode(){
        //하나 작은 칸이 빈 칸이면, 구슬 이동
        for(int i = 1; i< list.size(); i++){
            if((i-1)!=0 && list.get(i-1).equals("0")){
                list.remove(i-1);
            }
        }

        boolean isExplode=false;
        String num="0";
        int start=0;

        for(int i = 1; i< list.size(); i++){
            if(!list.get(i).equals(num)){
                //4개 이상일 경우
                if((i-start)>=4){
                    //폭발
                    isExplode=true;
                    for(int j=start;j<i;j++){
                        list.remove(start);
                    }
                    answer+=Integer.parseInt(num)*(i-start);
                    i=start;
                }
                num= list.get(i);
                start=i;
            }
        }

        if((list.size()-start)>=4){
            isExplode=true;
            for(int j=start;j< list.size();j++){
                list.remove(start);
            }
            answer+=Integer.parseInt(num)*(list.size()-start);
        }

        if(isExplode){
            moveAndExplode();
        }

    }


    public static ArrayList<String> arrayToList(){
        ArrayList<String> nList=new ArrayList<>();

        int r=(board.length)/2;
        int c=(board.length)/2;
        nList.add(String.valueOf(board[r][c]));

        int count=0; //구술 카운트
        int[] move={3,2,4,1}; //좌하우상 순으로
        int moveLen=0; //움직일 거리

        int nr=r;
        int nc=c;
        while(count<K){
            for(int m=0;m<move.length;m++){
                if(m==0 || m==2) {
                    moveLen++;
                }

                int moveCount=0;
                while(moveCount<moveLen){
                    nr+=dir[move[m]][0];
                    nc+=dir[move[m]][1];

                    nList.add(String.valueOf(board[nr][nc]));
                    moveCount++;
                    count++;

                    if(count==K){
                        return nList;
                    }
                }
            }
        }
        return nList;
    }

    public static void throwIce(int d,int s){
        int nr=(board.length)/2;
        int nc=(board.length)/2;
        for(int dist=0;dist<s;dist++){
            nr+=dir[d][0];
            nc+=dir[d][1];

            if(nr<=0 || nr>=board.length || nc<=0 || nc>= board.length){
                continue;
            }

            board[nr][nc]=0;
        }

    }
}