public class TestArray06 {
    public static void main(String[] args) {
/*         System.out.println(args.length);
        for(String str:args){
            System.out.println(str);
        } */
        method1(1,2,3,4,5);
    }

    public static void method1(int num1, int ...nums){
        System.out.println(num1);
        System.out.println("nums: " + nums.length);
        for(int n:nums){
            System.out.print(n+"\t");
        }
        System.out.println();
    }
}