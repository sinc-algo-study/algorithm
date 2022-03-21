package live.p3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static int getMaxPeak(ArrayList<Integer> list) {
        int max = -1;
        for(int peak : list) {
            max = Math.max(max, peak);
        }
        return max;
    }

    public static ArrayList<Integer> getPeakList(int[] arr) {
        ArrayList<Integer> list = new ArrayList<>();
        for(int i = 0; i < arr.length; i++) {
            if(i == 0) {  // 오른쪽만 보면 됨
                if(arr[i] >= arr[i+1])
                    list.add(arr[i]);
                continue;
            }
            if(i == arr.length - 1) {  // 왼쪽만 보면 됨
                if(arr[i] >= arr[i-1])
                    list.add(arr[i]);
                continue;
            }
            if(arr[i-1] <= arr[i] && arr[i] >= arr[i+1])
                list.add(arr[i]);
        }
        return list;
    }

    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
//        int N = Integer.parseInt(st.nextToken());
//        int[] arr = new int[N];
//
//        st = new StringTokenizer(br.readLine());
//        for(int i = 0; i < N; i++) {
//            arr[i] = Integer.parseInt(st.nextToken());
//        }

        // [39, 33, 24, 15, 12, 7] -> 39
        // [5, 8, 15, 28, 36, 48, 68, 52, 32, 17] -> 68
//        int[] arr1 = {39, 33, 24, 15, 12, 7};
//        int[] arr2 = {5, 8, 15, 28, 36, 48, 68, 52, 32, 17};
//        int[] arr3 = {39, 33, 24, 15, 12, 56, 68, 92, 26, 7};
//        ArrayList<Integer> peakList = getPeakList(arr3);
//        int ans = getMaxPeak(peakList);
//        System.out.println(ans);

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.println("");
    }
}