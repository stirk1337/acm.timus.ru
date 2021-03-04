#include <stdio.h>
char a[1000005], b[1000005];
int Count, min;
int main()
{ scanf("%d", &Count);
  min=1;
  for (int i=1; i<=Count; i++)
    scanf("%d %d", &a[i], &b[i]);
// summing
  for (int i=Count; i>=0; i--)
    { int temp = a[i] + b[i];
      a[i] = temp%10;
      a[i-1] += temp/10;
    }
  if (a[0] == 1) min--;
  for (int i=min; i<=Count; i++)
    printf("%d", a[i]);
        return 0;
}