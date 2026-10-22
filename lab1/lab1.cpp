#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <set>
#include <iomanip>

double get_coef(int index, int argc, char* argv[], const std::string& prompt) {
    if (index < argc) {
        try {
            size_t pos;
            double val = std::stod(argv[index], &pos);
            if (pos == std::string(argv[index]).length()) {
                return val;
            }
        } catch (...) {
        }
    }

    std::string input_str;
    while (true) {
        std::cout << prompt << " ";
        std::cin >> input_str;
        try {
            size_t pos;
            double val = stod(input_str, &pos);
            if (pos == input_str.length()) {
                return val;
            } else {
                std::cout << "Ошибка: введено некорректное значение.\n";
            }
        } catch (...) {
            std::cout << "Ошибка: введено некорректное значение.\n";
        }
    }
}

std::set<double> calculate_roots(double a, double b, double c) {
    std::set<double> roots;

    if (a == 0.0) {
        if (b != 0.0) {
            double y = -c / b;
            if (y > 0.0) {
                roots.insert(sqrt(y));
                roots.insert(-sqrt(y));
            } else if (y == 0.0) {
                roots.insert(0.0);
            }
        }
    } else {
        double D = b * b - 4 * a * c;
        std::cout << "Дискриминант D = " << D << "\n";

        if (D >= 0.0) {
            std::vector<double> y_roots;
            if (D == 0.0) {
                y_roots.push_back(-b / (2.0 * a));
            } else {
                y_roots.push_back((-b + sqrt(D)) / (2.0 * a));
                y_roots.push_back((-b - sqrt(D)) / (2.0 * a));
            }

            for (double y : y_roots) {
                if (y > 0.0) {
                    roots.insert(sqrt(y));
                    roots.insert(-sqrt(y));
                } else if (y == 0.0) {
                    roots.insert(0.0);
                }
            }
        }
    }
    
    return roots;
}

int main(int argc, char* argv[]) {
    std::cout << "Решение биквадратного уравнения: Ax^4 + Bx^2 + C = 0\n";
    double a = get_coef(1, argc, argv, "Введите A:");
    double b = get_coef(2, argc, argv, "Введите B:");
    double c = get_coef(3, argc, argv, "Введите C:");

    std::set<double> roots = calculate_roots(a, b, c);

    if (roots.empty()) {
        std::cout << "Нет действительных корней\n";
    } else {
        std::cout << "Найдены корни (" << roots.size() << "): ";
        std::cout << std::fixed << std::setprecision(4);
        for (double root : roots) {
            std::cout << root << " ";
        }
        std::cout << "\n";
    }

    return 0;
}