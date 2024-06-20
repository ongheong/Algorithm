import java.io.FileInputStream;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int N, M;
	static int[] numbers; //나중에 입력 코드로 바꾸기
	static boolean[] selected;
	static int[] ans;
	
	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		numbers = new int[N]; //전체 배열 개수
		ans = new int[M]; //조합의 요소 개수
		selected = new boolean[N];
		for (int i = 0; i<N; i++) {
			numbers[i] = i;
		}
		recursion(0);
	}
	static void recursion(int count) {
		if (count == M) {
			for (int i : ans) {
				System.out.print((i+1)+" ");
			}
			System.out.println();
			return;
		}
		for (int i=0; i < N; i++) {
			if (!selected[i]) {
				selected[i] = true;
				ans[count] = numbers[i];
				recursion(count+1);
				selected[i] = false;
			}
		}
	}
}