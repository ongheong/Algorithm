import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static int[] numbers;
	static int[] ans;
	static StringBuilder sb;
	
	public static void main(String[] args) throws Exception {
		//System.setIn(new FileInputStream("test.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		sb = new StringBuilder();
//		Scanner sc = new Scanner(System.in);
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		numbers = new int[N]; //전체 배열 개수
		ans = new int[M]; //조합의 요소 개수
		for (int i = 0; i<N; i++) {
			numbers[i] = i;
		}
		recursion(0);
		System.out.println(sb.toString());
	}
	static void recursion(int count) {
		if (count == M) {
			for (int i : ans) {
//				System.out.print((i+1)+" ");
				sb.append(i+1)
				  .append(' ');
			}
			//System.out.println();
			sb.append('\n'); //작은 따옴표가 메모리를 덜 차지함!
			return;
		}
		for (int i=0; i < N; i++) {
			ans[count] = numbers[i];
			recursion(count+1);
		}
	}
}
