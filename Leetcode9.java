
public class Leetcode9 {

    public static boolean isPalindrome(int x) {
        // bat loi
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        int reversed = 0;

        // dao so x
        while (x > reversed) {
            reversed = reversed * 10 + x % 10;
            x /= 10;
        }

        // so chu so chan || so chu so la le
        return x == reversed || x == reversed / 10;
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome(121)); // true
        System.out.println(isPalindrome(-121)); // false
        System.out.println(isPalindrome(10)); // false
        System.out.println(isPalindrome(12321)); // true
        System.out.println(isPalindrome(1000021)); // false
    }

}