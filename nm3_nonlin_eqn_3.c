#include <stdio.h>
#include <gsl/gsl_multimin.h>

// Define the Rosenbrock function
double rosenbrock(const gsl_vector *v, void *params) {
    double x = gsl_vector_get(v, 0);
    double y = gsl_vector_get(v, 1);

    return (1 - x) * (1 - x) + 100 * (y - x * x) * (y - x * x);
}

int main() {
    const gsl_multimin_fminimizer_type *minimizer_type = gsl_multimin_fminimizer_nmsimplex2;
    gsl_multimin_fminimizer *minimizer = gsl_multimin_fminimizer_alloc(minimizer_type, 2);

    gsl_vector *initial_guess = gsl_vector_alloc(2);
    gsl_vector_set(initial_guess, 0, 0.0);
    gsl_vector_set(initial_guess, 1, 0.0);

    gsl_multimin_function minex_func;
    minex_func.n = 2;
    minex_func.f = &rosenbrock;
    minex_func.params = 0;

    gsl_multimin_fminimizer_set(minimizer, &minex_func, initial_guess, 0.01, 1e-4);

    size_t iter = 0;
    int status;
    do {
        iter++;
        status = gsl_multimin_fminimizer_iterate(minimizer);
        if (status)
            break;

        status = gsl_multimin_test_size(minimizer->size, 1e-4);
    } while (status == GSL_CONTINUE && iter < 100);

    printf("Minimum found at (%g, %g)\n", gsl_vector_get(minimizer->x, 0), gsl_vector_get(minimizer->x, 1));

    gsl_multimin_fminimizer_free(minimizer);
    gsl_vector_free(initial_guess);

    return 0;
}

