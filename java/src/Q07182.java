import java.io.*;
import java.util.*;

public class Q07182 {

    static int [][] dynamic;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader((System.in)));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        dynamic = new int[n+1][k+1];

        System.out.println(bico(n,k));
    }

    static int bico(int n, int k) {
        if (dynamic[n][k]>0){
            return dynamic[n][k];
        }
        if (k==0||n==k){
            return dynamic[n][k] = 1;
        }
        return dynamic[n][k] = bico(n-1,k-1)+bico(n-1,k);
    }
}