package boj14938;

import java.io.*;
import java.util.*;
class Road{
    int num;
    int len;

    public Road(int num,int len){
        this.num=num;
        this.len=len;
    }
}

class Main{
    static List<Road>[] roads;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine()," ");
        int n=Integer.parseInt(st.nextToken());
        int m=Integer.parseInt(st.nextToken());
        int r=Integer.parseInt(st.nextToken());
        roads=new ArrayList[n+1];
        for(int i=0;i<roads.length;i++){
            roads[i]=new ArrayList<>();
        }

        int[] items=new int[n+1];
        st=new StringTokenizer(br.readLine()," ");
        for(int i=1;i<n+1;i++){
            items[i]=Integer.parseInt(st.nextToken());
        }

        for(int i=0;i<r;i++){
            st=new StringTokenizer(br.readLine()," ");
            int a=Integer.parseInt(st.nextToken());
            int b=Integer.parseInt(st.nextToken());
            int l=Integer.parseInt(st.nextToken());
            roads[a].add(new Road(b,l));
            roads[b].add(new Road(a,l));
        }
        System.out.println(solution(m,items));
    }

    public static int solution(int m,int[] items){
        int answer=0;
        int[][] minDist=new int[roads.length][roads.length];
        for(int i=1;i< roads.length;i++){
            minDist[i]=findMinDist(i);
        }


        for(int i=1;i<roads.length;i++){
            int itemSum=0;
            for(int j=1;j< roads.length;j++){
                if(minDist[i][j]<=m){
                    itemSum+=items[j];
                }
            }
            answer=Math.max(answer,itemSum);
        }
        return answer;
    }

    public static int[] findMinDist(int start){
        PriorityQueue<Road> pq=new PriorityQueue<>(new Comparator<Road>() {
            @Override
            public int compare(Road o1, Road o2) {
                return o1.len-o2.len;
            }
        });
        int[] minDist=new int[roads.length];
        Arrays.fill(minDist,Integer.MAX_VALUE);
        pq.add(new Road(start,0));
        minDist[start]=0;

        while(!pq.isEmpty()){
            Road now=pq.poll();
            for(int i=0;i<roads[now.num].size();i++){
                Road next=roads[now.num].get(i);
                if(now.len+next.len<minDist[next.num]){
                    minDist[next.num]=now.len+next.len;
                    pq.add(new Road(next.num,now.len+next.len));
                }
            }
        }
        return minDist;
    }

}