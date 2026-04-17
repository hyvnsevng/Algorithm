import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int idx = 0;
        int[] arr = new int[n];
        while (st.hasMoreTokens()) {
            arr[idx++] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(arr);

        int answer = 0;
        for (int i = 0; i < n; ++i) {
            int target = arr[i];
            int l = 0, r = n - 1;

            while (l < r) {
                if (l == i) {
                    l++;
                    continue;
                }
                if (r == i) {
                    r--;
                    continue;
                }
                
                int sum = arr[l] + arr[r];
                if (sum == target) {
                    answer++;
                    break;
                }

                if (sum < target) l++;
                else r--;
            }
        }

        System.out.println(answer);
    }
}