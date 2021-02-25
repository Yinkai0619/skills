public interface TI01 {
    public static final String ORGANIZATION = "DFZK";

    public abstract void m1();
    public abstract void m2(String str);
}

interface TI02 {
    public static final String name = "Yinkai";

    public abstract void m3();
    public abstract void m4(int num);
}

class Person {
    private String name;
    private int age;
    private String gender;

	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public String getGender() {
		return gender;
	}
	public void setGender(String gender) {
		this.gender = gender;
    }
	public Person(String name, int age,String gender) {
		this.name = name;
		this.age = age;
		this.gender = gender;
	}
}

class Employee extends Person implements TI01, TI02{
    private String department;

    public void setDepartment(String department) {
        this.department = department;
    }

    public String getDepartment() {
        return this.department;
    }

    public Employee(String name, int age, String gender, String department) {
        super(name, age, gender);
        this.department = department;
    }

    public void m1() {
        System.out.println("From m1.");
    }

    public void m2(String str) {
        System.out.println("From m2: " + str);
    }

    public void m3() {
        System.out.println("From m3.");
    }

    public void m4(int num) {
        System.out.println("From m4: " + num);
    }

    @Override
    public String toString() {
        return "Employee [department=" + department + 
        ", name=" + this.getName() + 
        ", age=" + super.getAge() + 
        ", department=" + getDepartment() + "]";
    }

}

class Test {
    public static void main(String[] args) {
        TI01 i1 = new Employee("Yinkai", 35, "Male", "IT");
        TI02 i2 = new Employee("Baina", 29, "Female", "IT");


        System.out.println(TI01.ORGANIZATION);
        System.out.println(Employee.name);
        System.out.println(i1.toString());
        System.out.println(i2.toString());
        System.out.println(i1.ORGANIZATION);
    }
}