#include "stdio.h"
#include "string.h"

int isPalindrome(char* test_str)
{
	int flag = 1;
	int length = strlen(test_str);
	int half = length / 2;
	int i = 0;
	while(i < half)
	{
		if (test_str[i] != test_str[length - i - 1])
		{
			flag = 0;
			break;
		}
		i+=1;
	}
	return flag;
}

int main()
{
	char test_str[100];
	gets(test_str);
	int flag = isPalindrome(test_str);
	if (flag)
	{
		printf("True");
	}
	else
	{
		printf("False");
	}
	printf("\n");
	return 0;
}