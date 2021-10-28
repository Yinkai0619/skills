public class PetStore {
    public static Animal getAnimal(String petName) {
        Animal an = null;

        if("cat".equals(petName)) {
            an = new Cat();
        }
        if("dog".equals(petName)) {
            an = new Dog();
        }
        
        return an;

    }
    
}
