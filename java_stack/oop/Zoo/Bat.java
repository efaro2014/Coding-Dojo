public class Bat extends Mammals{
    public Bat(){
        this.energylevel = 300;
    }
    int count = 0;
    public void fly(){
        count += 1;
        System.out.println("The bat taking off " + count + " times");
        this.energylevel -=50;
    }
    int n = 0;
    public void eatHumans(){
        n += 1;
        energylevel += 25;
        System.out.println(" The bat eaten humans " + n + "times");
    }
    int x = 0;
    public void attackTown(){
        x += 1;
        System.out.println(" The bat attacked the town " + x + "times");
        this.energylevel -= 100;
    }
    public void checkAliveOrDead(){
        if (this.energylevel < 0){
        System.out.println("The Bat is consumed and finally dead");
        }
        else{
            System.out.println("Oh no it is still alive");
        }
    }
    
    public static void main(String[] args){
        Bat bat = new Bat();
        bat.displayEnergy();
        bat.fly();
        bat.fly();
        bat.displayEnergy();
        bat.eatHumans();
        bat.eatHumans();
        bat.displayEnergy();
        bat.attackTown();
        bat.attackTown();
        // bat.attackTown();
        bat.displayEnergy();
        bat.checkAliveOrDead();
    }
    
}
       