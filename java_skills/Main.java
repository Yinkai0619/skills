public class Main {
    public static void main(String[] args) {
        int n = 100;
        System.out.println("n = " + n);

        n = 200;
        System.out.println("n = " + n);

        int x = n;
        System.out.println("x = " + x);

        x = x + 100;
        System.out.println("x = " + x);
        System.out.println("n = " + n);

    }
}
