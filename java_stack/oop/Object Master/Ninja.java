public class Ninja extends Humans{
    public Ninja(){
        // Set default stealth to 10
        stealth = 10;
    }
    // Add a method steal(Human) that takes the amount of stealth the ninja has,
    //  removes it from the other human's health, 
    // and adds it to the ninja's
     public Humans steal(Humans other_human){
        other_human.health -= this.stealth;
        this.health += this.stealth;
        return other_human;
    }
    // Add a method runAway() that decreases their health by 10
    public void runAway(){
        this.health -= 10;
    }
    public static void main(String[] args) {
        Ninja ninja = new Ninja();
        Humans human3 = new Humans();
        ninja.steal(human3);
        ninja.runAway();
        ninja.runAway();
        ninja.runAway();
        System.out.println("Others Health: "+ human3.displayHealth());
        System.out.println("Ninjas Health: "+ ninja.displayHealth());
    }
}
