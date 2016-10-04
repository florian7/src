typedef struct {
	size_t m, m_max;
	size_t n, n_max;
	float ** a;
} matrix;


void matrix_allocate(matrix * A);
void matrix_free(matrix * A);
void matrix_set(matrix * A, size_t i, size_t j, float val);
int matrix_fill(matrix * A, char * input);
int matrix_multiply(matrix * C, matrix * A, matrix * B);
void matrix_print(matrix * A);
