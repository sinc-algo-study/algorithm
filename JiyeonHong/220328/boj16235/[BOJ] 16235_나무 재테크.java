package boj16235;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Tree{
    int r;
    int c;
    int age;

    public Tree(int r,int c,int age){
        this.r=r;
        this.c=c;
        this.age=age;
    }

}

class Main{
    static LinkedList<Tree> trees; //위치당 나무나이들
    static int[][] foods; //양분
    static int N,M,K;
    static int[][] A;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String[] nmk=br.readLine().split(" ");
        N=Integer.parseInt(nmk[0]);
        M=Integer.parseInt(nmk[1]);
        K=Integer.parseInt(nmk[2]);

        A=new int[N][N];
        for(int i=0;i<N;i++){
            String[] arr=br.readLine().split(" ");
            for(int j=0;j<arr.length;j++){
                A[i][j]=Integer.parseInt(arr[j]);
            }
        }

        foods=new int[N][N];
        for(int i=0;i<N;i++){
            Arrays.fill(foods[i],5);
        }

        trees=new LinkedList<>();
        for(int i=0;i<M;i++){
            String[] arr=br.readLine().split(" ");
            int x=Integer.parseInt(arr[0]);
            int y=Integer.parseInt(arr[1]);
            int z=Integer.parseInt(arr[2]);
            trees.add(new Tree(x-1,y-1,z));
        }

        System.out.println(solution());
    }

    public static int solution(){
        int answer=0;
        for(int year=0;year<K;year++){
            List<Tree> dead=new ArrayList<>();
            //봄
            Iterator<Tree> it=trees.iterator();
            while(it.hasNext()){
                Tree tree=it.next();
                if(foods[tree.r][tree.c]>=tree.age){
                    foods[tree.r][tree.c]-=tree.age;
                    tree.age+=1;
                }else{
                    it.remove();
                    dead.add(tree);
                }
            }

            //여름
            for(int i=0;i<dead.size();i++){
                Tree tree=dead.get(i);
                foods[tree.r][tree.c]+=tree.age/2;
            }

            //가을
            List<Tree> babyTrees=new ArrayList<>();
            it=trees.iterator();
            while(it.hasNext()){
                Tree tree=it.next();
                if(tree.age%5==0){ //번식
                    babyTrees.addAll(growWood(tree));
                }
            }
            trees.addAll(0,babyTrees);

            //겨울
            for(int i=0;i<foods.length;i++){
                for(int j=0;j<foods[i].length;j++){
                    foods[i][j]+=A[i][j];
                }
            }
        }

        answer=trees.size();
        return answer;
    }

    public static List<Tree> growWood(Tree tree){
        List<Tree> babyTrees=new ArrayList<>();
        int[][] dir={{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
        for(int i=0;i<dir.length;i++){
            int nr=tree.r+dir[i][0];
            int nc=tree.c+dir[i][1];

            if(nr<0 || nr>=N || nc<0 || nc>=N){
                continue;
            }

            babyTrees.add(new Tree(nr,nc,1));
        }
        return babyTrees;
    }
}