package boj11054;

import java.util.*;
/*
r_dp[0] = {1} : 길이 1
r_dp[1] = {1, 5} : 길이 2
r_dp[2] = {1, 2} : 길이 2
r_dp[3] = {1} : 길이 1
r_dp[4] = {1, 2, 4} : 길이 3
r_dp[5] = {1, 2, 3} : 길이 3
r_dp[6] = {1, 2, 3, 4} : 길이 4
r_dp[7] = {1, 2, 3, 4, 5} : 길이 5
r_dp[8] = {1, 2} : 길이 2
r_dp[9] = {1} : 길이 1

l_dp[9] = {1} : 길이 1
l_dp[8] = {1, 2} : 길이 2
l_dp[7] = {1, 2, 5} : 길이 3
l_dp[6] = {1, 2, 4} : 길이 3
l_dp[5] = {1, 2, 3} : 길이 3
l_dp[4] = {1, 2, 3, 4} : 길이 4
l_dp[3] = {1} : 길이 1
l_dp[2] = {1, 2} : 길이 2
l_dp[1] = {1, 2, 3, 4, 5} : 길이 5
l_dp[0] = {1} : 길이 1


    1 5 2 1 4 3 4 5 2 1
rdp 1 2 2 1 3 3 4 5 2 1
ldp 1 5 2 1 4 3 3 3 2 1

 */
class Main{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int N=Integer.parseInt(sc.nextLine());
        int[] arr=new int[N];
        String[] s=sc.nextLine().split(" ");
        for(int i=0;i<N;i++){
            arr[i]=Integer.parseInt(s[i]);
        }
        System.out.println(solution(arr));
    }

    public static int solution(int[] arr){
        int answer=0;
        int[] rdp=new int[arr.length]; //오른쪽부터 제일 긴 부분수열의 길이
        int[] ldp=new int[arr.length]; //왼쪽부터 제일 긴 부분 수열의 길이

        for(int i=0;i<rdp.length;i++){
            rdp[i]=findRdp(rdp,arr,i);
        }

        for(int i=ldp.length-1;i>=0;i--){
            ldp[i]=findLdp(ldp,arr,i);
        }

        for(int i=0;i<arr.length;i++){
            answer=Math.max(answer,rdp[i]+ldp[i]-1); //자기 자신 2번 포함해서 -1
        }

        return answer;
    }

    public static int findRdp(int[] rdp, int[] arr,int idx){
        int ret=1;
        for(int i=0;i<idx;i++){
            if(arr[i]<arr[idx]){
                ret=Math.max(ret,rdp[i]+1);
            }
        }
        return ret;
    }

    public static int findLdp(int[] ldp,int[] arr,int idx){
        int ret=1;
        for(int i=arr.length-1;i>idx;i--){
            if(arr[i]<arr[idx]){
                ret=Math.max(ret,ldp[i]+1);
            }
        }
        return ret;
    }

}