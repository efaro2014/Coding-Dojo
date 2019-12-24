public class Wizzard extends Humans{
    public Wizzard(){
        // Set default health to 50
        health = 50;
        // Set default intelligence to 8
        intelligence = 8;
    }
    // Add a method heal(Human) that heals the other human
    //  by the wizard's intelligence
    public Humans heal(Humans other_human){
        other_human.health += this.intelligence;
        return other_human;
    }
    // Add a method fireball(Human) that decreases the other 
    // human's health by the wizard's intelligence * 3
    public Humans fireball(Humans other_human){
        other_human.health -= this.intelligence *3;
        return other_human;
    }
    public static void main(String[] args) {
        Wizzard wizzard = new Wizzard();
        Humans human3 = new Humans();
        // wizzard.attack(human3);
        // wizzard.attack(human3);
        // wizzard.attack(human3);
        // wizzard.heal(human3);
        wizzard.fireball(human3);
        System.out.println(human3.displayHealth());
        System.out.println(wizzard.intelligence);
    }
}
