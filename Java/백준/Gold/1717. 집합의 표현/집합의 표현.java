import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void union(int a, int b, int[] parents) {
        int pa = find(a, parents);
        int pb = find(b, parents);

        if (pa < pb) parents[pb] = pa;
        if (pa > pb) parents[pa] = pb;
    }

    public static int find(int x, int[] parents) {
        if (parents[x] != x) parents[x] = find(parents[x], parents);
        return parents[x];
    }

    public static void calc(int type, int a, int b, int[] parents) {
        if (type == 0) union(a, b, parents);
        else {
            if (find(a, parents) == find(b, parents)) System.out.println("YES");
            else System.out.println("NO");
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] parents = new int[n+1];
        for (int s = 0; s <= n; ++s) {
            parents[s] = s;
        }

        for (int i = 0; i < m; ++i) {
            st = new StringTokenizer(br.readLine());
            int calc_type = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            calc(calc_type, a, b, parents);
        }
    }
}