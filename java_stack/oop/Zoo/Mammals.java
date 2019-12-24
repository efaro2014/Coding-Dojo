public class Mammals{
    public int energylevel = 100;
    public int displayEnergy(){
        System.out.println(energylevel);
        return energylevel;
    }
    public static void main(String[] args) {
        Mammals mammal1 = new Mammals();
        // System.out.println(mammal1.displayEnergy());
        mammal1.displayEnergy();
    }
}
