-- =============================================================================
-- Blood Donation Management and Donor Availability Analysis System
-- Sample Dataset (DML)
-- Student: Karan Raajaa V | Register No: 732925ITR045 | Class: 25IT3A&B
-- Institution: Velalar College of Engineering and Technology, Erode - 12
-- =============================================================================

-- -----------------------------------------------------------------------------
-- 1. Populate blood_stock with all 8 ABO/Rh blood groups
-- -----------------------------------------------------------------------------
INSERT INTO blood_stock (blood_group, available_units, minimum_threshold, last_updated) VALUES
('A+', 16, 5, '2026-11-10 09:30:00'),
('A-', 6, 4, '2026-11-08 14:15:00'),
('B+', 20, 5, '2026-11-12 11:00:00'),
('B-', 3, 4, '2026-11-05 16:45:00'),
('AB+', 8, 4, '2026-11-09 10:20:00'),
('AB-', 2, 4, '2026-11-02 12:00:00'),
('O+', 24, 6, '2026-11-13 08:30:00'),
('O-', 4, 5, '2026-11-07 17:10:00');

-- -----------------------------------------------------------------------------
-- 2. Populate donors with realistic profiles
-- -----------------------------------------------------------------------------
INSERT INTO donors (donor_id, name, age, gender, contact_number, email, blood_group, city, registration_date) VALUES
(1, 'Karan Raajaa V', 20, 'Male', '9842104501', 'karan.raajaa@vcet.ac.in', 'O+', 'Erode', '2026-01-15'),
(2, 'Praveen Kumar S', 21, 'Male', '9789123450', 'praveen.k@gmail.com', 'A+', 'Perundurai', '2026-02-10'),
(3, 'Dharshini M', 20, 'Female', '9443210987', 'dharshini.m@yahoo.com', 'B+', 'Bhavani', '2026-02-18'),
(4, 'Sanjay Balaji R', 22, 'Male', '9944556677', 'sanjay.balaji@outlook.com', 'O-', 'Gobichettipalayam', '2026-03-05'),
(5, 'Ananya Sivakumar', 23, 'Female', '9894123456', 'ananya.s@gmail.com', 'AB+', 'Erode', '2026-03-22'),
(6, 'Vigneshwaran K', 28, 'Male', '9751098765', 'vicky.k@gmail.com', 'A-', 'Coimbatore', '2026-04-12'),
(7, 'Sneha Ramakrishnan', 25, 'Female', '9629876543', 'sneha.ram@gmail.com', 'B-', 'Salem', '2026-04-29'),
(8, 'Manojkumar T', 34, 'Male', '9500123456', 'manoj.t@hotmail.com', 'AB-', 'Tirupur', '2026-05-14'),
(9, 'Deepa Lakshmanan', 29, 'Female', '9488112233', 'deepa.l@gmail.com', 'O+', 'Erode', '2026-05-28'),
(10, 'Aravind Swaminathan', 31, 'Male', '9843001122', 'aravind.s@gmail.com', 'A+', 'Karur', '2026-06-10'),
(11, 'Kavitha Natarajan', 27, 'Female', '9787665544', 'kavitha.n@gmail.com', 'B+', 'Namakkal', '2026-06-25'),
(12, 'Hariharan G', 24, 'Male', '9965443322', 'hari.g@gmail.com', 'O-', 'Coimbatore', '2026-07-04'),
(13, 'Swathi Chandran', 22, 'Female', '9842778899', 'swathi.c@gmail.com', 'A+', 'Erode', '2026-07-20'),
(14, 'Gowtham Raj P', 26, 'Male', '9715223344', 'gowtham.raj@gmail.com', 'B+', 'Dharapuram', '2026-08-05'),
(15, 'Divya Bharathi K', 23, 'Female', '9600554433', 'divya.b@gmail.com', 'O+', 'Salem', '2026-08-18'),
(16, 'Mohanraj S', 38, 'Male', '9524110099', 'mohanraj.s@gmail.com', 'A-', 'Tirupur', '2026-09-02'),
(17, 'Nithya Sundaram', 30, 'Female', '9442998877', 'nithya.s@gmail.com', 'AB+', 'Erode', '2026-09-15'),
(18, 'Karthikeyan B', 42, 'Male', '9894002211', 'karthik.b@gmail.com', 'B-', 'Coimbatore', '2026-10-01');

-- -----------------------------------------------------------------------------
-- 3. Populate donations (Showing both eligible & cooldown historical events)
-- Note: Current reference date is November 2026.
-- Donations before August 15, 2026 are >= 90 days ago (ELIGIBLE).
-- Donations after August 15, 2026 are < 90 days ago (INELIGIBLE / COOLDOWN).
-- -----------------------------------------------------------------------------
INSERT INTO donations (donation_id, donor_id, blood_group, donation_date, units_donated, hemoglobin_level, phlebotomist_name, remarks) VALUES
(101, 1, 'O+', '2026-02-01', 1, 14.5, 'Dr. S. Ramesh', 'Normal whole blood collection'),
(102, 1, 'O+', '2026-06-15', 1, 14.2, 'Staff Nurse Geetha', 'Excellent donor response'),
(103, 2, 'A+', '2026-03-01', 1, 13.8, 'Dr. S. Ramesh', 'Routine donation camp'),
(104, 2, 'A+', '2026-07-10', 1, 14.0, 'Staff Nurse Priya', 'Fit for repeat donation'),
(105, 3, 'B+', '2026-03-15', 1, 12.8, 'Dr. R. Kavitha', 'Post-donation vitals normal'),
(106, 3, 'B+', '2026-07-28', 1, 13.0, 'Staff Nurse Geetha', 'College blood drive donation'),
(107, 4, 'O-', '2026-04-02', 1, 15.2, 'Dr. S. Ramesh', 'Universal donor emergency reserve'),
(108, 4, 'O-', '2026-10-25', 1, 15.0, 'Staff Nurse Geetha', 'Recent donation - Cooldown active'),
(109, 5, 'AB+', '2026-04-18', 1, 12.5, 'Dr. R. Kavitha', 'Routine voluntary donation'),
(110, 6, 'A-', '2026-05-02', 1, 14.1, 'Dr. S. Ramesh', 'Rare blood group collection'),
(111, 7, 'B-', '2026-05-15', 1, 13.2, 'Dr. R. Kavitha', 'Voluntary replacement donation'),
(112, 8, 'AB-', '2026-06-01', 1, 14.8, 'Dr. S. Ramesh', 'Rare negative phenotype unit'),
(113, 9, 'O+', '2026-06-12', 1, 13.6, 'Staff Nurse Priya', 'Corporate donation drive'),
(114, 9, 'O+', '2026-10-18', 1, 13.4, 'Staff Nurse Geetha', 'Recent donation - Cooldown active'),
(115, 10, 'A+', '2026-06-25', 1, 14.3, 'Dr. S. Ramesh', 'District camp collection'),
(116, 11, 'B+', '2026-07-08', 1, 12.9, 'Staff Nurse Geetha', 'Youth red cross camp donation'),
(117, 12, 'O-', '2026-07-18', 1, 14.6, 'Dr. S. Ramesh', 'Voluntary donor donation'),
(118, 13, 'A+', '2026-08-01', 1, 13.1, 'Staff Nurse Priya', 'Eligible (>90 days) donation'),
(119, 14, 'B+', '2026-08-20', 1, 14.0, 'Dr. R. Kavitha', 'Recent donation - Cooldown active'),
(120, 15, 'O+', '2026-09-05', 1, 13.5, 'Staff Nurse Geetha', 'Recent donation - Cooldown active'),
(121, 16, 'A-', '2026-09-22', 1, 14.4, 'Dr. S. Ramesh', 'Recent donation - Cooldown active'),
(122, 17, 'AB+', '2026-10-05', 1, 12.7, 'Staff Nurse Priya', 'Recent donation - Cooldown active'),
(123, 10, 'A+', '2026-10-20', 1, 14.2, 'Staff Nurse Geetha', 'Recent donation - Cooldown active'),
(124, 2, 'A+', '2026-11-02', 1, 13.9, 'Dr. S. Ramesh', 'Recent donation - Cooldown active'),
(125, 1, 'O+', '2026-11-08', 1, 14.4, 'Dr. S. Ramesh', 'Recent donation - Cooldown active');

-- -----------------------------------------------------------------------------
-- 4. Populate hospital_requests
-- -----------------------------------------------------------------------------
INSERT INTO hospital_requests (request_id, hospital_name, blood_group, units_requested, request_date, urgency_level, status, fulfillment_date, authorized_by) VALUES
(201, 'Government Headquarters Hospital, Erode', 'O+', 4, '2026-10-02', 'CRITICAL', 'FULFILLED', '2026-10-02', 'Dr. Mohanraj'),
(202, 'Apollo Speciality Hospital, Salem', 'A+', 3, '2026-10-10', 'URGENT', 'FULFILLED', '2026-10-10', 'Dr. Sundaram'),
(203, 'Kovai Medical Center and Hospital (KMCH)', 'B+', 5, '2026-10-18', 'NORMAL', 'FULFILLED', '2026-10-19', 'Dr. S. Ramesh'),
(204, 'Lotus Hospital, Erode', 'O-', 2, '2026-10-25', 'CRITICAL', 'FULFILLED', '2026-10-25', 'Dr. Mohanraj'),
(205, 'Ganga Medical Centre & Hospitals, CBE', 'A-', 2, '2026-11-01', 'URGENT', 'FULFILLED', '2026-11-01', 'Dr. Mohanraj'),
(206, 'Royal Care Super Speciality, Coimbatore', 'AB+', 2, '2026-11-04', 'NORMAL', 'FULFILLED', '2026-11-05', 'Dr. Sundaram'),
(207, 'Erode Trust Hospital, Erode', 'B-', 4, '2026-11-07', 'CRITICAL', 'PENDING', NULL, NULL),
(208, 'Sudha Hospitals, Erode', 'AB-', 3, '2026-11-09', 'URGENT', 'PENDING', NULL, NULL),
(209, 'Care 24 Hospital, Perundurai', 'O+', 6, '2026-11-11', 'CRITICAL', 'PENDING', NULL, NULL),
(210, 'Sri Ramakrishna Hospital, Coimbatore', 'A+', 2, '2026-11-12', 'NORMAL', 'PENDING', NULL, NULL),
(211, 'Manian Medical Centre, Erode', 'B+', 1, '2026-11-12', 'NORMAL', 'PENDING', NULL, NULL),
(212, 'Maruthi Hospital, Bhavani', 'O-', 8, '2026-11-06', 'CRITICAL', 'REJECTED', NULL, 'Dr. Mohanraj');

