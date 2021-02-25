public class Boy {
    private String name;
    private int age;

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

    public String Kiss(Girl girl) {
        return this.getName() + " is kissing " + girl.getName() + ". ";
    }

    public Boy() {

    }
    
    public Boy(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
}
