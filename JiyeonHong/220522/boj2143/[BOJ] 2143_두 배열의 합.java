package boj2143;

import java.io.*;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int T=Integer.parseInt(br.readLine());

        int n=Integer.parseInt(br.readLine());
        int[] arrN=new int[n];
        StringTokenizer st=new StringTokenizer(br.readLine()," ");
        for(int i=0;i<n;i++){
            arrN[i]=Integer.parseInt(st.nextToken());
        }

        int m=Integer.parseInt(br.readLine());
        int[] arrM=new int[m];
        st=new StringTokenizer(br.readLine()," ");
        for(int i=0;i<m;i++){
            arrM[i]=Integer.parseInt(st.nextToken());
        }

        System.out.println(solution(arrN,arrM,T));
    }

    public static long solution(int[] arrN,int[] arrM,int T){
        long answer=0;
        /*
        부분합 구하는 최악의 경우
        (1+2+3+...+999+1000)=(1000*1001)/2=500500
         */
        List<Integer> sumN=new ArrayList<>(); //부분합 배열
        List<Integer> sumM=new ArrayList<>(); //부분합 배열

        // 1 2 3 4
        // 1 1+2 1+2..3
        // 2 2+3 2+3+4
        for(int i=0;i<arrN.length;i++){
            int sum=0;
            for(int j=i;j<arrN.length;j++){
                sum+=arrN[j];
                sumN.add(sum);
            }
        }

        for(int i=0;i<arrM.length;i++){
            int sum=0;
            for(int j=i;j<arrM.length;j++){
                sum+=arrM[j];
                sumM.add(sum);
            }
        }

        Collections.sort(sumN);
        Collections.sort(sumM);

        answer=findT(sumN,sumM,T);
        return answer;
    }

    //투포인터
    public static long findT(List<Integer> sumN,List<Integer> sumM,int T){
        long count=0;

        int pn=0;
        int pm=sumM.size()-1;

        while(pn<sumN.size() && pm>=0){
            int n=sumN.get(pn);
            int m=sumM.get(pm);

            if(n+m==T){
                long ncnt=0;
                long mcnt=0;

                while(pn<sumN.size() && sumN.get(pn)==n){ //같은 숫자 나오는 경우 세기
                    pn++;
                    ncnt++;
                }
                while(pm>=0 && sumM.get(pm)==m){ //같은 숫자 나오는 경우 세기
                    pm--;
                    mcnt++;
                }
                count+=(ncnt*mcnt);
            }else if(n+m>T){
                pm--;
            }else if(n+m<T){
                pn++;
            }
        }
        return count;
    }

}