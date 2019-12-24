public class Humans{
    int strength = 3;
    int stealth = 3;
    int intelligence = 3;
    int health = 100;
    public Humans attack(Humans attacked){
        attacked.health -= this.strength;
        return attacked;
    }
    public int displayHealth(){
        return this.health;
    }
    public static void main(String[] args) {
        Humans human1 = new Humans();
        Humans human2 = new Humans();
        human1.attack(human2);
        System.out.println(human2.displayHealth());
        human1.attack(human2);
        System.out.println(human1.displayHealth());
        System.out.println(human2.displayHealth());
    }
}