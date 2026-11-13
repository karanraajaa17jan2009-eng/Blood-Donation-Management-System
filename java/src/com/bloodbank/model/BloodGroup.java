package com.bloodbank.model;

/**
 * Standard ABO and Rh blood group types.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public enum BloodGroup {
    A_POSITIVE("A+"),
    A_NEGATIVE("A-"),
    B_POSITIVE("B+"),
    B_NEGATIVE("B-"),
    AB_POSITIVE("AB+"),
    AB_NEGATIVE("AB-"),
    O_POSITIVE("O+"),
    O_NEGATIVE("O-");

    private final String code;

    BloodGroup(String code) {
        this.code = code;
    }

    public String getCode() {
        return code;
    }

    public static boolean isValid(String code) {
        if (code == null) return false;
        String trimmed = code.trim().toUpperCase();
        for (BloodGroup bg : values()) {
            if (bg.code.equalsIgnoreCase(trimmed)) {
                return true;
            }
        }
        return false;
    }

    public static BloodGroup fromString(String code) {
        if (code == null) throw new IllegalArgumentException("Blood group cannot be null");
        String trimmed = code.trim().toUpperCase();
        for (BloodGroup bg : values()) {
            if (bg.code.equalsIgnoreCase(trimmed)) {
                return bg;
            }
        }
        throw new IllegalArgumentException("Invalid blood group code: " + code);
    }
}

