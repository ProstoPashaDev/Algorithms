//Pavel Khramov
//Idea of storing index of initial Array was discussed with Anna Meshcheriakova
package org.example;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.DataInputStream;
import java.io.InputStream;

public class Main {
    static int ma1;
    static int mi1;
    static int ma2;
    static int mi2;
    static int[] ind;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Parser parser = new Parser(System.in);
        int n = parser.nextInt();
        int[] numbers = new int[n];
        mi1 = 999999999;
        ma1 = -9999999;
        for (int i = 0; i < n; i++) {
            //numbers[i] = scanner.nextInt();
            numbers[i] = parser.nextInt();
            mi1 = Math.min(mi1, numbers[i]);
            ma1 = Math.max(ma1, numbers[i]);
        }
        int l1 = ma1 - mi1 + 1;
        Integer[] count = new Integer[l1];
        ArrayList<Integer>[] indList = new ArrayList[l1];
        for (int i = 0; i < l1; i++) {
            indList[i] = new ArrayList<>();
            count[i] = 0;
        }
        for (int i = 0; i < n; i++) {
            count[numbers[i] - mi1]++;
            indList[numbers[i] - mi1].add(i);
        }
        Converter<Integer> converter = a -> a;
        Integer[] answersFreq = PavelKhramov_count_srt(count, l1, converter, Integer.class);
        for (int i = 0; i < l1; i++) {
            if (answersFreq[i] != 0) {
                for (int j = 0; j < indList[ind[i]].size(); j++) {
                    System.out.println((ind[i] + mi1) + " " + (indList[ind[i]].get(j)));
                }
            }
        }

    }

    static public <T> T[] PavelKhramov_count_srt(T[] numbers, int n, Converter<T> converter, Class<T> t) {
        ma2 = -999999999;
        mi2 = 99999999;
        for (int i = 0; i < n; i++) {
            ma2 = Math.max(ma2, converter.convert(numbers[i]));
            mi2 = Math.min(mi2, converter.convert(numbers[i]));
        }
        int l = ma2 - mi2 + 1;
        int[] count = new int[l];
        for (int i = 0; i < n; i++) {
            count[converter.convert(numbers[i]) - mi2]++;
        }

        //Accum array
        int[] prevsum = new int[l];
        prevsum[0] = count[0];
        for (int i = 1; i < l; i++) {
            prevsum[i] = prevsum[i - 1] + count[i];
        }

        T[] answer = (T[]) Array.newInstance(t, n);

        ind = new int[n];
        for (int i = n - 1; i >= 0; i--) {
            answer[prevsum[converter.convert(numbers[i]) - mi2] - 1] = numbers[i];
            ind[prevsum[converter.convert(numbers[i]) - mi2] - 1] = i;
            prevsum[converter.convert(numbers[i]) - mi2]--;
        }
        return answer;
    }
}
@FunctionalInterface
interface Converter<T> {
    int convert(T t);
}

class Parser {

    final private int BUFFER_SIZE = 1 << 16;

    private DataInputStream din;

    private byte[] buffer;

    private int bufferPointer, bytesRead;



    public Parser(InputStream in) {

        din = new DataInputStream(in);

        buffer = new byte[BUFFER_SIZE];

        bufferPointer = bytesRead =  0;

    }

    public String nextString(int maxSize) {

        byte[] ch = new byte[maxSize];

        int point =  0;

        try {

            byte c = read();

            while (c == ' ' || c == '\n' || c=='\r')

                c = read();

            while (c != ' ' && c != '\n' && c!='\r') {

                ch[point++] = c;

                c = read();

            }

        } catch (Exception e) {}

        return new String(ch, 0,point);

    }

    public int nextInt() {

        int ret =  0;

        boolean neg;

        try {

            byte c = read();

            while (c <= ' ')

                c = read();

            neg = c == '-';

            if (neg)

                c = read();

            do {

                ret = ret * 10 + c - '0';

                c = read();

            } while (c > ' ');



            if (neg) return -ret;

        } catch (Exception e) {}

        return ret;

    }

    public long nextLong() {

        long ret =  0;

        boolean neg;

        try {

            byte c = read();

            while (c <= ' ')

                c = read();

            neg = c == '-';

            if (neg)

                c = read();

            do {

                ret = ret * 10 + c - '0';

                c = read();

            } while (c > ' ');



            if (neg) return -ret;

        } catch (Exception e) {}

        return ret;

    }

    private void fillBuffer() {

        try {

            bytesRead = din.read(buffer, bufferPointer =  0, BUFFER_SIZE);

        } catch (Exception e) {}

        if (bytesRead == -1) buffer[ 0] = -1;

    }



    private byte read() {

        if (bufferPointer == bytesRead) fillBuffer();

        return buffer[bufferPointer++];

    }

}