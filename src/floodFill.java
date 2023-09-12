public class floodFill {

    private static final int[][] image = { { 1, 1, 1 }, { 1, 1, 0 }, { 1, 0, 1 } };

    public static int[][] fill() {
        int[][] result = new int[image.length][image[0].length];

        for (int i = 0; i < image.length; i++) {
            System.arraycopy(image[i], 0, result[i], 0, image[0].length);
        }



        for (int i = 0; i < image.length; i++) {
            for (int j = 0; j < image[0].length; j++) {
                if (image[i][j] != 0) { // above pixel
                    int newColor = 2;
                    if (i > 0) {
                        if (image[i][j] == image[i - 1][j]) {
                            result[i - 1][j] = newColor;
                        }
                    }

                    if (i < image.length - 1) { // below pixel
                        if (image[i][j] == image[i + 1][j]) {
                            result[i + 1][j] = newColor;
                        }
                    }

                    if (j > 0) { // left pixel
                        if (image[i][j] == image[i][j - 1]) {
                            result[i][j - 1] = newColor;
                        }
                    }

                    if (j < image[0].length - 1) { // right pixel
                        if (image[i][j] == image[i][j + 1]) {
                            result[i][j + 1] = newColor;
                        }
                    }
                }
            }
        }
        return result;
    }

    public static void main(String[]args){
        int[][] result = fill();
        for (int[] ints : result) {
            for (int j = 0; j < result[0].length; j++) {
                System.out.print(ints[j] + " ");
            }
            System.out.println();
        }
    }
}