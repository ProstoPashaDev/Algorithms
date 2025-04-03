//Pavel Khramov
package org.example;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.ArrayList;
import java.util.Scanner;

public class DSA_B {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        double[][] points = new double[n][2];
        Double[] dist = new Double[n];
        for (int i = 0; i < n; i++) {
            points[i][0] = Double.parseDouble(scanner.next());
            points[i][1] = Double.parseDouble(scanner.next());
            dist[i] = (points[i][0] * points[i][0] + points[i][1] * points[i][1]);
        }
        BucketNumberCounting<Double> counter = i -> {
            if (i >= 0 && i < 1) {
                return ((int)(i * 10)) % 10;
            } else {
                return ((int)(i * 10)) % 10 + 9;
            }
        };
        Comparator<Double> cmp = (i, j) -> Double.compare(i, j) > 0;
        printAnswer(PavelKhramov_bucket_srt(dist, n, 20, counter, cmp), points, 20);

    }

    //Comparator for inner bubbleSort
    static private <T> ArrayList<Integer>[] PavelKhramov_bucket_srt(T[] dist, int n, int bucketNumber, BucketNumberCounting<T> counter, Comparator<T> cmp) {
        //1 - -0.1
        ArrayList<T>[] distList = new ArrayList[bucketNumber+1];
        ArrayList<Integer>[] indList = new ArrayList[bucketNumber+1];
        for (int i = 0; i <= bucketNumber; i++) {
            distList[i] = new ArrayList<>();
            indList[i] = new ArrayList<>();
        }
        for (int i = 0; i < n; i++) {
            distList[counter.count(dist[i])].add(dist[i]);
            indList[counter.count(dist[i])].add(i);
        }
        for (int i = 0; i <= bucketNumber; i++) {
            bubbleSort(indList[i], distList[i], distList[i].size(), cmp);
        }
        return indList;
    }

    static private void printAnswer(ArrayList<Integer>[] indList, double[][] points, int n) {
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j < indList[i].size(); j++) {
                BigDecimal x = new BigDecimal(String.valueOf(points[indList[i].get(j)][0])).setScale(4, RoundingMode.HALF_UP);
                BigDecimal y = new BigDecimal(String.valueOf(points[indList[i].get(j)][1])).setScale(4, RoundingMode.HALF_UP);
                System.out.println(x + " " + y);

            }
        }
    }

    static private <T> void bubbleSort(ArrayList<Integer> pointsIndex, ArrayList<T> list, int n, Comparator<T> cmp) {
        boolean swapped = true;
        while (swapped) {
            swapped = false;
            for (int i = 1; i < n; i++) {
                //i1 < i2
                if (cmp.compare(list.get(i - 1), list.get(i))){
                    //Swap point and list, because they are connected
                    T temp = list.get(i);
                    list.set(i, list.get(i - 1));
                    list.set(i - 1, temp);

                    int temp2 = pointsIndex.get(i);
                    pointsIndex.set(i, pointsIndex.get(i - 1));
                    pointsIndex.set(i - 1, temp2);

                    swapped = true;
                }
            }
        }
    }
}
@FunctionalInterface
interface BucketNumberCounting<T> {
    int count(T t);
}
@FunctionalInterface
interface Comparator<T> {
    boolean compare(T t1, T t2);
}