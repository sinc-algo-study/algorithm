package boj22945;

import java.util.Arrays;
import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int N=Integer.parseInt(sc.nextLine());
        String[] s=sc.nextLine().split(" ");
        int[] devs=new int[s.length];
        for(int i=0;i<s.length;i++){
            devs[i]=Integer.parseInt(s[i]);
        }
        System.out.println(solution(devs));
    }

    public static int solution(int[] devs){
        int answer=0;
        int s=0;
        int e=devs.length-1;
        while(s<=e){
            answer=Math.max(answer,(e-s-1)*Math.min(devs[s],devs[e]));
            if(devs[s]>devs[e]){
                e--;
            }else{
                s++;
            }
        }
        return answer;
    }
}