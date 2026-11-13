package com.bloodbank.util;

import com.bloodbank.model.BloodGroup;
import java.util.regex.Pattern;

/**
 * Validates user inputs according to clinical and business constraints.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public class InputValidator {

    private static final Pattern PHONE_PATTERN = Pattern.compile("^[6-9]\\d{9}$");
    private static final Pattern EMAIL_PATTERN = Pattern.compile("^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,6}$");
    private static final Pattern NAME_PATTERN = Pattern.compile("^[A-Za-z ]{2,60}$");

    public static boolean isValidName(String name) {
        return name != null && NAME_PATTERN.matcher(name.trim()).matches();
    }

    public static boolean isValidAge(int age) {
        return age >= 18 && age <= 65;
    }

    public static boolean isValidPhone(String phone) {
        return phone != null && PHONE_PATTERN.matcher(phone.trim()).matches();
    }

    public static boolean isValidEmail(String email) {
        return email != null && EMAIL_PATTERN.matcher(email.trim()).matches();
    }

    public static boolean isValidBloodGroup(String bg) {
        return BloodGroup.isValid(bg);
    }

    public static boolean isValidUnits(int units) {
        return units > 0 && units <= 10;
    }

    public static boolean isValidHemoglobin(double hb) {
        return hb >= 12.0 && hb <= 20.0;
    }
}

