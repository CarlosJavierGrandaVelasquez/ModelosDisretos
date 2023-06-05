#include <iostream>

// Definición de predicados
bool es_estudiante(std::string nombre) {
    return nombre == "Juan" || nombre == "Pedro";
}

bool es_profesor(std::string nombre) {
    return nombre == "Maria";
}

int main() {
    // Consultas de conocimiento
    std::string nombreConsulta;
    std::cout << "Ingrese el nombre de una persona: ";
    std::cin >> nombreConsulta;

    // Realizar consultas utilizando predicados
    if (es_estudiante(nombreConsulta)) {
        std::cout << nombreConsulta << " es estudiante." << std::endl;
    } else if (es_profesor(nombreConsulta)) {
        std::cout << nombreConsulta << " es profesor(a)." << std::endl;
    } else {
        std::cout << "No se encontró información sobre la persona consultada." << std::endl;
    }

    return 0;
}
