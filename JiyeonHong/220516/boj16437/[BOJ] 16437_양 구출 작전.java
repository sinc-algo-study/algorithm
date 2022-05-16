package boj16437;

import java.io.*;
import java.util.*;

class Island{
    int num;
    String who;
    int total;

    public Island(int num,String who,int total){
        this.num=num;
        this.who=who;
        this.total=total;
    }
}

class Main{
    static List<Island>[] tree;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());

        tree=new ArrayList[N+1];
        for(int i=0;i<N+1;i++){
            tree[i]=new ArrayList<>();
        }

        for(int i=2;i<=N;i++){
            StringTokenizer st=new StringTokenizer(br.readLine()," ");
            String t=st.nextToken();
            int a=Integer.parseInt(st.nextToken());
            int p=Integer.parseInt(st.nextToken());
            tree[p].add(new Island(i,t,a));
        }

        System.out.println(solution());
    }

    /*
    단위 주의 : int 범위 벗어남
     */
    public static long solution(){
        long answer=0;

        boolean[] visited=new boolean[tree.length];
        //1번 섬부터 시작
        Island now=new Island(1,"S",0);
        answer+=dfs(now,visited);


        return answer;
    }

    /*
    leaf 노드를 탐색하며 양의 개수 리턴
    늑대인 경우 : cnt<=0(양이 늑대한테 모두 잡아먹힌 경우) 에는 0 리턴
                cnt>0(살아남은 양이 있는 경우)에는 cnt 리턴
    양인 경우 : cnt+양의 개수 리턴
     */
    public static long dfs(Island now,boolean[] visited){
        long cnt=0;
        visited[now.num]=true;

        for(int i=0;i<tree[now.num].size();i++){
            Island next=tree[now.num].get(i);
            if(!visited[next.num]){
                cnt+=dfs(next,visited);
            }
        }

        if(now.who.equals("W")){
            cnt-=now.total;
            if(cnt<0) cnt=0;
        }else{
            cnt+=now.total;
        }
        return cnt;
    }
}