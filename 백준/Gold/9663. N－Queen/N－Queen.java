//남의 코드 보고 풀었으므로 다시 풀기!
import java.util.Scanner;

public class Main {
	private static int N; 
	private static int ans; 
	private static int [] board = new int[15]; //N이 가질 수 있는 최대 크기(1<=N<15)
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		backTracking(0);
		System.out.println(ans);
	}

	private static void backTracking(int row) {
		if (row == N) { //맨 끝 열까지 도착했다면 == 답인 경우라면
			ans++;
			return;
		}
		for (int i=0; i<N; i++) {
			board[row] = i; //체스판의 [row][i]에 퀸 놓아보기
			if (promising(row)) { //해당 위치가 유망하면
				backTracking(row+1); //다음 행 탐색하기
			}
		}
		
	}

	private static boolean promising(int row) {
		for (int i = 0; i<row; i++) { //이전 행들에 놓은 값들과 비교하기
			//queen 공격 조건 : 같은 열이거나, 같은 행이거나, 대각선일 때 --> 전부 해당되지 않아야 유망함
			if (board[i]==board[row] || row - i == Math.abs(board[row] - board[i]))   
				return false;
		}
		return true;
	}
}
