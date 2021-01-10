import java.io.*;
import java.util.*;

public class 주유소 {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		long [] road = new long [n-1];
		long [] oil = new long [n];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i=0; i<n-1; i++) {
			road[i] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());
		for(int i=0; i<=n-1; i++) {
			oil[i] = Integer.parseInt(st.nextToken());
		}
		
		long ans = road[0] * oil[0];
		int now = 0;
		int next = 1;
		
		while(next < n-1) {
			if(oil[now] < oil[next]) {
				ans += (oil[now] * road[next]);
			}
			else {
				ans += (oil[next] * road[next]);
				now = next;
			}
			next++;
		}
		System.out.println(ans);
	}
}