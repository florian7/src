#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#include "matrix.h"

void matrix_allocate(matrix * A)
{
	size_t i;

	if (A->m_max == 0)
		A->m_max = 3;

	if (A->n_max == 0)
		A->n_max = 3;

	A->a = malloc(sizeof(float *) * A->m_max);

	for (i = 0; i < A->m_max; i++) {
		A->a[i] = malloc(sizeof(float) * A->n_max);
	}
}

void matrix_free(matrix * A)
{
	size_t i;
	
	for (i = 0; i < A->m_max; i++)
		free(A->a[i]);
	free(A->a);
}

static void matrix_realloc_n(matrix * A)
{
	size_t i;

	A->n_max *= 2;
	for (i = 0; i < A->m_max; i++) {
		A->a[i] = realloc(A->a[i], sizeof(float) * A->n_max);

		if (A->a[i] == NULL) {
			errno = ENOMEM;
			perror("matrix_realloc_n");
			exit(-1);
		}
	}
}

static void matrix_realloc_m(matrix * A)
{
	size_t i = A->m_max;

	A->m_max *= 2;
	A->a = realloc(A->a, sizeof(float *) * A->m_max);

	for (;i < A->m_max; i++) {
		A->a[i] = malloc(sizeof(float) * A->n_max);
	}

	if (A->a == NULL) {
		errno = ENOMEM;
		perror("matrix_realloc_m");
		exit(-1);
	}
}

void matrix_set(matrix * A, size_t i, size_t j, float val)
{
	while (j + 1> A->n_max)
		matrix_realloc_n(A);

	while (i + 1> A->m_max)
		matrix_realloc_m(A);

	A->a[i][j] = val;
}

int matrix_fill(matrix * A, char * input)
{
	size_t i, j;
	float val;
	enum {
		start,
		open,
		read,
		delim,
		close,
		end
	} status = start;

	while (*input != '\0') {

		switch (status) {
		case start:
			if (*input != '{' || *(input + 1) != '{') {
				errno = EINVAL;
				goto error;
			}

			i = 0, input++;
			status = open;
			break; 
			
		case open:
			if (A->m < i + 1) A->m = i + 1;
			j = 0, input++;
			status = read;
			break;

		case read:
			if (A->n < j + 1) A->n = j + 1;

			val = strtof(input, &input);
			if (errno < 0) goto error;

			matrix_set(A, i, j, val);
			j++;

			if (*input == ',')
				status = delim;

			else if (*input == '}')
				status = close;

			else {
				errno = EINVAL;
				goto error;
			}

			break;

		case delim:
			input++;

			if (*input == '{')
				status = open;

			else 
				status = read;

			break;

		case close:
			input++;

			if (*input == ',')
				status = delim;

			else if (*input == '}')
				status = end;

			else {
				errno = EINVAL;
				goto error;
			}

			i++;

			break;

		case end:
			input++;

			break;
		}
	}

	return 0;

error:
	perror("matrix_fill");
	return -1;
}

int matrix_multiply(matrix * C, matrix * A, matrix * B)
{
	size_t i, j, m, k;
	float sum;

	if (A->n != B->m) {
		fprintf(stderr, "matrix_multiply: Matrices A and B are not multiplicable\n");
		return -1;
	}

	memset(C, 0, sizeof(matrix));
	C->m_max = A->m, C->n_max = B->n;
	C->m = A->m, C->n = B->n;
	matrix_allocate(C);

	m = A->n;
	for (i = 0; i < A->m; i++) {
		for (j = 0; j < B->n; j++) {

			sum = 0;
			for (k = 0; k < m; k++) {
				sum += A->a[i][k] * B->a[k][j];
			}
			matrix_set(C, i, j, sum);
		}
	}

	return 0;
}

void matrix_print(matrix * A)
{
	size_t i, j;

	printf("Allocated: %dx%d\t", A->m_max, A->n_max);
	printf("Used: %dx%d\n", A->m, A->n);

	for (i = 0; i < A->m; i++) {
		for (j = 0; j < A->n; j++) {
			printf("%-8.1f", A->a[i][j]);
		}
		printf("\n");
	}
}
