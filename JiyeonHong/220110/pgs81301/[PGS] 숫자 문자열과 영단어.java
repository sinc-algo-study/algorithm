package pgs81301;

class Main {
    public static void main(String[] args) {
        String[] arr = { "one4seveneight", "23four5six7", "2three45sixseven" };
        Solution ss = new Solution();
        for (String s : arr) {
            System.out.println(ss.solution(s));
        }
    }
}

class Solution {
    String[] numbers = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" };

    public int solution(String s) {
        int answer = 0;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (s.substring(i, i + 1).matches("[0-9]")) {
                sb.append(s.charAt(i));
            } else {
                int number = makeNumber(s, i);
                sb.append(number);
                i += numbers[number].length() - 1;
            }
        }
        answer = Integer.parseInt(sb.toString());
        return answer;
    }

    public int makeNumber(String s, int start) {
        int number = -1;

        for (int i = 0; i < numbers.length; i++) {
            int end = start + numbers[i].length() < s.length() ? start + numbers[i].length() : s.length();
            if (s.substring(start, end).equals(numbers[i])) {
                number = i;
                break;
            }
        }
        return number;
    }

}