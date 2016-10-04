#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <limits.h>
#include <gmp.h>


#include "collatz.h"

int main (int argc, char * argv [])
{
	unsigned int max_steps = 10000000;
	int err;
	mpz_t n0;

	if (argc != 2){
		printf("Usage: %s <n0>\n", argv[0]);
		return -1;
	}
	
	err = mpz_init_set_str(n0, argv[1], 10);
	if (err < 0){
		perror("Could not parse argument");
		exit(EXIT_FAILURE);
	}

	int steps = collatz(n0, max_steps);

	if (steps < 0){
		printf(
			"Collatz(%Zd) did not end in %d steps (max_steps)\n", 
			n0, max_steps);
	}
	else{
		printf(
			"Collatz(%Zd) ended in %d steps\n",
			n0, steps);
	}

	return 0;
}
