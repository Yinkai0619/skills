public class TestFor03 {
   public static void main(String[] args) {
/* 
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

i       j       s
-4      1       4      
-3      3       3
-2      5       2
-1      7       1
0       9       0
1       7       1
2       5       2
3       3       3
4       1       4
 */

/*        for(int i=-4;i<=4;i++){

            for(int s=1;s<=Math.abs(i);s++){
                System.out.print(' ');
            }

           for(int j=1;j<=(9-Math.abs(i)*2);j++){
                System.out.print('*');
           }
            // System.out.println(i + " -> " + Math.abs(i));
            System.out.println();
       }
 */

/* 
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
 */
        for(int i=-4;i<=4;i++){     //行数

            for(int s=1;s<=Math.abs(i);s++){    //打印前置空格
                System.out.print(' ');
            }
            int n = 9 - Math.abs(i) * 2;    //打印行
            for(int j=1;j<=n;j++){
                if(j==1 || j==n){   //当为行首或行尾时打印*，否则打印空格
                    System.out.print('*');
                }else{
                    System.out.print(' ');
                }
            }
            // System.out.println(i + " -> " + Math.abs(i));
            System.out.println();
        }
   } 
}