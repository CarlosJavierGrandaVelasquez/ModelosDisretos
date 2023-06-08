package predicatelogicexample;
import java.util.function.Predicate;

/**
 *
 * @author Carlos Granda, DCCO-ESPE, Syntax Error
 */
public class PredicateLogicExample {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Predicate<Integer> p = x -> x > 0;  // P(x): x es mayor que 0
        Predicate<Integer> q = x -> x % 2 == 0;  // Q(x): x es par

        boolean result = checkPredicate(p, q);
        System.out.println("Resultado: " + result);
    }

    public static boolean checkPredicate(Predicate<Integer> p, Predicate<Integer> q) {
        for (int i = -10; i <= 10; i++) {
            if (p.test(i) && !q.test(i)) {
                return false;
            }
        }
        return true;
    }
}
