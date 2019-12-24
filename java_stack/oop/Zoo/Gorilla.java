 public class Gorilla extends Mammals{
        public void throwSomething(){
            energylevel -= 5;
            System.out.println("Throw some thing");
        }
        public void eatBananas(){
            System.out.println("The gorilla is happy to have banana!");
            this.energylevel += 5;
        }
        int count = 0;
        public void climb(){
            count += 1;
            System.out.println("The climed the tree " + count + " times");
            this.energylevel -=10;
        }
        
        public static void main(String[] args) {
        Gorilla gorilla = new Gorilla();
        gorilla.throwSomething();
        gorilla.eatBananas();
        gorilla.climb();
        gorilla.climb();
        gorilla.climb();
        gorilla.climb();
        gorilla.displayEnergy();
        
    }
 }