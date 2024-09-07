import java.util.HashMap;
import java.util.Map;

public class Leetcode13 {

    public int romanToInt(String s) {
        int result = 0;
        for (int i = 0; i <= s.length() - 1; i++) {
            switch (s.charAt(i)) {
                case 'I':
                    if (i + 1 < s.length() && s.charAt(i + 1) == 'V') {
                        result += 4;
                        i++;
                    } else if (i + 1 < s.length() && s.charAt(i + 1) == 'X') {
                        result += 9;
                        i++;
                    } else {
                        result += 1;
                    }

                    break;
                case 'V':
                    result += 5;
                    break;
                case 'X':
                    if (i + 1 < s.length() && s.charAt(i + 1) == 'L') {
                        result += 40;
                        i++;
                    } else if (i + 1 < s.length() && s.charAt(i + 1) == 'C') {
                        result += 90;
                        i++;
                    } else {
                        result += 10;
                    }
                    break;
                case 'L':
                    result += 50;
                    break;
                case 'C':
                    if (i + 1 < s.length() && s.charAt(i + 1) == 'D') {
                        result += 400;
                        i++;
                    } else if (i + 1 < s.length() && s.charAt(i + 1) == 'M') {
                        result += 900;
                        i++;
                    } else {
                        result += 100;
                    }
                    break;
                case 'D':
                    result += 500;
                    break;
                case 'M':
                    result += 1000;
                    break;
                default:
                    System.out.println("Roman char invalid");
            }
        }
        return result;
    }

    public static int romanToIntGptResult(String s) {
        // Tạo map để lưu giá trị của từng ký tự Roman
        Map<Character, Integer> romanMap = new HashMap<>();
        romanMap.put('I', 1);
        romanMap.put('V', 5);
        romanMap.put('X', 10);
        romanMap.put('L', 50);
        romanMap.put('C', 100);
        romanMap.put('D', 500);
        romanMap.put('M', 1000);

        int total = 0;
        int prevValue = 0;

        // Duyệt qua từng ký tự của chuỗi Roman từ phải sang trái
        for (int i = s.length() - 1; i >= 0; i--) {
            char currentChar = s.charAt(i);
            int currentValue = romanMap.get(currentChar);

            // Nếu giá trị hiện tại nhỏ hơn giá trị trước đó, trừ nó khỏi tổng
            if (currentValue < prevValue) {
                total -= currentValue;
            } else {
                total += currentValue;
            }

            prevValue = currentValue;
        }

        return total;
    }

    public static void main(String[] args) {
        // romanToInt la cach toi giai quyet
        // romanToIntGptResult la cach ChatGPT giai quyet
        Leetcode13 lc13 = new Leetcode13();
        int myresult = lc13.romanToInt("MCMXCIV");
        int result = lc13.romanToIntGptResult("MCMXCIV");
        System.out.println(myresult);
        System.out.println(result);
    }
}
