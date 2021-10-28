public class TestFor04 {
    public static void main(String[] args) {

/*
  *  
 *** 
*****
 *** 
  *  
*/

/*
        int size = 5;
        int startNum = size / 2 + 1;
        int endNum = size / 2 + 1;
        boolean flag = true;
        for(int i=1;i<=size;i++){
            for(int j=1;j<=size;j++){
                if( j >= startNum && j <= endNum ){
                    System.out.print('*');
                }else{
                    System.out.print(' ');
                }
            }
            if(startNum==1){
                flag = false;
            }
            if(flag){
                startNum--;
                endNum++;
            }else{
                startNum++;
                endNum--;
            }
            System.out.println();
        }
 */
/* 
  *  
 * * 
*   *
 * * 
  * 
 */
        int size = 5;
        int startNum = size / 2 + 1;
        int endNum = size / 2 + 1;
        boolean flag = true;
        for(int i=1;i<=size;i++){
            for(int j=1;j<=size;j++){
                if( j == startNum || j == endNum ){
                    System.out.print('*');
                }else{
                    System.out.print(' ');
                }
            }
            if(startNum==1){
                flag = false;
            }
            if(flag){
                startNum--;
                endNum++;
            }else{
                startNum++;
                endNum--;
            }
            System.out.println();
        }

    }
    
}
