#include <stdio.h>
int main(void)
{
	int n=1;
	int a;
	int k=1;
	
	scanf("%d",&a);
	
	while(1)
	{
		if(a<=n)
		{
			printf("%d",k);
			return 0;
		}
		else
		{
			n += k*6;
			k++;
		}
	}
	return 0;
}