#include <gmp.h>

int collatz (mpz_t n0, int max_steps);
int collatz_rec (mpz_t n, int max_steps, int steps);
