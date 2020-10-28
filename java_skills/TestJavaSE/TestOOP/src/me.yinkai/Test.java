public class Test {
    public static void main(String[] args) {
        Person yinkai = new Person();
        yinkai.age = 35;
        yinkai.name = "Yinkai";
        yinkai.height = 172.5;
        yinkai.weight = 85.2;

        Person nana = new Person();
        nana.name = "Baina";
        nana.age = 30;
        nana.height = 151;
        nana.weight = 49;

        System.out.println(yinkai.name);
        System.out.println(nana.name);

        yinkai.eat();
        yinkai.sleep("home");
        yinkai.sleep("copration");
        System.out.println(yinkai.introduce());
        System.out.println(nana.introduce());
    }    
}
