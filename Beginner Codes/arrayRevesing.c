#include <stdio.h>    

int main()    
{   int n,i;   
    int arr[n];  
    printf("\nInput the size of array: ");  
    scanf("%d",&n); 
    printf("\nEnter array elements:\n");
    for(i=0;i<n;i++)
    {
      scanf("%d",&arr[i]);
    }
    printf(" \nEntered elements are:\n ");    
    for (i = 0; i < n; i++) 
    {     
        printf("%d ", arr[i]);     
    }
    printf("\n");
     
    printf("\nArray in reverse order:\n");        
    for (i = n-1; i >= 0; i--) 
    {     
        printf("%d ", arr[i]);     
    }
    return 0;
 
 }
