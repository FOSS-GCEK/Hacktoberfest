#include <stdio.h>
#include <math.h>
int main()
{
  int num,t,rem,n=0,result=0;
  printf("Enter an integer:");
  scanf("%d",&num);
  t=num;
  while(t!=0)
  {
   t=t/10;
   ++n;
  }
  t=num;
  while(t!=0)
  {
    rem=t%10;
    result=result+pow(rem,n);
    t=t/10;
  }
  if (result==num)
    printf("%d is an Armstrong number",num);
  else
    printf("%d is not an Armstrong number",num);
  return 0;
}
