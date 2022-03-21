package other.sk220312.p3;

class Solution {

    public int solution(int width, int height, int[][] diagonals) {
        int answer = 0;



        return answer;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

//        int width = 2;
//        int height = 2;
//        int[][] diagonals = {{1,1}, {2,2}};

//        int width = 1;
//        int height = 1;
//        int[][] diagonals = {{1,1}};

        int width = 51;
        int height = 37;
        int[][] diagonals = {{17,19}};

        long ans = sol.solution(width, height, diagonals);
        System.out.println(ans);
    }
}
