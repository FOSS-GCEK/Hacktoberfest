#include <stdio.h>

int main()
{
  int n;

  printf("Enter a number\n");
  scanf("%d", &n);

  if (n > 0)
    printf("Greater than zero.\n");
  else
    printf("Less than or equal to zero.\n");

  return 0;
}

