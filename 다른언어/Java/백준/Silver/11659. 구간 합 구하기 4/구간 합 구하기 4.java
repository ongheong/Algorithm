import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[] arr = new int[n+1];
		int[] sumArr = new int[n+1];
		sumArr[0] = arr[0] = 0;
		for (int i = 1; i<n+1; i++) {
			arr[i] = sc.nextInt();
			sumArr[i] = sumArr[i-1] + arr[i]; //입력 배열과 구간합 배열 만들기
		}
		
		for (int i=0; i<m; i++) {
			int start = sc.nextInt();
			int end = sc.nextInt();
			System.out.println(sumArr[end] - sumArr[start-1]);
		}
		
	}
}