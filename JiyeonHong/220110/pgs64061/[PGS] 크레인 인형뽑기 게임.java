package pgs64061;
import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        // 각 열의 맨 위 인형의 위치
        int[] doll = new int[board.length];

        for (int c = 0; c < board.length; c++) {
            for (int r = 0; r < board.length; r++) {
                if (board[r][c] > 0) {
                    doll[c] = r;
                    break;
                }
            }
        }

        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < moves.length; i++) {
            int top = !stack.isEmpty() ? stack.peek() : -1;

            int c = moves[i] - 1;
            int r = doll[c];

            if (top == board[r][c]) {
                stack.pop();
                answer += 2;
            } else if (board[r][c] > 0) {
                stack.push(board[r][c]);
            }

            board[r][c] = 0;
            doll[c] = r + 1 < board.length ? r + 1 : r; // 인덱스 벗어나지 않도록

        }
        return answer;
    }
}

class Main {
    public static void main(String[] args) {
        int[][] board = { { 0, 0, 0, 0, 0 }, { 0, 0, 1, 0, 3 }, { 0, 2, 5, 0, 1 }, { 4, 2, 4, 4, 2 },
                { 3, 5, 1, 3, 1 } };
        int[] moves = { 1, 5, 3, 5, 1, 2, 1, 4 };
        Solution ss = new Solution();
        System.out.println(ss.solution(board, moves));
    }
}