#include <iostream>

using namespace std;

void remove_zeros(int* items, int size) {
    for (int i = size - 1; i >= 0; i--) {
        if (items[i] == 0) {
            if (size > 1) {
                for (int j = i; j < size - 1; j++) {
                    items[j] = items[j + 1];
                }
                size--;
            }
        } else {
            break;
        }
    }
}

void add(const int* poly1, int size1, const int* poly2, int size2, int* result) {
    int size = max(size1, size2);
    for (int i = 0; i < size; i++) {
        if (i < size1) {
            result[i] += poly1[i];
        }
        if (i < size2) {
            result[i] += poly2[i];
        }
    }
}

void split(const int* poly1, int size1, const int* poly2, int size2, int* result1, int* result2) {
    int mid = max(size1, size2) / 2;
    for (int i = 0; i < mid; i++) {
        result1[i] = poly1[i];
        result2[i] = poly1[i + mid];
    }
    for (int i = 0; i < mid; i++) {
        result1[i + mid] = poly2[i];
        result2[i + mid] = poly2[i + mid];
    }
}

void increase_exponent(const int* poly, int size, int* result, int n) {
    for (int i = 0; i < n; i++) {
        result[i] = 0;
    }
    for (int i = 0; i < size; i++) {
        result[i + n] = poly[i];
    }
}

void subtract(const int* poly1, int size1, const int* poly2, int size2, int* result) {
    for (int i = 0; i < size2; i++) {
        result[i] = -poly2[i];
    }
    add(poly1, size1, result, size2, result);
}

void multiply_polynomial(const int* poly1, int size1, const int* poly2, int size2, int* result, int m, int n) {
    if (m == 0 || n == 0) {
        return;
    }

    if (m == 1) {
        if (poly1[0] == 0) {
            result[0] = 0;
        } else {
            for (int i = 0; i < n; i++) {
                result[i] = poly1[0] * poly2[i];
            }
        }
        return;
    } else if (n == 1) {
        if (poly2[0] == 0) {
            result[0] = 0;
        } else {
            for (int i = 0; i < m; i++) {
                result[i] = poly2[0] * poly1[i];
            }
        }
        return;
    }

    n = max(m, n);
    if (n % 2 != 0) {
        n = n - 1;
    }

    int* AB_first = new int[n];
    int* AB_second = new int[n];
    split(poly1, m, poly2, n, AB_first, AB_second);

    int* add_A = new int[n];
    int* add_B = new int[n];
    add(AB_first, n, AB_second, n, add_A);
    add(AB_first, n, AB_second, n, add_B);

    int* Y = new int[2 * n];
    int* U = new int[2 * n];
    int* Z = new int[2 * n];
    multiply_polynomial(add_A, n, add_B, n, Y, 2 * n, 2 * n);
    multiply_polynomial(AB_first, n, AB_second, n, U, n, n);
    multiply_polynomial(AB_first, n, AB_second, n, Z, n, n);

    subtract(Y, 2 * n, add(U, 2 * n, Z, 2 * n), 2 * n, Y);
    increase_exponent(Y, 2 * n, Y, n / 2);
    increase_exponent(Z, n, Z, n);

    add(Y, 2 * n, add(U, 2 * n, Z, 2 * n), 2 * n, result);
    remove_zeros(result, 2 * n);

    delete[] AB_first;
    delete[] AB_second;
    delete[] add_A;
    delete[] add_B;
    delete[] Y;
    delete[] U;
    delete[] Z;
}

int main() {
    int poly1[] = {2, 0, 5, 7};
    int poly2[] = {3, 4, 2};
    int m = sizeof(poly1) / sizeof(poly1[0]);
    int n = sizeof(poly2) / sizeof(poly2[0]);

    int* result = new int[m + n - 1];
    multiply_polynomial(poly1, m, poly2, n, result, m, n);

    cout << "Result: ";
    for (int i = 0; i < m + n - 1; i++) {
        cout << result[i] << " ";
    }
    cout << endl;

    delete[] result;

    return 0;
}
