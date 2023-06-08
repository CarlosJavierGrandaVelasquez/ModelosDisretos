package representacionconocimiento;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author Carlos Granda, DCCO-ESPE, Syntax Error
 */
public class RepresentacionConocimiento {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // Creación de la base de conocimientos como una lista de objetos Persona
        List<Persona> conocimiento = new ArrayList<>();

        // Agregar hechos a la base de conocimientos
        conocimiento.add(new Persona("Juan", "estudiante"));
        conocimiento.add(new Persona("Maria", "profesora"));
        conocimiento.add(new Persona("Pedro", "estudiante"));

        // Consultas de conocimiento
        String nombreConsulta = "Juan";

        boolean encontrado = false;

        // Recorrer la base de conocimientos y buscar la ocupación de la persona consultada
        for (Persona persona : conocimiento) {
            if (persona.getNombre().equals(nombreConsulta)) {
                System.out.println("La ocupacion de " + persona.getNombre() + " es " + persona.getOcupacion());
                encontrado = true;
                break;
            }
        }

        if (!encontrado) {
            System.out.println("No se encontro información sobre la persona consultada.");
        }
    }
    
}
