import java.util.*;
public class Prog_1018 {
	public static void main(String[] args) {
		Scanner lee= new Scanner(System.in);
		int t, a,b;
		t=lee.nextInt();
		while (t<= 15){
		 for (int i=1; i<=t;i++){
			  a=lee.nextInt(); 
			 b=lee.nextInt(); 
			 if (a<b)
					 System.out.println("<");
			 else {
				 if (a>b)
					 System.out.println(">");
				 else 
					 System.out.println("=");
			 } 
		
		 }
		break;
		 }
	}
}

