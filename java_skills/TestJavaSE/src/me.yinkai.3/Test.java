public class Test {
    public static void main(String[] args) {
        // Girl g1 = new Girl();
        Person g1 = new Person();
        g1.setName("Nana");
        g1.setAge(29);
        g1.setGender("Female");
        System.out.println(g1.getName());
        System.out.println(g1.getAge());
        System.out.println(g1.getGender() + "\n-----------------------");

        Person b1 = new Person("Yinkai","Male",35);
        System.out.println(b1.getName() + "\n" + b1.getGender() + "\n" + b1.getAge());
    }
    
}
