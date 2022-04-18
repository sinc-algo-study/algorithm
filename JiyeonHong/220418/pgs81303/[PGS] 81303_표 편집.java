package pgs81303;

import java.util.*;
class Solution {
    public String solution(int n, int k, String[] cmd) {
        String answer = "";
        int total=n;

        Stack<Integer> stack=new Stack<>();
        for(int i=0;i<cmd.length;i++){
            String[] arr=cmd[i].split(" ");
            if(arr[0].equals("U")){
                k-=Integer.parseInt(arr[1]);
            }else if(arr[0].equals("D")){
                k+=Integer.parseInt(arr[1]);
            }else if(arr[0].equals("C")){
                stack.push(k);
                if(k==total-1){
                    k--;
                }
                total--;
            }else if(arr[0].equals("Z")){
                int restore=stack.pop();
                if(restore<=k) k++;
                total++;
            }
        }


        StringBuilder sb=new StringBuilder();
        for(int i=0;i<total;i++){
            sb.append("O");
        }

        while(!stack.isEmpty()){
            sb.insert(stack.pop(),"X");
        }
        answer=sb.toString();
        return answer;
    }

}