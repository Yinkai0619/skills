public class T03 {
    public static void main(String[] args) {
        int score = 97;
        char level = 'Z';
        switch(score/10){
            case 10:
            case 9: 
                level = 'A';
                break;
            case 8:
                level = 'B';
                break;
            case 7:
                level = 'C';
                break;
            case 6:
                level = 'D';
                break;
            case 5:
            case 4:
            case 3:
            case 2:
            case 1:
            case 0:
                level = 'E';
                break;
            default : 
                System.out.println("Score Error!!");
                break;
        }
        System.out.println("Your level: " + level);
    }
}

