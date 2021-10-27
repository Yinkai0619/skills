public class Girl {
    private String name;
    private int age;
    Mom m;

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

    public Girl() {

    }

    public Girl(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String Introduce(Boy boy) {
        return "My lover is " + boy.getName() + ". His age is " + boy.getAge() + ". ";
    }    

    void wechat() {
        m.say();
    }
   
    public void play(Animal animal) {
        animal.shout();
    }
}
