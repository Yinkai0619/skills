public class Demo {
    String name;
    int age = 10;
    static String arg1 = "arg1";

    public void a() {
        {
            System.out.println("这是普通块");
            
            class LIC2 {

            }
        }

        class LIC1 {

        }
    }
    
    public static void b() {
        System.out.println("bbb");
    }

    {
        System.out.println("这是构造块");
    }

    static{
        System.out.println("这是静态块");
    }

    public Demo() {
        System.out.println("这是空构造器");
        class LIC3 {

        }
    }

    public Demo(String name) {
        this.name = name;
        System.out.println("这是构造器");
    }

    class MIC1 {
        {
            System.out.println("这是成员内部类");
        }
        
        int age = 20;
        public void c() {
            name = "Yinkai";
            a();
            int age = 30;

            System.out.println(age);    //内部类方法内属性
            System.out.println(this.age);   //内部类属性
            System.out.println(Demo.this.age);  //外部类Demo的属性 
        }

    }
    
    static class SMIC1 {
        public void e() {
            System.out.println("这是静态成员内部类");
            System.out.println(arg1);
            b();
        }
    }

    public void d() {
        MIC1 mic1 = new MIC1();
        // mic1.age = 10;
        // System.out.println(mic1.age);
        mic1.c();
    }
}

class Test {
    public static void main(String[] args) {
        // Demo d1 = new Demo();
        // Demo.b();
        // d1.a();
        // System.out.println("-------------------------");
        // d1.d();


        //非静态成员内部类
        Demo d1 = new Demo();
        Demo.MIC1 mic1 = d1.new MIC1();
        System.out.println(mic1.age + "-----");


        //静态成员内部类
        Demo.SMIC1 smic1 = new Demo.SMIC1();
        smic1.e();


    }
}
