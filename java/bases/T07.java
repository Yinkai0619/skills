import java.util.Scanner;

public class T07 {
    public static void main(String[] args) {
        final double PI = 3.1415926;
        java.util.Scanner sc = new Scanner(System.in);
        System.out.print("Plz input a radii: ");
        int r = sc.nextInt();

        // Girth
        double c = 2 * PI * r;
        System.out.println("Girth: " + c);

        // Acreage
        double s = PI * r * r;
        System.out.println("Acreage: " + s);
    }
    
}
