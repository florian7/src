#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>

int collatz_rec(mpz_t n, int max_steps, int steps)
{
	steps++;
	//gmp_printf("%d : %Zd\n", steps, n);

	if (steps > max_steps){
		return -1;
	}

	else if (mpz_cmp_ui(n, 1) == 0){
		return steps;
	}

	else if (mpz_divisible_ui_p(n, 2)){
		mpz_divexact_ui(n, n, 2);
		return collatz_rec(n, max_steps, steps);
	}

	else{
		mpz_mul_ui(n, n, 3);
		mpz_add_ui(n, n, 1);
		return collatz_rec(n, max_steps, steps);
	}


}

int collatz (mpz_t n0, int max_steps)
{
	return collatz_rec(n0, max_steps, -1);
}

