// Array with Odd Numbers
import java.util.ArrayList;
import java.util.Arrays;

public class Odd{
    public static ArrayList<Integer> odd(){
        ArrayList<Integer> array = new ArrayList<Integer>();
        for(int i =0; i < 255; i++){
            if ( i % 2 !=0 ){
                array.add(i);
            }
        }
        return array;
    }
    public static ArrayList<Integer> greaterY(int[] arr, int val){
        ArrayList<Integer> arraygreater= new ArrayList<Integer>();
        for (int i=0; i<arr.length; i++){
            if (arr[i] > val){
                arraygreater.add(arr[i]);
            }
        }
        return arraygreater;
    }
    public static ArrayList<Integer> square(int[] x){
        ArrayList<Integer> arraysquare= new ArrayList<Integer>();
        for (int i =0; i < x.length; i++){
            int temp = x[i] * x[i];
            arraysquare.add(temp);
        }
        return arraysquare;
    }
    public static ArrayList<Integer> noNegatives(int[] arr){
        ArrayList<Integer> positiveArray= new ArrayList<Integer>();
        for (int i =0; i < arr.length; i++){
            if (arr[i] < 0){
                arr[i] = 0;                
            }
            positiveArray.add(arr[i]);
        }
        return positiveArray;
    }
    public static ArrayList<Integer> shift(int[] array){
        ArrayList<Integer> new_array= new ArrayList<Integer>();
        for (int i =1; i<array.length; i++){
            new_array.add(array[i]);
        }
        new_array.add(0);
        return new_array;
    }
    public static void main(String[] args){
        int[] arr = {1,24,52,-3, 8};
        System.out.println(greaterY(arr, 5));
        // System.out.println(odd());
        System.out.println((square(arr)));
        System.out.println(noNegatives(arr));
        System.out.println((shift(arr)));

    }
}


