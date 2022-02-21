package boj22860;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main{
    static List<String>[] folders; //하위 폴더명,파일명
    static Map<String,Integer> foldersIdx; //folders에서 폴더 이름의 인덱스
    static Set<String> files;
    static int count=0;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String s=br.readLine();
        int N=Integer.parseInt(s.split(" ")[0]);
        int M=Integer.parseInt(s.split(" ")[1]);

        folders=new ArrayList[N+1];
        for(int i=0;i<folders.length;i++){
            folders[i]=new ArrayList<>();
        }

        foldersIdx=new HashMap<>();
        foldersIdx.put("main",0);
        for(int i=0;i<N+M;i++){
            String[] name=br.readLine().split(" ");

            //배열 idx 추가
            if(!foldersIdx.containsKey(name[0])){
                foldersIdx.put(name[0],foldersIdx.size());
            }

            if(!foldersIdx.containsKey(name[1]) && name[2].equals("1") ){ //폴더면
                foldersIdx.put(name[1],foldersIdx.size());
            }

            folders[foldersIdx.get(name[0])].add(name[1]);
        }


        StringBuilder sb=new StringBuilder();
        int Q=Integer.parseInt(br.readLine());
        for(int i=0;i<Q;i++){
            String[] route= br.readLine().split("/");

            String last=route[route.length-1];//경로 마지막 폴더
            files=new HashSet<>();
            count=0;
            //마지막 경로의 하위 폴더 탐색
            search(foldersIdx.get(last));

            sb.append(files.size()+" "+count+"\n");
        }

        System.out.println(sb.toString());
    }

    public static void search(int now){
        for(int i=0;i<folders[now].size();i++){
            String name=folders[now].get(i);
            if(!foldersIdx.containsKey(name)){//파일이면
                files.add(name);
                count++;
            }else{
                search(foldersIdx.get(name));
            }
        }
    }
}