import java.util.HashMap;
import java.util.Set;
public class Songs {
    public static void main(String[] args) {
        HashMap<String, String> songs = new HashMap<String, String>();
        songs.put("Track1", "Never google your symptoms");
        songs.put("Track2", "Never google your symptoms");
        songs.put("Track3", "Walter Wizard");
        songs.put("Track4", "Mereye Meareye");
        // get the keys by using the keySet method
        Set<String> keys = songs.keySet();
        System.out.println(songs.get("Track1"));
        for(String key : keys) {
            // System.out.println(key);
            System.out.println(songs.get(key));    
        }
    }
}


