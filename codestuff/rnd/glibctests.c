/* Compare the behavior of memcpy and strncat(..., ..., SIZE_MAX) */

#include <stdint.h>
#include <string.h>
#include <stdio.h>

int main(void)
{
  enum { n = 64 };   /* block size */

  /* array for memcpy */
  char s1[n * 5]; /* two blocks for each of two strings plus the gap */
  char *s2 = s1 + n * 3;	/* the second part */

  /* array for strncat */
  char p1[n * 5];
  char *p2 = p1 + n * 3;

  for (int l = 1; l <= n; l++) /* length, including the terminating 0 */
    for (int i = 0; i < n; i++)     /* offset of the first string */
      for (int j = 0; j < n; j++) { /* offset of the second string */
	/* prepare initial data for memcpy */
	memset(s1, 1, n * 3); /* fill the first part with 1s */
	memset(s2, 2, n * 2); /* fill the second part with 2s */
	s1[i] = 0;	      /* let the first string be empty */
	s2[j + l - 1] = 0;    /* the second string is of size l */
	/* make a copy for strncat */
	memcpy(p1, s1, sizeof p1);

	/* real work */
	memcpy(s1 + i, s2 + j, l);
	strncat(p1 + i, p2 + j, SIZE_MAX);

	/* compare the results */
	if (memcmp(s1, p1, sizeof s1) != 0) {
	  printf("Fail with l = %d, i = %d, j = %d, to = %p, from = %p\n",
		 l, i, j, (void *)(p1 + i), (void *)(p2 + j));

	  printf("after memcpy:\n");
	  for (int z = 0; z < n * 2; z++)
	    printf("%x", (unsigned char)s1[z]);
	  printf("\n");

	  printf("after strncat:\n");
	  for (int z = 0; z < n * 2; z++)
	    printf("%x", (unsigned char)p1[z]);
	  printf("\n");
	  printf("%*s the string should end here\n", i + l, "^");

	  return 1;
	}
      }

  printf("Ok\n");
  return 0;
}
