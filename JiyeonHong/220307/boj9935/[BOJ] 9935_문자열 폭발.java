package boj9935;

import java.util.Scanner;
import java.util.Stack;
/*
스택 이용
1. 문자열 0번째 문자부터 스택에 넣으면서
2. 만약 stack size >= 폭발 문자열 길이 이면
3. stack에서 폭발 문자열 길이만큼 문자열 꺼내서
4. 같으면 stack에서 pop
 */
class Main{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String s=sc.nextLine();
        String blow=sc.nextLine();


        Stack<Character> stack=new Stack<>();
        for(int i=0;i<s.length();i++){
            stack.push(s.charAt(i));
            if(stack.size()>=blow.length() && isBlowExist(stack,blow)){
                for(int j=0;j<blow.length();j++){ //stack에서 꺼내기
                    stack.pop();
                }
            }
        }

        StringBuilder sb=new StringBuilder();
        while (!stack.isEmpty()){
            sb.append(stack.pop());
        }


        s=sb.length()==0?"FRULA":sb.reverse().toString();
        System.out.println(s);
    }

    public static boolean isBlowExist(Stack<Character> stack, String blow){
        for(int i=stack.size()-blow.length();i<stack.size();i++){
            if(stack.get(i) != blow.charAt( i+blow.length()- stack.size() )){
                return false;
            }
        }
        return true;
    }
}