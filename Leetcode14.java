public class Leetcode14 {

    public static String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return "";
        }
        // so sanh chuoi 1 vs chuoi 2 ,lay ra dc prefix cua ca hai sau do lan luot so
        // sanh
        // vs cac chuoi con lai prefix se giam dan cho toi khi khong co prefix
        String prefix = strs[0];

        for (int i = 1; i < strs.length; i++) {

            System.out.println(strs[i].indexOf(prefix));
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);

                if (prefix.isEmpty()) {
                    return "";
                }
            }
        }

        return prefix;
    }

    public static void main(String[] args) {
        String[] strs1 = { "flower", "flow", "flight" };
        System.out.println(longestCommonPrefix(strs1)); // Output: "fl"

        String[] strs2 = { "dog", "racecar", "car" };
        System.out.println(longestCommonPrefix(strs2)); // Output: ""
    }
}
