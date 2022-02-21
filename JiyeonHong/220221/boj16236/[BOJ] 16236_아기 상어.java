package boj16236;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Place{
    int r;
    int c;
    int dist;

    Place(int r,int c,int dist){
        this.r=r;
        this.c=c;
        this.dist=dist;
    }
}

class Main{
    static List<int[]>[] fishes=new ArrayList[10]; //크기당 물고기 위치
    static int[][] space;
    static int[][] dir={{-1,0},{0,-1},{0,1},{1,0}};
    static int sharkSize=2;
    static int eatCnt=0;
    static int answer=0;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        for(int i=0;i<fishes.length;i++){
            fishes[i]=new ArrayList<>();
        }

        int N=Integer.parseInt(br.readLine());
        space=new int[N][N];
        for(int i=0;i<N;i++){
            String[] arr=br.readLine().split(" ");
            for(int j=0;j<arr.length;j++){
                int size=Integer.parseInt(arr[j]);
                space[i][j]=size;
                if(size!=0)
                    fishes[size].add(new int[]{i, j});
            }
        }
        solution();
        System.out.println(answer);
    }

    public static void solution(){
        int[] now=fishes[9].get(0);

        List<int[]> canEatPlaces=canEat(now); //먹을 수 있는 물고기 자리
        if(canEatPlaces.size()==0){
            return;
        }else if(canEatPlaces.size()==1){
            int[] dest=canEatPlaces.get(0);
            int minDist=findMinDist(now,dest);
            if(minDist==Integer.MAX_VALUE){ //막혀서 갈 수 없는 경우
                return;
            }

            move(now,dest,minDist);
            solution();
        }else{
            int minDist=Integer.MAX_VALUE;
            int[] distArr=new int[canEatPlaces.size()];
            for(int i=0;i<canEatPlaces.size();i++){
                int[] end=canEatPlaces.get(i);
                distArr[i]=findMinDist(now,end);
                minDist=Math.min(minDist,distArr[i]);
            }

            if(minDist==Integer.MAX_VALUE){ //막혀서 갈 수 없는 경우
                return;
            }

            int[] dest=findUpLeft(canEatPlaces,minDist,distArr);
            move(now,dest,minDist);
            solution();
        }
    }

    public static void move(int[] now, int[] dest,int minDist){
        answer+=minDist;
        eatCnt++;
        if(eatCnt==sharkSize){
            sharkSize++;
            eatCnt=0;
        }
        fishes[space[dest[0]][dest[1]]].remove(dest);

        fishes[9].remove(now);
        space[now[0]][now[1]]=0;

        fishes[9].add(dest);
        space[dest[0]][dest[1]]=9;
    }

    //가장 위,가장 왼쪽 자리 찾는 함수
    public static int[] findUpLeft(List<int[]> canEatPlaces,int minDist,int[] distArr){
        List<int[]> up=new ArrayList<>();
        up.add(new int[]{space.length,space.length});

        for(int i=0;i<distArr.length;i++){
            if(distArr[i]!=minDist){
                continue;
            }
            //minDist일 경우
            int[] cmp=up.get(0); //위 비교
            if(cmp[0]>canEatPlaces.get(i)[0]){
                up.clear();
                up.add(canEatPlaces.get(i));
            }else if(cmp[0]==canEatPlaces.get(i)[0]){
                up.add(canEatPlaces.get(i));
            }
        }

        if(up.size()>0){ //가장 위 물고기가 여러마리일 경우, 열 기준으로 정렬
            up.sort(new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    return o1[1]-o2[1];
                }
            });
        }

        return up.get(0);
    }

    //최소 거리 찾는 함수 (다익스트라)
    public static int findMinDist(int[] start,int[] end){
        int[][] minDist=new int[space.length][space.length];
        for(int i=0;i<minDist.length;i++){
            Arrays.fill(minDist[i],Integer.MAX_VALUE);
        }

        PriorityQueue<Place> pq=new PriorityQueue<>((p1,p2)->{return p1.dist-p2.dist;});
        pq.add(new Place(start[0],start[1],0));

        while(!pq.isEmpty()){
            Place now=pq.poll();

            for(int d=0;d<4;d++){
                int nr=now.r+dir[d][0];
                int nc=now.c+dir[d][1];

                if(nr<0 || nr>=space.length || nc<0 || nc>=space.length){
                    continue;
                }
                if(space[nr][nc]>sharkSize){
                    continue;
                }

                int newDist=now.dist+1;
                if(newDist<minDist[nr][nc]){
                    minDist[nr][nc]=newDist;
                    pq.add(new Place(nr,nc,newDist));
                }
            }
        }

        return minDist[end[0]][end[1]];
    }

    //먹을 수 있는 물고기 자리 찾는 함수
    public static List<int[]> canEat(int[] now){
        int size=sharkSize;
        if(sharkSize>9){
            size=9;
        }

        List<int[]> canEatPlaces=new ArrayList<>();
        for(int i=1;i<size;i++){
            for(int j=0;j<fishes[i].size();j++){
                int[] place=fishes[i].get(j);
                canEatPlaces.add(place);
            }
        }
        return canEatPlaces;
    }
}