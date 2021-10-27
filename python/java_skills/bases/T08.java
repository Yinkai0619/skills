import java.util.Scanner;

public class T08 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Plz enter your name: ");
        String name = sc.next();

        System.out.print("Plz enter your gender: ");
        char gender = sc.next().charAt(0);

        System.out.print("Plz enter your age: ");
        int age = sc.nextInt();

        System.out.print("Plz enter your height: ");
        float height = sc.nextFloat();

        System.out.println("Info" + "test");
        System.out.println("\nName: " + name);
        System.out.println("\nAge: " + age);
        System.out.println("\nGender: " + gender);
        System.out.println("\nHeight: " + height);
    }
}
