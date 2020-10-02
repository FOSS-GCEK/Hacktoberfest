#include <stdio.h>
#include <stdlib.h>

int main()    
{   int n,i;   
    int *arr;  
    printf("\nInput the size of array: ");  
    scanf("%d",&n); 
    arr = malloc(n*sizeof(int));
    printf("\nEnter array elements:\n");
    for(i=0;i<n;i++)
    {
      scanf("%d",(arr+i));
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
