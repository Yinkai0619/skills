package Test1;

public interface TI02 {
    public static final int NUM = 10;

    public abstract void a();

    public default void b() {
        System.out.println("From TI02.b----------");
    }
    
    public static void c() {
        System.out.println("From TI02.c");
    }
}

class TC01 implements TI02 {
    public void a() {
        System.out.println("From TI02.a");
        b();
        TI02.super.b();
    }

    public static void c() {
        System.out.println("From TC01.c");
    }

}

class Demo {
    public static void main(String[] args) {
        TC01 c1 = new TC01();
        
        c1.a();
        System.out.println(TI02.NUM);
        System.out.println(c1.NUM);
        c1.c();
    }
}