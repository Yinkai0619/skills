public class Person {
    int age;
    String name;
    double height;
    double weight;

    public void eat(){
        System.out.println("I lick eating.");
    }

    public void sleep(String address){
        System.out.println("I like sleeping at " + address + ". ");
    }

    public String introduce(){
        return "My name is " + name + ", my age is " + age + ", My height is " + height + ", my weight is " + weight + ". ";
    }
}