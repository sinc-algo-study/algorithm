package live.p2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 팩토리얼을 구하는 함수를 작성하라
 */

public class Main {

    public static long factorial(long num) {
        if(num == 1) {
            return num;
        }else {
            return num * factorial(num - 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long num = Integer.parseInt(br.readLine());
        long facto = factorial(num);
        System.out.println(facto);
    }
}
