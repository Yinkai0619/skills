public class Test {
    public static void main(String[] args) {
        Student s1 = new Student();
        s1.setName("Nana");
        s1.setAge(29);
        s1.setHeight(151.5);

        Student s2 = new Student("Yinkai", 57, 35, 172.1);

        System.out.println("Name: " + s1.getName());
        System.out.println("StudentNumber: " + s1.getSno());
        System.out.println("Age: " + s1.getAge());
        System.out.println("Height: " + s1.getHeight());
        s1.study();
        s1.eat();
        s1.sleep();

        System.out.println("===============================");
        System.out.println("Name: " + s2.getName() +  
        "\nStudentNumber: " + s2.getSno() + "\nAge: " + s2.getAge());
        s2.getAge();
        
        System.out.println("\nThe relationship between " + 
        s1.getName() + " and " + s2.getName() + 
        // ": " + s1.getRelationship());
        ": " + s2.getRelationship());

        System.out.println("\n" + s1.toString());
    }
    
}
