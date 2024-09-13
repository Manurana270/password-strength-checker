# password-strength-checker
 # Introduction
The Password Generator and Strength Estimator is a user-friendly application designed to enhance password security through a graphical user interface (GUI) built with Python's Tkinter library. This application serves two primary functions: generating passwords and evaluating their strength. Users can generate passwords of varying complexity—easy, moderate, or hard—based on their personal information. Additionally, users can input their own passwords to receive a detailed assessment of their strength.

The strength estimation evaluates several factors including password length, complexity, entropy, and the avoidance of common patterns and predictable sequences. By analyzing these elements, the application provides immediate feedback on how secure a password is and offers recommendations for improvement. This tool not only assists users in creating robust passwords but also helps in assessing and enhancing the security of their existing passwords, making it a valuable resource for both personal and professional use

 # Methodology (Step-by-Step)
1. User Input Collection
Initial Setup: The GUI is initialized using Tkinter, creating a window with input fields for the user to enter personal information such as first name, last name, age, date of birth, and father's name.
User Choice: Users are given an option to either generate a new password or enter their own password for evaluation.
2. Password Generation (if chosen)
Character Extraction: Extract relevant characters from user-provided information, such as first name and last name.
Password Creation: Generate passwords based on predefined complexity levels:
Easy Passwords: Combine parts of the user’s name with random lower-case letters.
Moderate Passwords: Use a combination of uppercase letters, lowercase letters, special characters, and digits.
Hard Passwords: Incorporate a mix of uppercase and lowercase letters, digits, and special characters with shuffling to ensure randomness.
3. Password Strength Estimation (if user inputs their own password)
Common Password Check: Compare the password against a list of common passwords to identify if it is a widely used password.
Substitution Check: Replace characters with their commonly substituted counterparts and evaluate the presence of personal information.
Credential Check: Score the password based on its resemblance to user-provided information (e.g., name, last name, father's name).
Entropy Calculation: Compute the password's entropy to measure its unpredictability.
Pattern Check: Analyze the password for repetitive characters, sequential digits, and keyboard patterns.
Combination Attempts: Estimate the number of possible combinations and adjust the score accordingly.
4. Scoring and Feedback
Score Calculation: Aggregate scores from various checks to determine the overall strength of the password.
Feedback Display: Present the password's strength score and corresponding security rating (e.g., 'Easy', 'Moderate', 'Hard') in the GUI.
5. Output
Password List: Display the generated passwords or the strength evaluation of the entered password in a list format within the GUI.
Save/Review: Allow users to review the results and save the generated passwords if desired.
This methodology ensures that the application effectively guides users in creating strong passwords and provides a thorough assessment of their password security

# Results
The application effectively generates and evaluates passwords based on user input:

Password Generation:

Easy: Simple passwords combining parts of the user's name with random lowercase letters.
Moderate: Passwords with a mix of uppercase, lowercase letters, digits, and special characters.
Hard: Complex passwords incorporating a mix of character types and shuffled for increased randomness.
Password Strength Estimation:

Length and Complexity: Longer, diverse character passwords score higher.
Common Passwords: Matches with common passwords receive lower scores.
Credential Check: Passwords containing user information score lower.
Entropy and Patterns: Higher entropy and fewer patterns lead to better scores.
Combination Attempts: More possible combinations indicate stronger passwords.
The results provide clear insights into password security, helping users create and evaluate strong passwords.
<img width="743" alt="Screenshot 2023-07-20 143744" src="https://github.com/user-attachments/assets/9ff1b773-8de3-42f7-b1f9-fb57b6f3f693">

# Conclusion
The Password Generator and Strength Estimator application offers a robust solution for enhancing password security. By generating passwords with varying levels of complexity and assessing their strength based on multiple criteria, the application provides valuable insights into password security.

The tool effectively distinguishes between easy, moderate, and hard passwords, helping users understand the importance of password length, character variety, and unpredictability. It also identifies potential vulnerabilities by checking against common passwords and personal information.

Overall, the application is a practical and user-friendly resource for improving password security, making it easier for individuals to create strong, resilient passwords and protect their sensitive information.
