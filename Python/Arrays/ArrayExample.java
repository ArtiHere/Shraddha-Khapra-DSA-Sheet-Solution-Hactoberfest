public class ArrayExample {
    public static void main(String[] args) {
        // Creating an array of integers
        int[] numbers = new int[5]; // Creates an array of size 5

        // Initializing the array
        numbers[0] = 10;
        numbers[1] = 20;
        numbers[2] = 30;
        numbers[3] = 40;
        numbers[4] = 50;

        // Accessing elements in the array
        System.out.println("The element at index 2 is: " + numbers[2]);

        // Modifying an element
        numbers[2] = 35;

        // Looping through the array and printing its elements
        System.out.println("Array elements:");
        for (int i = 0; i < numbers.length; i++) {
            System.out.println("Element at index " + i + ": " + numbers[i]);
        }
    }
}
