import java.util.Scanner;

public class Main {
	private static int N;
	private static int K;
	private static int[] coins;
	private static int answer;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		K = sc.nextInt();
		coins = new int[N];
		
		for (int i = 0; i<N; i++) {
			coins[i] = sc.nextInt();
		}
		for (int i = N-1; i>-1; i--) {
			if (coins[i] <= K) {
				answer += K / coins[i];
				K %= coins[i];
			}
		}
		System.out.println(answer);
	}

}
