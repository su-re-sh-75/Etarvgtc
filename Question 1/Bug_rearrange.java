import java.util.*;

public class Bug_rearrange {
    public static List<Integer> rearrange(List<Integer> arr, int n) {
        for (int i = 0; i < n; i++) {
            arr.set(i, arr.get(i) + (arr.get(arr.get(i))) * n);
        }

        for (int i = 0; i < n; i++) {
            arr.set(i, arr.get(i));
        }

        return arr;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Read the size of the list
        int n = scanner.nextInt();

        // Read the elements of the list
        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            arr.add(scanner.nextInt());
        }

        // Call rearrange method
        List<Integer> result = rearrange(arr, n);

        // Print the result
        for (int i = 0; i < n; i++) {
            System.out.print(result.get(i) + " ");
        }

        scanner.close();
    }
}
