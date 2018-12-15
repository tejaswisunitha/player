#include<stdio.h>
int main()
{
	int a[20],j,i,n,count=0;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=0;i<n;i++)
	{
		count=0;
		for(j=0;j<n;j++)
		{
			if((a[i]==a[j])&&i!=j)
			{
				count++;
			}
		}
		if(count==0)
		{
			printf("%d",a[i]);
      return 0;
		}
	}
}
