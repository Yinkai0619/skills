public class TestFor02 {
    public static void main(String[] args) {
        for(int i=1;i<=5;i++){

/*             for(int s=1;s<=5;s++){
                System.out.print(' ');
            }
 */

/* 
    ************
   ************
  ************
************
 */
/*             for(int s=i-4;s!=0;s++){
                System.out.print(' ');
            }
            for(int j=1;j<=9;j++){
                System.out.print('*');
            }
            System.out.println();
 */

/* 
     *
    ***
   *****
 *********
***********
 */
            for(int s=1;s<=(5-i);s++){
                System.out.print(' ');
            }

            for(int j=1;j<=i*2-1;j++){
                System.out.print('*');
            }

            System.out.println();
        }
    }    
}

