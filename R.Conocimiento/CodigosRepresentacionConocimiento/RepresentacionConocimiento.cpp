#include <iostream>
#include <vector>

// Definición de la estructura de conocimiento
struct Persona {
    std::string nombre;
    std::string ocupacion;
};

int main() {
    // Creación de la base de conocimientos
    std::vector<Persona> conocimiento;

    // Agregar hechos a la base de conocimientos
    conocimiento.push_back({"Juan", "estudiante"});
    conocimiento.push_back({"Maria", "profesora"});
    conocimiento.push_back({"Pedro", "estudiante"});

    // Consultas de conocimiento
    std::string nombreConsulta;
    std::cout << "Ingrese el nombre de una persona: ";
    std::cin >> nombreConsulta;

    bool encontrado = false;

    // Recorrer la base de conocimientos y buscar la ocupación de la persona consultada
    for (const auto& persona : conocimiento) {
        if (persona.nombre == nombreConsulta) {
            std::cout << "La ocupacion de " << persona.nombre << " es " << persona.ocupacion << std::endl;
            encontrado = true;
            break;
        }
    }

    if (!encontrado) {
        std::cout << "No se encontro información sobre la persona consultada." << std::endl;
    }

    return 0;
}
