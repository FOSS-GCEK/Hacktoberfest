import java.util.Scanner;
public class JavaExample 
{
    public static void main(String[] args) 
    {
    	int count, temp;
    	
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter number of elements you want in the array: ");
        count = scan.nextInt();
        int num[] = new int[count];
        System.out.println("Enter array elements:");
        for (int i = 0; i < count; i++) 
        {
            num[i] = scan.nextInt();
        }
        scan.close();
        Sort(num, count);
    }
    static void Sort(int arr[], int n){
        int temp;
        for (int i = 0; i < n; i++) 
        {
            for (int j = i + 1; j < n; j++) { 
                if (arr[i] > arr[j]) 
                {
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        System.out.print("Array Elements in Ascending Order: ");
        for (int i = 0; i < n - 1; i++) 
        {
            System.out.print(arr[i] + ", ");
        }
        System.out.print(arr[n - 1]);
    }
}
