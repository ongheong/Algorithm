import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
	static int input[];
	static int N, M;
	static int select[];
	static int sum;
	public static void main(String[] args) throws Exception {
		//N장의 카드 중에서 3개를 뽑고, M보다 작으면서 더한 값이 가장 크면 출력
		//--> 조합(중복x)
		//System.setIn(new FileInputStream("test.txt"));
		Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = sc.nextInt();
		M = sc.nextInt();
		input = new int[N];
		select = new int[3];
		//StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i=0; i<N; i++) {
			input[i] = sc.nextInt();
		}
//		for(int i = 0; i<N; i++) {
//			input[i] = Integer.parseInt(st.nextToken());
//		}
		recursion(0, 0);
		System.out.println(sum);
		sc.close();
	}
	private static void recursion(int cnt, int start) {
		if (cnt == 3) {
			int tmp = 0;
			for (int s : select) {
				tmp += s;
			}
			if (tmp > sum && tmp <= M) sum = tmp;
			return;
		}
		for (int i=start; i<N; i++) {
			select[cnt] = input[i];
			recursion(cnt+1, i+1);
		}
	}

}
