import java.util.Arrays;
public class TestArray07 {
    public static void main(String[] args) {
        int[] nums = {1,3,6,8,2,5,7,4};
        System.out.println(Arrays.toString(nums));
        // Arrays.sort(nums);
        // System.out.println(Arrays.toString(nums));
        // System.out.println(Arrays.binarySearch(nums,4));
        // int[] nums1 = Arrays.copyOf(nums, 5);
        // System.out.println(Arrays.toString(nums1));

        // int[] nums2 = Arrays.copyOfRange(nums, 2, 6);
        // System.out.println(Arrays.toString(nums2));

        // int[] nums1 = {1,3,6,8,2,5,7,4};
        // System.out.println(Arrays.equals(nums, nums1));
        // System.out.println(nums == nums1);

        Arrays.fill(nums, 5);
        System.out.println(Arrays.toString(nums));
    }
    
}
