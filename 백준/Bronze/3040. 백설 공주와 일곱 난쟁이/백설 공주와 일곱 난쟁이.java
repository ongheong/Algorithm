import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int answer = 0;
	static int nums[];
	static int realAns[];
	static int arr[];
	
	public static void main(String[] args) throws Exception { //중복없는조합
		//일곱 숫자의 합이 100이 되는 경우를 찾아라
		Scanner sc = new Scanner(System.in);
		
		arr = new int[9];
		nums = new int[9];
		realAns = new int[9];
		
		for (int i=0; i<9; i++) {
			arr[i] = sc.nextInt();
		}
		recursion(0, 0);
		for (int r : realAns) {
			System.out.println(r);	
		}
	}
	
	static void recursion(int cnt, int start) {
		if (cnt == 7) {
			for(int c : nums) {
				answer += c;
			}
			if (answer == 100) {
				realAns = Arrays.copyOf(nums, 7);
			}
			answer = 0;
			return;
		}
		for (int i =start; i< 9; i++) {
			nums[cnt] = arr[i];
			recursion(cnt+1, i+1);
		}
	}
}
