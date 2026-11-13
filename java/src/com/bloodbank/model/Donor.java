package com.bloodbank.model;

import java.time.LocalDate;

/**
 * Represents a voluntary blood donor.
 * Author: Karan Raajaa V (Reg. No: 732925ITR045)
 */
public class Donor {
    private int donorId;
    private String name;
    private int age;
    private String gender;
    private String contactNumber;
    private String email;
    private String bloodGroup;
    private String city;
    private LocalDate registrationDate;

    public Donor() {
        this.registrationDate = LocalDate.now();
    }

    public Donor(int donorId, String name, int age, String gender, String contactNumber, 
                 String email, String bloodGroup, String city, LocalDate registrationDate) {
        this.donorId = donorId;
        this.name = name;
        this.age = age;
        this.gender = gender;
        this.contactNumber = contactNumber;
        this.email = email;
        this.bloodGroup = bloodGroup;
        this.city = city;
        this.registrationDate = (registrationDate != null) ? registrationDate : LocalDate.now();
    }

    // Constructor without ID (for new donor registration)
    public Donor(String name, int age, String gender, String contactNumber, 
                 String email, String bloodGroup, String city) {
        this(0, name, age, gender, contactNumber, email, bloodGroup, city, LocalDate.now());
    }

    public int getDonorId() {
        return donorId;
    }

    public void setDonorId(int donorId) {
        this.donorId = donorId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public String getContactNumber() {
        return contactNumber;
    }

    public void setContactNumber(String contactNumber) {
        this.contactNumber = contactNumber;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getBloodGroup() {
        return bloodGroup;
    }

    public void setBloodGroup(String bloodGroup) {
        this.bloodGroup = bloodGroup;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public LocalDate getRegistrationDate() {
        return registrationDate;
    }

    public void setRegistrationDate(LocalDate registrationDate) {
        this.registrationDate = registrationDate;
    }

    @Override
    public String toString() {
        return String.format("Donor[ID=%d, Name='%s', BloodGroup='%s', Age=%d, Phone='%s', City='%s']",
                donorId, name, bloodGroup, age, contactNumber, city);
    }
}

