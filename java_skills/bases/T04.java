public class T04 {
    public static void main(String[] args) {
        // int num = 1;
        // int sum = 0;
        // while( num <= 100 ) {
        //     sum += num;
        //     num++;
        // }

        // int num = 2;
        // int sum = 0;
        // while( num <= 1000 ) {
        //     sum += num;
        //     num += 2;
        // }

        // int num = 5;
        // int sum = 0;
        // while( num <= 100 ) {
        //     sum += num;
        //     num += 5;
        // }

        // int num = 1;
        // int sum = 1;
        // while( num <= 13 ) {
        //     sum *= num;
        //     num += 2;
        // }
        /*
        int sum = 0;
        outer:for(int i = 1;i <= 100; i++){
            sum += i;
            System.out.println("Sum: " + sum);
            while(sum >= 300){
                break outer;
            }
        }

        int sum = 0;
        outer:for(int i = 1; i <= 100; i++){
            sum += i;
            while(sum == 300){
                continue outer;
            }
            System.out.println("Sum: " + sum);
        }
        */

        int n = 0;
        for(int i = 1; i <= 100; i++){
            if(i%5==0){
                System.out.print(i + "\t");
                n++;
                if(n%6==0){
                    System.out.println();
                }
            }

        }
    }
}