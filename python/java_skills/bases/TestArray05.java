import java.util.Arrays;
public class TestArray05 {
    public static void main(String[] args) {
        int[] nums = {3,5,9,7,11,29,17};
        // int[] nums = {3,5,9,7};
        //            0 1 2 3
        System.out.print("Before: \t");
        System.out.println(Arrays.toString(nums));

        // removeIndex(nums,1);
        removeValue(nums,11);
        System.out.print("After: \t\t");
        System.out.println(Arrays.toString(nums));
    }

    public static int[] removeValue(int[] arr, int value){
        int index = -1;
        for(int i=0;i<=arr.length-1;i++){
            if(arr[i] == value){
                index = i;
                break;
            }
        }
        removeIndex(arr, index);
        return arr;
    }

    public static int[] removeIndex(int[] arr, int index){
        if(index >= 0 && index <= arr.length){
            for(int i=index; i<=arr.length-2; i++){
                arr[i] = arr[i+1];
            }
            arr[arr.length-1] = 0;
        }else{
            System.out.println("Error");
        }
        return arr;
    }

    public static int[] insertArr(int[] arr, int index, int ele){
        for(int i=arr.length-1; i!=index; i--){
            arr[i] = arr[i-1];
        }
        arr[index] = ele;
        return arr;
    }

    public static void printArray(int[] arr){
        int arrLength = arr.length;
        for(int i=0;i<arrLength;i++){
            if(i != arrLength-1){
                System.out.print(arr[i] + ", ");
            }else{
                System.out.println(arr[i]);
            }
        }
    }

    public static int getIndex(int[] arr, int ele){
        int index = -1;
        for(int i=0;i<arr.length;i++){
            if(arr[i] == ele){
                index = i;
                break;
            }
        }
        return index;
    } 
}
