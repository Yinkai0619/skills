public class TestArray04 {
    public static void main(String[] args) {
        int[] nums = {3,5,9,7,11,29,17};
        // int[] nums = {3,5,9};
/* 
        int index = getIndex(nums, 111);
        if(index == -1){
            System.out.println("Null");
        }else{
            System.out.println("Index: " + index);
        }
 */
        System.out.print("Before: ");
        printArray(nums);

        insertArr(nums, 1, 0);

        System.out.print("After: ");
        printArray(nums);
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
