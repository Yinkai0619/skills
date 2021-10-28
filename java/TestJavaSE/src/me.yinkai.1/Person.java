public class Person {
    private String name;
    private int age;
    private double height;
    protected String relationship = "colleague";

    public void setName(String name){
        this.name = name;
    } 

    public String getName(){
        return this.name;
    }

    public void setAge(int age){
        if(age >= 1 && age <= 120){
            this.age = age;
        }else{
            System.out.println("Error: Invalid Value.");
        }
    }

    public int getAge(){
        return this.age;
    }

    public void setHeight(double height){
        if(height >= 100.0 && height <= 250.0){
            this.height = height;
        }else{
            System.out.println("Error: Invalid Value.");
        }
    }

    public double getHeight(){
        return this.height;
    }

    public void eat(){
        System.out.println("Eatting...");
    }

    public void sleep(){
        System.out.println("Sleeping...");
    }

    public void talk(){
        System.out.print("Talking...");
    }

    public Person(){
        super();
    }

    public Person(String name, int age, double height){
        super();
        this.name = name;
        this.age = age;
        this.height = height;
    }

}
