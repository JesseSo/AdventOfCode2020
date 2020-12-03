package com.aoc;

import java.io.*;

public class Main {

    public static void main(String[] args) {

        try {
            File input = new File("src/com/aoc/input.txt");
            BufferedReader br = new BufferedReader(new FileReader(input));
            BufferedReader br2 = new BufferedReader(new FileReader(input));
            System.out.println("Answer1: " + answer1(br)+ " Answer2 : " + answer2(br2));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    private static int answer1(BufferedReader br) throws IOException {
        String line;
        int validCases = 0;
        while ((line = br.readLine()) != null) {
            int count = 0;
            int index = line.indexOf('-');
            int chIndex = line.indexOf(':');
            char ch = line.substring(chIndex-1,chIndex).charAt(0);
            int first = Integer.parseInt(line.substring(0, index));
            int last = Integer.parseInt(line.substring(index+1, index+3).replaceAll("\\s",""));
            for(int i = 0; i < line.length(); i++) {
                if(line.charAt(i) == ch) {
                    count++;
                }
            }
            count--;
            if(count >= first && count <= last){
                validCases++;
            }
        }
        return validCases;
    }

    private static int answer2(BufferedReader br) throws IOException {
        String line;
        int validCases = 0;
        while ((line = br.readLine()) != null) {
            int index = line.indexOf('-');
            int chIndex = line.indexOf(':');
            char ch = line.substring(chIndex - 1, chIndex).charAt(0);
            int first = Integer.parseInt(line.substring(0, index));
            int last = Integer.parseInt(line.substring(index + 1, index + 3).replaceAll("\\s", ""));
            line = line.substring(chIndex + 1, line.length());
            if ((line.charAt(first) == ch || line.charAt(last) == ch) && line.charAt(first) != line.charAt(last)) {
                validCases++;
            }
        }
        return validCases;
    }
}