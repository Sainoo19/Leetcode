import java.util.HashMap;
import java.util.Map;

public class Leetcode20 {
    public static boolean isValid(String s) {
        StringBuilder newStringBuilder = new StringBuilder(s);
        boolean result = true;
        char current = '{';
        while (newStringBuilder != null) {
            for (int i = 0; i <= newStringBuilder.length() - 1; i++) {
                if (newStringBuilder.charAt(i) == '(' || newStringBuilder.charAt(i) == '{'
                        || newStringBuilder.charAt(i) == '[') {
                    current = newStringBuilder.charAt(i);
                } else {
                    if (current == '{' && newStringBuilder.charAt(i) == '}') {
                        newStringBuilder.delete(i - 1, i);
                        i = 0;
                    } else {
                        return result = false;
                    }
                    if (current == '(' && newStringBuilder.charAt(i) == ')') {
                        newStringBuilder.delete(i - 1, i);
                        i = 0;
                    } else {
                        return result = false;
                    }
                    if (current == '[' && newStringBuilder.charAt(i) == ']') {
                        newStringBuilder.delete(i - 1, i);
                        i = 0;
                    } else {
                        return result = false;
                    }
                }
            }
        }

        return result;
    }

    public static void main(String[] args) {
        String s1 = "([]){}"; // Example valid string
        String s2 = "()"; // Example invalid string

        System.out.println("String \"" + s1 + "\" is valid: " + isValid(s1));
        System.out.println("String \"" + s2 + "\" is valid: " + isValid(s2));
    }
}
