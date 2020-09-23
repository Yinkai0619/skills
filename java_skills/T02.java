import java.util.Scanner;
public class T02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Plz enter your age: ");
        int age = sc.nextInt();
        boolean flag = false;
        if (age >= 7) {
            flag = true;
        }else if (age >= 5) {
            System.out.print("Plz enter your gender(M/F): ");
            char gender = sc.next().charAt(0);
            if (gender == 'M' || gender == 'm') {
                flag = true;
            }
        }

        System.out.println("Carriable: " + flag);
    }
}