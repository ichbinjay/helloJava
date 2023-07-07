class DominoPiling{
    public static void main(String[] args) {
        int m = 3;
        int n = 3;
        int area = m*n;
        int domino = 2;
        int maxDomino = area/domino;
        System.out.println(maxDomino);
    }
}