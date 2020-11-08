public class TestArray02 {
    public static void main(String[] args) {
        int[] nums = {3,5,9,7,11,29,17};
        System.out.println("Max: " + getMaxNum(nums));
        System.out.println("Min: " + getMinNum(nums));
    }

    public static int getMaxNum(int[] arr){
        int max = arr[0];
        for(int element: arr){
            if(element > max){
                max = element;
            }
        }
        return max;
    }

    public static int getMinNum(int[] arr){
        int min = arr[0];
        for(int element: arr){
            if(element < min){
                min = element;
            }
        }
        return min;
    }
    
}
