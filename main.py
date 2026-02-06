include <iostream>
include <vector>
include <cmath>
include <algorithm>

extern "C" {
    
    struct Vector3D {
        double* data;
        int size;
    };

    double dot_product(double* vec_a, double* vec_b, int size) {
        double product = 0.0;
        for (int i = 0; i < size; ++i) {
            product += vec_a[i] * vec_b[i];
        }
        return product;
    }

    double magnitude(double* vec, int size) {
        double sum = 0.0;
        for (int i = 0; i < size; ++i) {
            sum += vec[i] * vec[i];
        }
        return std::sqrt(sum);
    }

    double cosine_similarity(double* vec_a, double* vec_b, int size) {
        double dot = dot_product(vec_a, vec_b, size);
        double mag_a = magnitude(vec_a, size);
        double mag_b = magnitude(vec_b, size);

        if (mag_a == 0.0 || mag_b == 0.0) {
            return 0.0;
        }
        return dot / (mag_a * mag_b);
    }

    int find_best_match_index(double* query_vec, double* database_flat, int rows, int cols) {
        int best_index = -1;
        double max_score = -1.0;

        for (int i = 0; i < rows; ++i) {
            double* current_vec = &database_flat[i * cols];
            double score = cosine_similarity(query_vec, current_vec, cols);
            
            if (score > max_score) {
                max_score = score;
                best_index = i;
            }
        }
        return best_index;
    }
}
