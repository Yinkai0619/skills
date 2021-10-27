public class Dog extends Animal {
    private double weight;

    public void setWeight(double weight){
        this.weight = weight;
    }

    public double getWeight(){
        return this.weight;
    }

    public void shout() {
        System.out.println("A bark from a dog.");
    }

    public void eat() {
        System.out.println("The dog is eating.");
    }
    
}
