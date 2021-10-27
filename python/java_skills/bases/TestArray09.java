public class TestArray09 {
    public static void main(String[] args) {
        // int[][] arrs = new int[3][];
        // int[] arr1 = new int[]{1,2,3};
        // arrs[0] = arr1;
        // arrs[1] = new int[]{4,5,6,7};
        // arrs[2] = new int[]{8,9};
        int[][] arrs = new int[3][2];
/*         for(int i=0;i<arrs.length;i++){
            for(int j=0;j<arrs[i].length;j++){
                System.out.print(arrs[i][j] + ", ");
            }
            System.out.println();
        } */
        arrs[1] = new int[]{4,5,6};
        for(int[] arr:arrs){
            for(int ele:arr){
                System.out.print(ele + ", ");
            }
            System.out.println();
        }
    }
    
}
