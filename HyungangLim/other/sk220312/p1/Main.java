package other.sk220312.p1;

import java.util.PriorityQueue;

//class Coin implements Comparable<Coin> {
//    int value, cost;  // 동전의 액면가, 생산단가
//    int num;  // 가성비. 적절한 네이밍이 안 떠오름..
//    Coin(int value, int cost) {
//        this.value = value;
//        this.cost = cost;
//        int div = 1000 / value;  // 모든 동전의 공배수인 1000을 기준으로 가성비 계산
//        num = (div * value) - (div * cost);
//    }
//
//    // value = 1000으로 맞춘 차액을 기준으로 정렬
//
//    @Override
//    public int compareTo(Coin o) {
//        if(this.num != o.num) {
//            return o.num - this.num;
//        }else{
//            // 사실 차액이 같으면 어떤 동전을 사용해도 상관없음
//            // 사용한 동전의 개수는 신경쓰지 않는다
//            return o.value - this.value;
//        }
//    }
//}
//
//class Solution {
//    public int solution(int money, int[] costs) {
//        int answer = 0;
//
//        // 1, 5, 10, 50, 100, 500
//        // 최소비용으로 money 를 만들어야 함
//
//        // 생산단가 - 화폐단위 가 가장 큰 놈부터 사용할 수 있는 만큼 최대한 사용
//
//        PriorityQueue<Coin> pq = new PriorityQueue<>();
//        pq.add(new Coin(1, costs[0]));
//        pq.add(new Coin(5, costs[1]));
//        pq.add(new Coin(10, costs[2]));
//        pq.add(new Coin(50, costs[3]));
//        pq.add(new Coin(100, costs[4]));
//        pq.add(new Coin(500, costs[5]));
//
//        // 가성비가 큰 동전 먼저 사용한다
//        //       값   단가  가성비
//        // (1)   1,   2   : -1   ->  1000, 2000 : -1000
//        // (5)   5,   11  : -6   ->  1000, 2200 : -1200
//        // (10)  10,  20  : -10  ->  1000, 2000 : -1000
//        // (50)  50,  100 : -50  ->  1000, 2000 : -1000
//        // (100) 100, 200 : -100 ->  1000, 2000 : -1000
//        // (500) 500, 600 : -100 ->  1000, 1200 : -200
//
//        int target = money;
//        while(!pq.isEmpty()) {
//            if(target == 0) break;
//
//            Coin s = pq.poll();
//            int div = target / s.value;
//
//            target -= div * s.value;
//            answer += div * s.cost;
//
//        }
//
//        return answer;
//    }
//}
//
//public class Main {
//    public static void main(String[] args) {
//        Solution sol = new Solution();
////        int money = 4578;
////        int[] costs = {1, 4, 99, 35, 50, 1000};
//        int money = 1999;
//        int[] costs = {2, 11, 20, 100, 200, 600};
//        int ans = sol.solution(money, costs);
//        System.out.println(ans);
//    }
//}


class Solution {
    public int solution(int money, int[] costs) {
        int answer = 0;

        int[] coins = {1, 5, 10, 50, 100, 500};
        int[][] dp = new int[costs.length][money + 1];
        for(int i = 0; i <= money; i++) {
            dp[0][i] = costs[0] * i;
        }

        for(int i = 1; i < costs.length; i++) {
            for(int j = 1; j <= money; j++) {
                dp[i][j] = dp[i-1][j];
                if(j - coins[i] >= 0) {
                    dp[i][j] = Math.min(dp[i][j], dp[i][j - coins[i]] + costs[i]);
                }
            }
        }

        answer = dp[5][money];
        return answer;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        // 2308
        int money = 4578;
        int[] costs = {1, 4, 99, 35, 50, 1000};

        // 2798
//        int money = 1999;
//        int[] costs = {2, 11, 20, 100, 200, 600};
        int ans = sol.solution(money, costs);
        System.out.println(ans);
    }
}
