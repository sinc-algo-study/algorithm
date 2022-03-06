package algo220307.boj9935_문자열폭발;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

/**
 * 브루트포스는 N^2 .. = 10^12
 * 스택을 이용한 O(NM) 풀이
 */

public class Main {

    static String input, bomb;
    static Stack<Character> stk = new Stack<>();
    static StringBuilder sb = new StringBuilder();

    public static void process() {
        for(int i = 0; i < input.length(); i++) {
            char ch = input.charAt(i);
            stk.push(ch);

            if(stk.size() >= bomb.length()) {
                boolean hasBomb = true;
                for(int j = 0; j < bomb.length(); j++) {
                    if(stk.get(stk.size() - bomb.length() + j) != bomb.charAt(j)) {
                        hasBomb = false;
                        break;
                    }
                }
                // bomb 삭제
                if(hasBomb) {
                    for(int j = 0; j < bomb.length(); j++) {
                        stk.pop();
                    }
                }
            }
        }

        // 메모리 초과
//        Stack<Character> temp = new Stack<>();
//        while(!stk.isEmpty()) {
//            temp.push(stk.pop());
//        }
//        while(!temp.isEmpty()) {
//            ans += temp.pop();
//        }
        for(char ch : stk) {
            sb.append(ch);
        }
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        input = br.readLine();
        bomb = br.readLine();
    }

    public static void output() {
        System.out.println(sb.length() == 0 ? "FRULA" : sb.toString());
    }

    public static void main(String[] args) throws IOException {
        init();
        process();
        output();
    }
}
