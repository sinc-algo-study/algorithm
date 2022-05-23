package boj1052;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main{
    static boolean[] alphabet=new boolean[26];
    static String[] words;
    static int answer=0;

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine()," ");
        int N=Integer.parseInt(st.nextToken());
        int K=Integer.parseInt(st.nextToken());
        words=new String[N];
        for(int i=0;i<N;i++){
            words[i]=br.readLine();
        }
        System.out.println(solution(words,K));
    }

    public static int solution(String[] words,int K){
        alphabet['a'-'a']=true;
        alphabet['n'-'a']=true;
        alphabet['t'-'a']=true;
        alphabet['i'-'a']=true;
        alphabet['c'-'a']=true;
        if(K<5){
            return 0;
        }else{
            dfs(0,0,K-5);
        }
        return answer;
    }

    public static void dfs(int now,int count, int K){
        if(count==K){
            answer=Math.max(answer,countCanReadWord());
            return;
        }

        for(int i=now;i<26;i++){
            if(alphabet[i]==false){
                alphabet[i]=true;
                dfs(i,count+1,K);
                alphabet[i]=false;
            }
        }
    }

    public static int countCanReadWord(){
        int count=0;
        for(int i=0;i<words.length;i++){
            count++;
            for(int j=0;j<words[i].length();j++){
                if(alphabet[words[i].charAt(j)-'a']==false){
                    count--;
                    break;
                }
            }
        }
        return count;
    }

}