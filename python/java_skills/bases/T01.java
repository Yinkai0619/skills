import java.util.Scanner;
public class T01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Please enter your scores: ");

        if (sc.hasNextInt()) {
            int score = sc.nextInt();
            if (score > 0) {
                String discount = "";
                if (score>=8000) {
                    discount = "0.6";
                }else if (score>=4000) {
                    discount = "0.7";
                }else if (score>=2000) {
                    discount = "0.8";
                }else {
                    discount = "0.9";
                }
                System.out.println("Your Discount: " + discount);
            }else {
                System.out.println("Input Error!!");
            }
        }else {
            System.out.println("Input Error!!");
        }
    }
}