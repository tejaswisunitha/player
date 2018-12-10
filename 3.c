#include<stdio.h>
void main()
{
    int i,n,r,rev;
    scanf("%d",&n);
    while(n%10!=0)
    {
      r=n%10;
      rev=10*rev+r;
      n=n/10;
    }
    printf("%d",rev);
}
