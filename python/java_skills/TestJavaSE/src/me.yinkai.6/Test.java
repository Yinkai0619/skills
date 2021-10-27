public class Test {
    public static void main(String[] args) {
        // Person yinkai = new Person();
        // Male yinkai = new Male();
        // yinkai.name = "Yinkai";
        // yinkai.age = 35;
        // yinkai.weight = 85.5;

        Male yinkai = new Male("Yinkai", 35, 85.5);

        System.out.println(yinkai.toString());

        yinkai.eat("bread");
        yinkai.sleep();
    }
    
}
