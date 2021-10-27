public abstract class Person {
    protected String name;
    protected int age;
    protected double weight;

    public abstract void eat(String food);

    public abstract void sleep();

    @Override
    public String toString() {
        return "Person [age=" + age + ", name=" + name + ", weight=" + weight + "]";
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }

    public Person(String name, int age, double weight) {
        this.name = name;
        this.age = age;
        this.weight = weight;
    }

}

class Male extends Person {

    public Male(String name, int age, double weight) {
        super(name, age, weight);
        super.name = name;
        super.age = age;
        super.weight = weight;
        
    }

    public void eat(String food) {
        System.out.println("I like to eat " + food + ". ");
    }

    public void sleep() {
        System.out.println("I don't like sleeping.");
    }

    @Override
    public String toString() {
        return "Male [age=" + age + ", name=" + name + ", weight=" + weight + "]";
    }
}
