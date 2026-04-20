import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void union(int a, int b, int[] parents, int[] rank) {
        int pa = find(a, parents);
        int pb = find(b, parents);

        if (rank[pa] < rank[pb]) parents[pa] = pb;
        else if (rank[pa] > rank[pb]) parents[pb] = pa;
        else {
            parents[pb] = pa;
            rank[pa]++;
        }
    }

    public static int find(int x, int[] parents) {
        if (parents[x] != x) parents[x] = find(parents[x], parents);
        return parents[x];
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
        int[] rank = new int[n+1];

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; ++i) {
            st = new StringTokenizer(br.readLine());
            int calc_type = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (calc_type == 0) union(a, b, parents, rank);
            else {
                if (find(a, parents) == find(b, parents)) sb.append("YES\n");
                else sb.append("NO\n");
            }
        }
        System.out.println(sb);
    }
}