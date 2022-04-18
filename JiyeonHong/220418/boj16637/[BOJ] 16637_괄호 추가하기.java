package boj16637;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;

class Main{
    static List<Integer> n=new ArrayList<>();
    static List<Character> o=new ArrayList<>();
    static int answer=Integer.MIN_VALUE;

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int N=Integer.parseInt(sc.nextLine());
        String nums=sc.nextLine();
        System.out.println(solution(nums));
    }

    public static int solution(String nums){
        for(int i=0;i<nums.length();i++){
            char c=nums.charAt(i);
            if(c=='+' || c=='-' || c=='*'){
                o.add(c);
            }else{
                n.add(Character.getNumericValue(c));
            }
        }
        dfs(0,n.get(0));
        return answer;
    }

    public static void dfs(int idx,int sum){
        if(idx==o.size()){
            answer=Math.max(answer,sum);
            return;
        }
        dfs(idx+1,calculate(o.get(idx),sum,n.get(idx+1))); //괄호 없이
        if(idx+2<n.size()){
            dfs(idx+2,calculate(o.get(idx),sum,calculate(o.get(idx+1),n.get(idx+1),n.get(idx+2)))); //괄호 치고
        }

    }

    public static int calculate(char op,int n1,int n2){
        int ret=0;
        if(op=='+'){
            ret=n1+n2;
        }else if(op=='-'){
            ret=n1-n2;
        }else{
            ret=n1*n2;
        }
        return ret;
    }

    //    public static int solution(String nums){
//        //[][0]:괄호 안 했을 때, [][1]:괄호 했을 때
//        int[][] dp=new int[nums.length()-nums.length()/2][2];
//        dp[0][0]=0;
//        dp[0][1]=(int)(nums.charAt(0)-'0');
//        for(int i=0;i<nums.length();i++){
//            char c=nums.charAt(i);
//            //[i][0] : 괄호 한 경우+안한경우 / 괄호 안한경우+안한경우 중 최대값
//            //이전에 괄호 안한 경우(dp[i-1][0]) *연산자* 숫자
//            //이전에 괄호 한 경우(dp[i-1][1]) *연산자* 숫자
//            //[i][1] : 이전에 괄호 안한 경우+괄호 한 경우
//            //Math.max([i-2][0],[i-2][1]) *전 연산자*  괄호 한 경우
//
//            if(c=='+' || c=='-' || c=='*'){
//                int n1=(int)(nums.charAt(i-1)-'0');
//                int n2=(int)(nums.charAt(i+1)-'0');
//                int idx=(i+1)/2;
//
//                dp[idx][0]=Math.max(calculate(c,dp[idx-1][0],n2),calculate(c,dp[idx-1][1],n2));
//                char op=i-2<0?'+':nums.charAt(i-2);
//                int idxMinus2Max=idx-2<0?0:Math.max(dp[idx-2][0],dp[idx-2][1]);
//                dp[idx][1]=calculate(op,idxMinus2Max,calculate(c,n1,n2));
//
//            }
//        }
//        return Math.max(dp[dp.length-1][0],dp[dp.length-1][1]);
//    }
}

