public class TestArray03 {
    public static void main(String[] args) {
        int[] nums = {3,5,9,7,11,29,17};
        int index = getIndex(nums, 11);
        if(index == -1){
            System.out.println("Null");
        }else{
            System.out.println("Index: " + index);
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
