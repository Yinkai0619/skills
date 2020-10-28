import java.util.Scanner;
public class TestMethod02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Please enter a number: ");
        // int yourGuessNum = sc.nextInt();
        // int myHeartNum = 5;
        // System.out.println(yourGuessNum == myHeartNum?"Success":"Failed");    
        guessNum(sc.nextInt());
    }

    public static void guessNum(int yourNum){
        int myHeartNum = (int)(Math.random()*6+1);
        System.out.println(yourNum == myHeartNum?"Success":"Failed");    
        System.out.println();
    }
}
