#include <stdio.h>
#include <string.h>
  
int main()
{
    char s1[25],temp[20];
    printf("Enter a string:");
    gets(s1);
	strcpy(temp,s1);
	strrev(s1);
	printf("The reverse of given string is\t");
	puts(s1);
	int res=strcmp(s1,temp);
	if (res==0)
	printf("The given string is a palindrome string.");
	else
	printf("The given string is not a palindrome string.");
    return 0;
}
