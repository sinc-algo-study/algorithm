//package boj3687;
//
//import java.io.*;
//import java.util.*;
//
//class Main{
//    public static void main(String[] args) throws IOException {
//        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
//        int testCaseCnt=Integer.parseInt(br.readLine());
//        int[] testCases=new int[testCaseCnt];
//        for(int i=0;i<testCaseCnt;i++){
//            testCases[i]=Integer.parseInt(br.readLine());
//        }
//
//        solution(testCases);
//    }
//
//    public static void solution(int[] testCases){
//        for(int i=0;i<testCases.length;i++){
//            System.out.println(findMin(testCases[i])+" "+findMax(testCases[i]));
//        }
//    }
//
//    public static String findMax(int stick){
//        Map<Integer, int[]> numbers=new HashMap<>();
//        numbers.put(2,new int[]{1});
//        numbers.put(3,new int[]{7});
//        numbers.put(4,new int[]{4});
//        numbers.put(5,new int[]{5,3,2});
//        numbers.put(6,new int[]{9,6,0});
//        numbers.put(7,new int[]{8});
//
//        List<Integer> ret=new ArrayList<>();
//        int cnt=2;
//        while(stick>0){
//            if(cnt>stick){
//                cnt=stick;
//            }
//
//            if(stick-cnt==1){
//                cnt++;
//                continue;
//            }
//
//            stick-=cnt;
//            ret.add(numbers.get(cnt)[0]);
//        }
//
//        Collections.sort(ret,Collections.reverseOrder());
//        StringBuilder sb=new StringBuilder();
//        for(int i=0;i<ret.size();i++){
//            sb.append(ret.get(i));
//        }
//        return sb.toString();
//    }
//
//    public static String findMin(int stick){
//        Map<Integer, int[]> numbers=new HashMap<>();
//        numbers.put(2,new int[]{1});
//        numbers.put(3,new int[]{7});
//        numbers.put(4,new int[]{4});
//        numbers.put(5,new int[]{2,3,5});
//        numbers.put(6,new int[]{0,6,9});
//        numbers.put(7,new int[]{8});
//
//        List<Integer> ret=new ArrayList<>();
//        int cnt=7;
//        while(stick>0){
//            if(cnt>stick){
//                cnt=stick;
//            }
//
//            if(stick-cnt==1){
//                cnt--;
//                continue;
//            }
//
//            stick-=cnt;
//            ret.add(numbers.get(cnt)[0]);
//        }
//
//
//        int zeroCnt=0;
//        for(int i=0;i<ret.size();i++){
//            if(ret.get(i)==0){
//                zeroCnt++;
//            }
//        }
//        if(zeroCnt==ret.size()){
//            ret.remove(0);
//            ret.add(numbers.get(6)[1]);
//        }
//
//        Collections.sort(ret);
//        StringBuilder sb=new StringBuilder();
//        for(int i=0;i<ret.size();i++){
//            sb.append(ret.get(i));
//        }
//        for(int i=0;i<sb.length();i++){
//            if(sb.charAt(i)=='0'){
//                continue;
//            }else{
//                char c=sb.charAt(i);
//                sb.deleteCharAt(i);
//                sb.insert(0,c);
//                break;
//            }
//        }
//        return sb.toString();
//    }
//}