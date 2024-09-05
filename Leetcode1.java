import java.util.Arrays;

public class Leetcode1 {

    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    result = new int[] { i, j };
                }
            }
        }
        return result;

    }

    public static void main(String[] args) {
        int[] nums = { 3, 2, 3 };
        int target = 6;
        Leetcode1 solution = new Leetcode1();
        int[] result = solution.twoSum(nums, target);
        System.out.println(Arrays.toString(result));
    }

}