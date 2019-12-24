// Array with Odd Numbers
public class Odd{
    public static int odd(){
        int [] array = { };
        for(int i =0; i < 255; i++){
            if ( i % 2 !=0 ){
                array.add(i);
            }
        }
        return array;
    }
    public static void main(String[] args){
        System.out.println(odd());
    }
}