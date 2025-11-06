import numpy as np

class Collocation:
    @staticmethod
    def solve(p, q, r, a, b, yp_b=None, N=5, x_eval=None):
        def phi(i, x):
            return x**(2*i-2) * (1 - x**2)
        def phi_prime(i, x):
            if x == 0 and i == 1:
                return 0.0
            return (2*i-2)*x**(2*i-3)*(1 - x**2) - 2*x**(2*i-1)
        def phi_double_prime(i, x):
            if x == 0 and i == 1:
                return -2.0
            term1 = 0.0 if (x == 0 and i <= 1) else (2*i-2)*(2*i-3)*x**(2*i-4)*(1 - x**2)
            term2 = -4*(i-1) * x**(2*i-2)
            term3 = -2 * x**(2*i-2)
            return term1 + term2 + term3

        if x_eval is None:
            x_internal = np.linspace(a + 1e-6, b - 1e-6, N-1)
            x_eval = x_internal
        else:
            x_internal = x_eval

        A = np.zeros((N, N))
        B = np.zeros(N)

        # Collocation equations
        for k, xk in enumerate(x_internal[:-1]):  # leave last for derivative BC
            for i in range(N):
                A[k, i] = phi_double_prime(i+1, xk) + p(xk)*phi_prime(i+1, xk) + q(xk)*phi(i+1, xk)
            B[k] = r(xk)

        # Derivative BC at x=b
        if yp_b is not None:
            for i in range(N):
                A[-1, i] = phi_prime(i+1, b)
            B[-1] = yp_b

        # Solve
        a_coeff = np.linalg.solve(A, B)

        # Evaluate
        y_values = np.zeros_like(x_eval)
        for i in range(N):
            y_values += a_coeff[i] * phi(i+1, x_eval)

        return x_eval, y_values, a_coeff

# Example usage
p = lambda x: -2*x
q = lambda x: 2
r = lambda x: x

x_eval = np.array([0, 0.125, 0.25, 0.375, 0.5])
x_values, y_values, coeffs = Collocation.solve(p, q, r, 0, 0.5, yp_b=1, N=4, x_eval=x_eval)

print(coeffs)