public class Test {
    public static void main(String[] args) {
        Boy yinkai = new Boy("Yinkai", 35);
        Girl nana = new Girl("Nana", 29);

        System.out.println(yinkai.Kiss(nana));
        System.out.println(nana.Introduce(yinkai));

        nana.m = new Mom();
        nana.wechat();
        
        System.out.println();
        System.out.println("========================================");
        System.out.println();

        // Dog d = new Dog();
        // Animal an = d;
        Animal an = PetStore.getAnimal("dog");
        nana.play(an);
        Dog dog = (Dog)an;

        dog.eat();
        // dog.setWeight(100.2);
        // System.out.println(dog.getWeight());

        // Animal dog1 = PetStore.getAnimal("dog");
        // dog1.shout();
        // Dog dog2 = (Dog) dog1;
        // dog2.setWeight(40.5);
        // System.out.println(dog2.getWeight());        



        // System.out.println();

        // Animal an2 = new Cat();
        // an2.shout();
    }

}
