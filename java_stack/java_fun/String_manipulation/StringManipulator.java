public class StringManipulator {
    public String trimAndConcat(String str, String any){
        String combined = String.format("%s%s", str.trim(),any.trim());
        return combined;
    }
    public Integer getIndexOrNull(String str, String letter){
        int num = str.indexOf(letter);
        if(num >=0){
            return num;
        }
        else{
            return null;
        }
        
    }
    public String concatSubstring(String str, int startindex, int endindex, 
    String word){
        String name = str.substring(startindex, endindex);
        String newname = name.concat(word);
        return newname;
        }
}

