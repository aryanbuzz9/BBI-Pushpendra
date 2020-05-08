import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // Your code here!
        String s="abcdefgfedcba";
        System.out.println(s);
        s=s.replace('g','_');
        System.out.println(s);
        for(int i=5;i>0;i--)
        {
            s=s.replace(s.charAt(i),'_');
            System.out.println(s);
            
        }
    }
}
