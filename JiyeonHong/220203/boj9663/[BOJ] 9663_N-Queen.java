package boj9663;

import java.io.*;

class Solution {
    int answer = 0;

    public int solution(int N) {
        int[] board = new int[N];

        putQueen(board, 0);
        return answer;
    }

    public void putQueen(int[] board, int r) {
        if (r == board.length) {
            answer++;
            return;
        }

        for (int c = 0; c < board.length; c++) {
            board[r] = c; // r행 c열에 queen
            if (isNoQueen(board, r)) { // r행 c열에 queen 놓을 수 있으면
                putQueen(board, r + 1);
            }
        }
    }

    public boolean isNoQueen(int[] board, int r) {
        // 같은 행&열, 대각선에 queen 있는지 확인
        for (int i = 0; i < r; i++) {
            if (board[i] == board[r] || r - i == Math.abs(board[r] - board[i])) {
                return false;
            }
        }
        return true;
    }

}

class Main {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Solution s = new Solution();
        System.out.println(s.solution(N));
    }
}
