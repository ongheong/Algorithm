import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws IOException {
		//System.setIn(new FileInputStream("input.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		for (int i=0; i<n; i++) {
			boolean flag = true;
			String[] psList = br.readLine().split("");
			Stack<String> stack = new Stack<>();
			for (String p:psList) {
				if (p.equals("(")) stack.push(p);
				else if (p.equals(")")) {
					if (stack.isEmpty()) {
						flag = false;
						break;
					}
					else stack.pop();
				}
			}
			if (!stack.isEmpty()) flag = false;
			if (flag) System.out.println("YES");
			else System.out.println("NO");
		}
		
	}

}
