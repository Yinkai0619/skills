public class Person {
    private String name;
    private String gender;
    private int age;
    
    public void setName(String name) {
        this.name = name;
    }

    public String getName(){
        return this.name;
    }

    public void setAge(int age){
        if (age >= 1 || age <= 120) {
            this.age = age;
        }else{
            System.out.println("Error: Invalid Value.");
        }
    }

    public int getAge(){
        return this.age;
    }

    public void setGender(String gender){
        if(gender == "Male" || gender == "Female"){
            this.gender = gender;
        }else{
            System.out.println("Error: Invalid Value.");
        }
    }

    public String getGender(){
        return this.gender;
    }

    public Person(){

    }

    public Person (String name, String gender, int age){
        this.name = name;
        this.setAge(age);
        this.setGender(gender);
    }
    
}
