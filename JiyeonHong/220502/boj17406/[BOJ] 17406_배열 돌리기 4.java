package boj17406;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class Main{
    static int N;
    static int M;
    static int K;
    static int[][] board;
    static List<int[]> rotations;
    static List<int[]> permutationList=new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine()," ");
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        K=Integer.parseInt(st.nextToken());

        board=new int[N][M];
        for(int i=0;i<N;i++){
            String[] s=br.readLine().split(" ");
            for(int j=0;j<M;j++){
                board[i][j]=Integer.parseInt(s[j]);
            }
        }

        rotations=new ArrayList<>();
        for(int i=0;i<K;i++){
            st=new StringTokenizer(br.readLine()," ");
            int r=Integer.parseInt(st.nextToken());
            int c=Integer.parseInt(st.nextToken());
            int s=Integer.parseInt(st.nextToken());
            rotations.add(new int[]{r, c, s});
        }

        System.out.println(solution());
    }

    public static int solution(){
        int answer=Integer.MAX_VALUE;
        //1. 연산 순열 구하기
        int[] arr=new int[K];
        for(int i=0;i<arr.length;i++){
            arr[i]=i;
        }
        permutation(arr,0,K,K);

        //2. 순열 순서로 회전
        //3. 배열 값 구하기
        for(int i=0;i<permutationList.size();i++){
            int[] rotationOrder=permutationList.get(i); //{2,1}
            answer=Math.min(answer,findPermutationMin(rotationOrder));
        }
        return answer;
    }

    public static int findPermutationMin(int[] order){
        int[][] nBoard=copyBoard(board);

        //순열 인덱스 하나의 회전연산하기
        for(int i=0;i<order.length;i++){
             int[] rotation=rotations.get(order[i]);
             //회전
            nBoard=rotate(nBoard,rotation[0],rotation[1],rotation[2]);
         }

        return findRowMin(nBoard);
    }

    public static int findRowMin(int[][] nBoard){
        int min=Integer.MAX_VALUE;
        for(int i=0;i<nBoard.length;i++){
            int sum=0;
            for(int j=0;j<nBoard[i].length;j++){
                sum+=nBoard[i][j];
            }
            min=Math.min(min,sum);
        }
        return min;
    }

    public static int[][] rotate(int[][] origin,int r,int c,int s){
        int[][] newOrigin=copyBoard(origin);
        int[][] dir={{0,1},{1,0},{0,-1},{-1,0}};

        for(int place=s;place>=0;place--){
            int moveTotal=2*place*4;
            int d=0; //방향
            int xStart=r-place-1,xEnd=r+place-1;
            int yStart=c-place-1,yEnd=c+place-1;

            int x=r-place-1,y=c-place-1; //시작 위치
            int moveCnt=0;
            while(moveCnt<moveTotal){
                int nx=x+dir[d%4][0];
                int ny=y+dir[d%4][1];

                if(nx<xStart || nx>xEnd || ny<yStart || ny>yEnd){
                    d++;
                    continue;
                }

                newOrigin[nx][ny]=origin[x][y];
                x+=dir[d%4][0];
                y+=dir[d%4][1];
                moveCnt++;
            }
        }
        return newOrigin;
    }

    public static int[][] copyBoard(int[][] origin){
        int[][] ret=new int[origin.length][origin[0].length];
        for(int i=0;i<origin.length;i++){
            for(int j=0;j<origin[0].length;j++){
                ret[i][j]=origin[i][j];
            }
        }
        return ret;
    }

    public static void permutation(int[] arr, int depth, int n, int r) {
        if (depth == r) {
            permutationList.add(arr);
            return;
        }

        for (int i = depth; i < n; i++) {
            arr=swap(arr, depth, i);
            permutation(arr, depth + 1, n, r);
            arr=swap(arr, depth, i);
        }
    }

    public static int[] swap(int[] arr, int depth, int i) {
        int temp = arr[depth];
        arr[depth] = arr[i];
        arr[i] = temp;
        return arr;
    }
}