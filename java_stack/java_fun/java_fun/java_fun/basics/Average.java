public class Average{
    public static int average(){
        int [] array = {2, 10, 3};
        int sum = 0;
        for(int i =0; i <array.length; i++){
            sum += array[i];
        }
        return sum/array.length;
    }
    public static void main(String[] args){
        System.out.println(average());
    }
}