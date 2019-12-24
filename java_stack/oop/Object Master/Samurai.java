public class Samurai extends Humans{
    private static int number =0;
    public Samurai(){
        // Set default health to 200
        health = 200;
        number +=1;
    }
    // Add a method deathBlow(Human) that kills the other human, 
    // but reduces the Samurai's health by half
    public Humans deathBlow(Humans other_human){
        other_human.health = 0;
        System.out.println("OMG Samurai killed human3!");
        this.health -= this.health/2;
        return other_human;
    }
    // Add a method meditate() that heals the 
    // Samurai for half of their current health.
    public void meditate(){
        this.health += this.health/2;
    }
    // Add a method howMany() that returns the total
    //  current number of Samurai.
    public static int howMany(){
        return number;
    }
      public static void main(String[] args) {
        Samurai samurai = new Samurai();
        Samurai samurai2 = new Samurai();
        Samurai samurai3 = new Samurai();
        Humans human3 = new Humans();
        samurai.deathBlow(human3);
        samurai.meditate();
        // Samurai.howMany();
        System.out.println(Samurai.howMany());
        System.out.println("Others Health: "+ human3.displayHealth());
        System.out.println("Samurai's Health: "+ samurai.displayHealth());
    }
}