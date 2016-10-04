#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "matrix.h"

int main (int argc, char * argv [])
{
	matrix A, B, C;

	if (argc == 2) {
		memset(&A, 0, sizeof(matrix));
		matrix_allocate(&A);
		matrix_fill(&A, argv[1]);
		matrix_print(&A);
		matrix_free(&A);
	}

	else if (argc == 4) {
		if (!strcmp(argv[2], "*")) {

			memset(&A, 0, sizeof(matrix));
			matrix_allocate(&A);
			matrix_fill(&A, argv[1]);

			memset(&B, 0, sizeof(matrix));
			matrix_allocate(&B);
			matrix_fill(&B, argv[3]);

			matrix_multiply(&C, &A, &B);
			matrix_print(&C);

			matrix_free(&A), matrix_free(&B), matrix_free(&C); 
		}
	}
}
