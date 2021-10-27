public class Test {
    public static void main(String[] args) {
        Phone p1 = new Phone("Huawei", 2020, 3900);
        Phone p2 = new Phone("Huawei", 2020, 3900);

        System.out.println(p1.toString());
        System.out.println(p2.toString());
        System.out.println();
        System.out.println(p1==p2);
        System.out.println(p1.equals(p2));

        Cat c = new Cat();
        System.out.println("\n" + p1.equals(c));
        

        System.out.println(Double.compare(p1.getPrice(), 4.3));



    }
    
}
