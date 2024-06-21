import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
	static int [][] ingredients;
	static boolean visited[] ;
	static int N;
	static int sour;
	static int bitter;
	static int answer = 100000000;
	
	
	public static void main(String[] args) throws FileNotFoundException {
		//전체 신맛 ==> 신맛의 곱
		//전체 쓴맛 ==> 쓴맛의 합
		//신맛 + 쓴맛이 0에 가까운 수를 출력
		//중복, 순서 신경 안씀 -> 조합(중복x) --> 주어진 배열로 만들 수 있는 모든 부분집합 구하기
		//System.setIn(new FileInputStream("test.txt"));
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		ingredients = new int[N][2];
		visited = new boolean[N];
		for (int i = 0; i<N; i++) {
			ingredients[i][0] = sc.nextInt();
			ingredients[i][1] = sc.nextInt();
		}
		makeSubset(0);
		System.out.println(answer);
		sc.close();
	}
	//공집합을 빼야함...!
	private static void makeSubset(int cnt) {
		if (cnt == N) {
			for (int i=0; i<N; i++) {
				if (visited[i]) {
					//신맛쓴맛계산
					if (sour == 0) sour = ingredients[i][0];
					else sour *= ingredients[i][0];
					bitter += ingredients[i][1];
				}
			}
			if (sour != 0 && bitter != 0) {
				int tmp = Math.abs(sour - bitter);
				if (answer > tmp) answer = tmp;
				sour = 0;
				bitter = 0;
			}
			return;
		}
		visited[cnt] = false;
		makeSubset(cnt+1);
		visited[cnt] = true;
		makeSubset(cnt+1);
	}

}
