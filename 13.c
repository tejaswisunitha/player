#include <stdio.h>
int main()
{
    int m,rev=0,rem,sum=0;
    scanf("%d",&m);
    while(m!=0)
    {
        rem=m%10;
        sum=sum+(rem*rem);
        m=m/10;
    }
    printf("%d",sum);
	return 0;
}
