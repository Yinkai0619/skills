import java.util.Scanner;

public class T05 {
    public static void main(String[] args) {
        int count = 0;
        Scanner sc = new Scanner(System.in);
        boolean flag = true;

        for(int i=1;i<=10;i++){
            System.out.println("Please input the number "+i+": ");
            int num = sc.nextInt();
            
            if(num > 0){
                count++;
            } 

            if(num==666){
                flag = false;
                break;
            }
        }

        if(flag){
            System.out.println("Normal quit.");
        }else{
            System.out.print("Except quit.");
        }

        System.out.println("The number count: " + count);

    }
}
