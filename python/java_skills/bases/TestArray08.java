import java.util.Arrays;

public class TestArray08 {
    public static void main(String[] args) {
        int[] srcArr = {1,5,2,4,3};
        int[] desArr = new int[10];

        System.arraycopy(srcArr, 2, desArr, 4, 3);
        System.out.println(Arrays.toString(desArr));
    }
    
}
