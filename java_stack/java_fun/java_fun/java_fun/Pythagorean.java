import java.lang.Math;
public class Pythagorean{
    public Double calculateHypotenuse(){
        double a = 10;
        double b = 20;
        double A = a*a;
        double B = b * b;
        double c = Math.sqrt(A + B);
        return c;
    }
}