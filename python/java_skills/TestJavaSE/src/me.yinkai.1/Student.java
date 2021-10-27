public class Student extends Person {
    private int sno;
    protected String relationship = "lovers";


    public void setSno(int sno){
        this.sno = sno;
    }

    public int getSno(){
        return this.sno;
    }

    public void study(){
        System.out.println("Studying...");
    }
    
    public Student(){
        super();
    }

    public Student(String name, int sno, int age, double height){
        super(name,age,height);
        this.sno = sno;
        // this.setName(name);
        // this.setAge(age);
        // this.setHeight(height);
    }

    public int getAge(){
        return 0;
    }

    String getRelationship(){
        return this.relationship;
        // return super.relationship;
    }

    public String toString(){
        return this.getName() + '{' + this.getAge() + ", " + 
        this.getHeight() + ", " + 
        this.getSno() + '}';
    }
}