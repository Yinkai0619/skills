import java.util.Scanner;

public class TestArray01 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int scores[] = new int[10];
        int sum = 0;
        for(int i=1;i<=10;i++){
            System.out.print("Please enter score of student " + i + ": ");
            int score = sc.nextInt();
            scores[i-1] = score;
            sum += score;
        }
        
        System.out.println("The sum of score: " + sum);
        System.out.println("The average score: " + sum / scores.length);

        int count = 1;
        for(int element: scores){
            System.out.println("Student " + count + ": " + element);
            count++;
        }
    }
}