package algo220214.boj5582_공통부분문자열;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 *
 * 1. 브루트 포스 가능?
 * -> 모든 부분 문자열을 만들어서 map으로 관리?
 * -> 길이가 N인 문자열에 대해 모든 부분문자열의 개수는 N^2..
 *
 * 문자열의 길이는 최대 4,000..
 * 나올 수 있는 부분문자열은 최대 2 * (4,000 ^ 2) = 3,200만 개
 * -> 찾아보니 java 7 update 6 부터 String.substring 은 O(N).. (그 전까지는 O(1) 이었다고 함)
 * -> 그럼 3200만 * 4000 으로 불가능
 *
 * 2. DP (LCS) - Longest Common Subsequence, Longest Comment Substring
 * Subsequence : 연속된 것만 허용
 * Substring : 불연속한 것도 허용
 *
 * https://www.youtube.com/watch?v=EAXDUxVYquY&ab_channel=Chan-SuShin  ->  Logest Common Substring
 *
 * (그 외 LCS 관련 문제)
 * 백준 9251. LCS
 * 백준 9252. LCS 2
 * 백준 1958. LCS 3
 * 백준 5582. 공통 부분 문자열
 * 백준 15483. 최소 편집
 *
 *
 */

public class Main {

    public static int longestCommonSubsequence(String s1, String s2) {
        int ans = 0;
        int N = s1.length();
        int M = s2.length();

        int[][] dp = new int[N+1][M+1];  // 모든 좌표의 초기값은 0
        for(int i = 1; i <= N; i++) {
            for(int j = 1; j <= M; j++) {
                if(s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                    ans = Math.max(ans, dp[i][j]);
                }
            }
        }

        return ans;
    }

//    public static int longestCommonSubstring(String s1, String s2) {
//        int N = s1.length();
//        int M = s2.length();
//
//        int[][] dp = new int[N+1][M+1];  // 모든 좌표의 초기값은 0
//        for(int i = 1; i <= N; i++) {
//            for(int j = 1; j <= M; j++) {
//                if(s1.charAt(i-1) == s2.charAt(j-1)) {
//                    dp[i][j] = dp[i-1][j-1] + 1;
//                }else {
//                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
//                }
//            }
//        }
//
//        return dp[N][M];
//    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s1 = br.readLine();
        String s2 = br.readLine();
        System.out.println(longestCommonSubsequence(s1, s2));
//        System.out.println(longestCommonSubstring(s1, s2));
    }
}
