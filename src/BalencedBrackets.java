import java.io.*;
import java.util.*;
import java.util.stream.*;

class Result {
    public static String isBalanced(String s) {
    Stack<Character> stack = new Stack<Character>();
    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (c == '(' || c == '[' || c == '{') {
            stack.push(c);
        }
        if (c == ')' || c == ']' || c == '}') {
            if (stack.isEmpty()) {
                return "NO";
            }
            char last = stack.peek();
            if (c == ')' && last == '(' || c == ']' && last == '[' || c == '}' && last == '{') {
                stack.pop();
            } else {
                return "NO";
            }
        }
    }
    return stack.isEmpty() ? "YES" : "NO";
    }
}
        char c = s.charAt(i);
        if (c == '(' || c == '{' || c == '[') {
            stack.push(c);
        } else if (c == ')' || c == '}' || c == ']') {
            if (stack.isEmpty()) {
                return "NO";
            }
            char top = stack.pop();
            if (c == ')' && top != '(') {
                return "NO";
            } else if (c == '}' && top != '{') {
                return "NO";
            } else if (c == ']' && top != '[') {
                return "NO";
            }
        }
    }
    return stack.isEmpty() ? "YES" : "NO";
    }
}

public class BalencedBrackets {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, t).forEach(tItr -> {
            try {
                String s = bufferedReader.readLine();

                String result = Result.isBalanced(s);

                bufferedWriter.write(result);
                bufferedWriter.newLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}
