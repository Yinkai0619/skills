public class TestMethod01 {
    public static int add1(int num1, int num2){
        return num1 + num2;
    }
    
    public static void add2(int num1, int num2){
        System.out.println(num1 + num2);
    }

    public static void main(String[] args) {
        System.out.println(add1(3,5));
        add2(5,4);
    }
}
