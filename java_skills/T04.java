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

        int num = 1;
        int sum = 1;
        while( num <= 13 ) {
            sum *= num;
            num += 2;
        }
        System.out.println("Sum: " + sum);
    }
}