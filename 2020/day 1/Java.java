
import java.io.File; 
import java.util.Scanner; 
public class Java { 
    public static void main(String[] args) {
        try {

            File file = new File("day 1\\inputs.txt"); 
	        Scanner sc = new Scanner(file);
            Scanner sc_ = new Scanner(file);
            int i;
            int j;
            while (sc.hasNextLine()) {
                i = sc.nextInt();
                while (sc_.hasNextLine()) {
                    j = sc_.nextInt();
                    if (i + j == 2020) {
                        System.out.println(i+j);
                        System.out.println(i*j);
                    }
                }
            }
            sc.close();
            sc_.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    } 
} 
