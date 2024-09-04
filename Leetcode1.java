import java.util.Arrays;

public class Leetcode1 {

    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] + nums[i + 1] == target) {
                result = new int[] { i, i + 1 };
            }
        }
        return result;

    }

    public static void main(String[] args) {
        int[] nums = { 2, 7, 11, 15 };
        int target = 9;
        Leetcode1 solution = new Leetcode1();
        int[] result = solution.twoSum(nums, target);
        System.out.println(Arrays.toString(result));
    }

}