import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static int changeNum(int i) {
		if (i == 1) return 0;
		return 1;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int []switches = new int[n];
		for (int i = 0; i<n; i++) {
			switches[i] = sc.nextInt();
		}
		
		int num = sc.nextInt();
		for (int i = 0; i<num; i++) {
			int student = sc.nextInt();
			int stNum = sc.nextInt();
			if (student == 1) {
				for (int j = 0; j<n; j++) {
					if ((j+1) % stNum == 0) {
						switches[j] = changeNum(switches[j]); 
					}
				}
			} else {
				switches[stNum-1] = changeNum(switches[stNum-1]);
				int j = 1;
				while(stNum - j -1 > -1 && stNum + j -1 < n) {
					if (switches[stNum-j-1] != switches[stNum+j-1]) {
						break;
					} 
					switches[stNum-j-1] = changeNum(switches[stNum-j-1]);
					switches[stNum+j-1] = changeNum(switches[stNum+j-1]);
					j++;
				}
			}
		}
		for (int i=0; i<n; i++) {
			if ((i+1) % 20 == 0) System.out.print(switches[i]+"\n");
			//if ((i) % 20 == 0) System.out.println("\n"+switches[i]);  
			else System.out.print(switches[i] + " ");
		}
		sc.close();
	}

}
