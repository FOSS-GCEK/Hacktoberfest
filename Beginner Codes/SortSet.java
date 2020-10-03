import java.util.Arrays;
class SortSet
{
  public static void main(String args[])
  {
     int n=args.length;
     int[] ar = new int[n];
     for(int i=0;i<n;i++)
     {
       ar[i]=Integer.parseInt(args[i]);
     }
     Arrays.sort(ar);
     for(int i=0;i<n;i++)
     {
        System.out.print(ar[i]+" ");
     }
  }
}


/*
//Decending Order
import java.util.Arrays; 
import java.util.Collections; 
  
public class SortExample 
{ 
    public static void main(String[] args) 
    { 
        // Note that we have Integer here instead of 
        // int[] as Collections.reverseOrder doesn't 
        // work for primitive types. 
        Integer[] arr = {13, 7, 6, 45, 21, 9, 2, 100}; 
  
        // Sorts arr[] in descending order 
        Arrays.sort(arr, Collections.reverseOrder()); 
  
        System.out.println("Modified arr[] : %s", 
                          Arrays.toString(arr)); 
    } 
}
*/
