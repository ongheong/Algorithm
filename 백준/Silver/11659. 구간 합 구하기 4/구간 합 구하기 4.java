import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[] arr = new int[n+1];
		int[] sumArr = new int[n+1];
		sumArr[0] = arr[0] = 0;
		for (int i = 1; i<n+1; i++) {
			arr[i] = sc.nextInt();
			sumArr[i] = sumArr[i-1] + arr[i];
		}
		
//		for (int i = 1; i<n; i++) { // 구간합 배열 구하기
//			sumArr[i] = sumArr[i-1] + arr[i];
//		}
		
		for (int i=0; i<m; i++) { // 조건 시작
			int start = sc.nextInt();
			int end = sc.nextInt();
			System.out.println(sumArr[end] - sumArr[start-1]);
		}
		
	}

}
