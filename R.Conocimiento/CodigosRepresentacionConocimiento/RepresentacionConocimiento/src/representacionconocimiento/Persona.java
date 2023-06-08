package representacionconocimiento;


/**
 *
 * @author Carlos Granda, DCCO-ESPE, Syntax Error
 */
// Definición de la clase Persona para representar el conocimiento
class Persona {
    private String nombre;
    private String ocupacion;

    public Persona(String nombre, String ocupacion) {
        this.nombre = nombre;
        this.ocupacion = ocupacion;
    }

    public String getNombre() {
        return nombre;
    }

    public String getOcupacion() {
        return ocupacion;
    }
}
