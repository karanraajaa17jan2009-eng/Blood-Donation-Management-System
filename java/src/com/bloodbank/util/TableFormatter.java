package com.bloodbank.util;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Utility to render formatted ASCII/Unicode tables in the console.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public class TableFormatter {

    public static void printTable(String title, String[] headers, List<String[]> rows) {
        if (headers == null || headers.length == 0) return;

        int numCols = headers.length;
        int[] colWidths = new int[numCols];

        // Initialize with header widths
        for (int i = 0; i < numCols; i++) {
            colWidths[i] = Math.max(headers[i].length(), 4);
        }

        // Measure row data widths
        for (String[] row : rows) {
            for (int i = 0; i < Math.min(row.length, numCols); i++) {
                if (row[i] != null) {
                    colWidths[i] = Math.max(colWidths[i], row[i].length());
                }
            }
        }

        // Calculate total table width
        int totalWidth = 1; // leading border
        for (int w : colWidths) {
            totalWidth += w + 3; // content + 2 spaces padding + 1 divider
        }

        // Print Title if present
        if (title != null && !title.isEmpty()) {
            System.out.println();
            System.out.println("=".repeat(Math.max(totalWidth, title.length() + 6)));
            System.out.println("   " + title.toUpperCase());
            System.out.println("=".repeat(Math.max(totalWidth, title.length() + 6)));
        }

        // Print Top Border
        printDivider(colWidths, '+', '-');

        // Print Headers
        StringBuilder headerLine = new StringBuilder("|");
        for (int i = 0; i < numCols; i++) {
            headerLine.append(" ").append(padRight(headers[i], colWidths[i])).append(" |");
        }
        System.out.println(headerLine);

        // Print Header Divider
        printDivider(colWidths, '+', '=');

        // Print Data Rows
        if (rows.isEmpty()) {
            String emptyMsg = "No records found.";
            System.out.println("| " + padRight(emptyMsg, totalWidth - 4) + " |");
        } else {
            for (String[] row : rows) {
                StringBuilder rowLine = new StringBuilder("|");
                for (int i = 0; i < numCols; i++) {
                    String val = (i < row.length && row[i] != null) ? row[i] : "";
                    rowLine.append(" ").append(padRight(val, colWidths[i])).append(" |");
                }
                System.out.println(rowLine);
            }
        }

        // Print Bottom Border
        printDivider(colWidths, '+', '-');
        System.out.printf(" Total Count: %d record(s)\n\n", rows.size());
    }

    private static void printDivider(int[] colWidths, char corner, char fill) {
        StringBuilder sb = new StringBuilder();
        sb.append(corner);
        for (int w : colWidths) {
            sb.append(String.valueOf(fill).repeat(w + 2)).append(corner);
        }
        System.out.println(sb);
    }

    private static String padRight(String s, int n) {
        if (s == null) s = "";
        if (s.length() >= n) return s;
        return s + " ".repeat(n - s.length());
    }
}

