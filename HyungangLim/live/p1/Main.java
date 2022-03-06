package live.p1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 최대공약수, 최소공배수 구하는 함수를 작성하라
 */

public class Main {

    public static int getGCD(int a, int b) {



        return 0;
    }

    public static int getLCM(int min, int max) {
        int lcm = min;
        for(int i = 1; i <= min; i++) {
            if(min % i == 0 && max % i == 0) {
                lcm = i;
            }
        }
        return lcm;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int num1 = Integer.parseInt(st.nextToken());
        int num2 = Integer.parseInt(st.nextToken());
        int min = Math.min(num1, num2);
        int max = Math.max(num1, num2);

        int lcm = getLCM(min, max);
        int gcd = getGCD(min, max);
    }
}
