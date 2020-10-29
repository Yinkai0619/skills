public class Person {
    String name;
    int age;
    double height;
    double weight;

    public Person(){
    //    name = "Nana";
    //    age = 30;
    //    height = 152.5;
    }

    public Person(String name, int age, double height, double weight){
        this(name, age, height);
        this.weight = weight;
    }
    
    public Person(String name, int age, double height){
        this(name, age);
        this.height = height;
    }

    public Person(String name, int age){
        this(name);
        this.age = age;
    }

    public Person(String name){
        this.name = name;
    }

    public void eat(){
        System.out.println("I lick eating.");
    }
    
}
