import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
	
	public static void main(String[] args) throws IOException {
		//System.setIn(new FileInputStream("input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer tokens = new StringTokenizer(br.readLine()," ");
		int s = Integer.parseInt(tokens.nextToken()); //전체길이
		int p = Integer.parseInt(tokens.nextToken()); //부분길이
		ArrayList<String> dnaList = new ArrayList<>();
		
		//tokens = new StringTokenizer(br.readLine(),"");
		String[] splitStr = br.readLine().split("");
		for (int i =0; i<s; i++) {
			dnaList.add(splitStr[i]);
		} //"c", "c", ... 
		
		tokens = new StringTokenizer(br.readLine()," ");
		int rules[] = new int[4];
		for (int i=0; i<4; i++) {
			rules[i] = Integer.parseInt(tokens.nextToken());
		}
		
		ArrayList<String> tmp = new ArrayList<>();
		for (int i = 0; i<p; i++) {
			tmp.add(dnaList.get(i));
		}
		int answer = 0;
		int []count = new int[4];
		boolean flag = true;
		
		//첫번째 tmp 체크
		count[0] = Collections.frequency(tmp, "A");
		count[1] = Collections.frequency(tmp, "C");
		count[2] = Collections.frequency(tmp, "G");
		count[3] = Collections.frequency(tmp, "T");
		for (int i =0; i<4; i++) {
			if (count[i] < rules[i]) {
				flag = false;
				break;
			}
		}
		if (flag) answer++;

		int left = 0, right = p;
		String plus, minus;
		
		while (right < s) {
			plus = dnaList.get(right);
			if (plus.equals("A")) count[0] += 1;
			else if (plus.equals("C")) count[1] += 1;
			else if (plus.equals("G")) count[2] += 1;
			else if (plus.equals("T")) count[3] += 1;
			
			minus = dnaList.get(left);
			if (minus.equals("A")) count[0] -= 1;
			else if (minus.equals("C")) count[1] -= 1;
			else if (minus.equals("G")) count[2] -= 1;
			else if (minus.equals("T")) count[3] -= 1;
//			tmp.add(dnaList.get(right));
//			tmp.remove(0);
			flag = true;
			for (int i =0; i<4; i++) { 
				if (count[i] < rules[i]) {
					flag = false;
					break;
				}
			}
			if (flag) answer++;
			left++;
			right++;
		}
		System.out.println(answer);
	}
}

