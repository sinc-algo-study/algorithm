package boj5582;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
/*
dp 사용
- 부분 문자열은 연속하는 문자열
- 문자열 탐색하다가 같은 문자 발견하면
   same[i][j]=sane[i-1][j-1]+1
 */

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String s1=br.readLine();
        String s2=br.readLine();
        System.out.println(solution(s1,s2));
    }

    public static int solution(String s1,String s2){
        int answer=0;
        int[][] same=new int[s1.length()][s2.length()];

        for(int i=0;i<s1.length();i++){
            for(int j=0;j<s2.length();j++){
                if(s1.charAt(i)==s2.charAt(j)){
                    if(i-1>=0 && i-1<s1.length() && j-1>=0 && j-1<s2.length()) {
                        same[i][j] = same[i - 1][j - 1] + 1;
                    }else{
                        same[i][j]=1;
                    }
                }
                answer=Math.max(answer,same[i][j]);
            }

        }
        return answer;
    }
}