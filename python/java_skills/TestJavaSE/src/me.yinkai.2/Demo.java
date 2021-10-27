public class Demo {
    int id;
    static int sid;

    public void nm(){
        System.out.println("normal method");
        {
            System.out.println("normal block");
        }
    }

    public static void sm(){
        System.out.println("static method");
    }

    {
        System.out.println("building block");
    }

    static{
        System.out.println("static block");
        Demo.sid = 50;
    }

    public Demo(){
        System.out.println("empty constructor");
    }

    public Demo(int id){
        this.id = id;
    }

    public static void main(String[] args) {
        Demo d1 = new Demo();
        Demo.sm();
        d1.nm();
        System.out.println("-------------------------------------");

        Demo d2 = new Demo();
        Demo.sm();
        d2.nm();
    }
}
