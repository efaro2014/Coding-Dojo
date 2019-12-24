public class Basics{
    // public static void main(String[] args) {
        // fizzbuzz logic here
        // for (int i = 0; i < 255; i++){
        // System.out.println("bar");
        // }
        // int sum = 0;
        // for(int i =0; i <255; i++){
        //     sum += i;
        // }
        // System.out.println(sum);

        // int [] array = {1,3,5,7,9,13};
        // for(int i=0; i < array.length; i++){
        //     System.out.println(array[i]);
        // }
    public static int largest(){
        int [] array = {1,3,5,7,9,13};
        int max = 0;
        for(int i=0; i<array.length; i++){
            if (array[i] > max){
                max = array[i];
            }
        }
        return max;
    }
}




