public class Girl {
    String name;
    private int age;
    
    public void setAge(int age){
        if(age >= 20 && age <= 30){
            this.age = age;
        }else{
            this.age = 28;
        }
    }

    public int getAge(){
        return age;
    }
}
