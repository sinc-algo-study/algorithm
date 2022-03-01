package algo220221.boj22860_폴더정리;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Node {
    String name;
    int type;
    Node(String name, int type) {
        this.name = name;
        this.type = type;
    }

    public String getName() {
        return name;
    }

    public int getType() {
        return type;
    }
}

public class Main {

    static int N, M, Q;
    static Map<String, ArrayList<Node>> map;
    static ArrayList<String> queryList;
    static ArrayList<int[]> ansList;

    static Set<String> set;
    static int CNT;

    public static void dfs(String folder) {
        ArrayList<Node> nodeList = map.get(folder);
        if(nodeList == null) {
            ansList.add(new int[]{0, 0});
            return;
        }

        for(Node node : nodeList) {
            if(node.getType() == 0) {
                set.add(node.getName());
                CNT += 1;
            }else {
                dfs(node.getName());
            }
        }
    }

    public static void process() {
        for(String folder : queryList) {
            set = new HashSet<>();
            CNT = 0;
            dfs(folder);
            int[] arr = {set.size(), CNT};
            ansList.add(arr);
        }
    }

    public static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new HashMap<>();
        queryList = new ArrayList<>();
        ansList = new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        while(st.countTokens() > 1) {
            String parent = st.nextToken();
            String child = st.nextToken();
            int type = Integer.parseInt(st.nextToken());

            if(map.containsKey(parent)) {
                map.get(parent).add(new Node(child, type));
            }else {
                map.put(parent, new ArrayList<>());
                map.get(parent).add(new Node(child, type));
            }

            st = new StringTokenizer(br.readLine());
        }

        Q = Integer.parseInt(st.nextToken());
        for(int i = 0; i < Q; i++) {
            st = new StringTokenizer(br.readLine(), "/");
            while(st.countTokens() > 1) {  // 어차피 마지막 폴더만 필요
                st.nextToken();
            }
            queryList.add(st.nextToken());
        }
    }

    public static void output() {
        for(int[] ans : ansList) {
            System.out.println(ans[0] + " " + ans[1]);
        }
    }

    public static void main(String[] args) throws IOException {
        init();
        process();
        output();
    }
}

