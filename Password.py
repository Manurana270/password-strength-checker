import re
import math
from tkinter import *
import dictionary
import random
import string
import csv
from dateutil.parser import parse
score = 0

# Password Generation


def generatePassword(row):
    chars = ''
    chars2 = ''
    name = row[0]

    chars2 = ''.join([char.lower() for char in name if char.isalpha()])[:3]
    for value in row:
        if isinstance(value, str):
            chars += ''.join(list(value.replace(' ', '').strip()))

    easyPass = []
    moderatePass = []
    hardPass = []

    # Generate easy password
    for i in range(random.randint(1, 4)):
        lower_char1 = random.choice([char for char in chars if char.islower()])
        lower_char2 = random.choice([char for char in chars if char.islower()])
        password = chars2 + lower_char1 + lower_char2
        easyPass.append(password)

    # Generate moderate password
    for _ in range(random.randint(1, 3)):
        password = chars2.upper() + random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.punctuation) + str(random.randint(0, 9))
        moderatePass.append(password)

    # Generate hard password
    for i in range(random.randint(1, 2)):
        upper_chars = ''.join([char for char in chars if char.isupper()])
        lower_chars = ''.join([char for char in chars if char.islower()])
        digits = ''.join([char for char in chars if char.isdigit()])
        punctuation = ''.join(
            [char for char in chars if char in string.punctuation])
        password_list = []
        if len(upper_chars) >= 2:
            password_list += random.sample(upper_chars, 2)
        else:
            password_list += random.sample(string.ascii_uppercase, 2)
        if len(lower_chars) >= 2:
            password_list += random.sample(lower_chars, 2)
        else:
            password_list += random.sample(string.ascii_lowercase, 2)
        if len(digits) >= 2:
            password_list += random.sample(digits, 2)
        else:
            password_list += random.sample(string.digits, 2)
        if len(punctuation) >= 2:
            password_list += random.sample(punctuation, 2)
        else:
            password_list += random.sample(string.punctuation, 2)
        random.shuffle(password_list)
        hardPass.append(''.join(password_list))

    passwords_gen = []
    for i in easyPass:
        passwords_gen.append(i)
    for j in moderatePass:
        passwords_gen.append(j)
    for k in hardPass:
        passwords_gen.append(k)
    return passwords_gen


with open('comman_passwords.txt', 'r') as cp:
    common_passwords = cp.read().splitlines()


# Strength Estimation
def check_commanpass(password):
    with open("comman_passwords.txt", "r") as f:
        rd = f.read().splitlines()
        for i in range(len(rd)):
            if rd[i] in password:
                return 0
            else:
                continue
        return 1


def substitute(password):
    substitutions = {'0': ['o'], '1': ['i', 'l'], '3': ['e'], '4': [
        'a'], '5': ['s'], '7': ['t'], '8': ['b'], '9': ['g', 'q']}
    for sub, chars in substitutions.items():
        for char in chars:
            password = password.replace(char, sub)
    return password


def check_cred(password, name, last, father):
    str1 = substitute(password)
    aux_score = 0
    pattern1 = r'\b{}\b'.format(re.escape(name.lower()))
    match1 = re.search(pattern1, str1)
    if (match1):
        aux_score -= 2
    else:
        aux_score += 2
    pattern2 = r'\b{}\b'.format(re.escape(last.lower()))
    match2 = re.search(pattern2, str1)
    if (match2):
        aux_score -= 2
    else:
        aux_score += 2
    pattern3 = r'\b{}\b'.format(re.escape(father.lower()))
    match3 = re.search(pattern3, str1)
    if (match3):
        aux_score -= 2
    else:
        aux_score += 2
    date_patterns = [
        # dd/mm/yyyy or dd-mm-yyyy or dd.mm.yyyy
        r'\b(0?[1-9]|[12][0-9]|3[01])[./-](0?[1-9]|1[012])[./-]\d{4}\b',
        # yyyy/mm/dd or yyyy-mm-dd or yyyy.mm.dd
        r'\b\d{4}[./-](0?[1-9]|1[012])[./-](0?[1-9]|[12][0-9]|3[01])\b',
        # mm/dd/yyyy or mm-dd-yyyy or mm.dd.yyyy
        r'\b(0?[1-9]|1[012])[./-](0?[1-9]|[12][0-9]|3[01])[./-]\d{4}\b',
        # ddmmyy or ddmmyy
        r'\b(0?[1-9]|[12][0-9]|3[01])(0?[1-9]|1[012])\d{2}\b',
        r'\b\d{2}(0?[1-9]|1[012])(0?[1-9]|[12][0-9]|3[01])\b',  # yymmdd
    ]
    date_regex = '|'.join(date_patterns)
    match4 = re.search(date_regex, str1)
    if match4:
        aux_score -= 1
    else:
        aux_score += 1
    pattern4 = r'(.)\1{2,}'  # Repeated characters
    pattern5 = '0123456789'  # Sequential digits
    pattern6 = 'qwertyuiopasdfghjklzxcvbnm'  # Keyboard patterns
    if re.search(pattern4, str1):
        aux_score -= 2
    for i in range(len(pattern5)):
        for k in range(i, len(pattern5)):
            str = pattern5[i:k+1]
            if (len(str) > 1) and str in password:
                aux_score = 0
            else:
                continue
    for i in range(len(pattern6)):
        for k in range(i, len(pattern6)):
            str = pattern6[i:k+1]
            if (len(str) > 1) and str in password:
                aux_score = 0
            else:
                continue
    return aux_score


def check_ent(password):
    ent = 0
    N = len(password)
    char_set = set(password)
    L = len(char_set)
    ent = (L*(math.log(N)))/math.log(2)
    if (round(ent) > 80):
        return 5
    else:
        return -3


def check_relation(password):
    aux_score = 0
    charset_size = 94
    if (len(password) >= 8):
        aux_score += 4
        for i in range(len(password)-1):
            if (not (password[i].isalnum()) and not (password[i+1].isalnum())):
                aux_score -= 1
            else:
                aux_score += 2
    else:
        aux_score -= 2
        for i in range(len(password)-1):
            if (not (password[i].isalnum()) and not (password[i+1].isalnum())):
                aux_score -= 2
            else:
                aux_score += 2
    password_len = len(password)
    if password_len > 0:
        char_freq = {}
        for c in password:
            if c in char_freq:
                char_freq[c] += 1
            else:
                char_freq[c] = 1
        entropy = 0
        for c in char_freq:
            p = char_freq[c] / password_len
            entropy += - p * math.log(p, 2)
        possible_combinations = charset_size ** password_len
        aux_score += entropy * math.log(possible_combinations, 2)
    if aux_score >= 98:
        return 3
    elif aux_score >= 94 and aux_score < 98:
        return 1
    else:
        return -1


def check_attempts(password):
    # character set size based on contents of password
    if password.isalnum():
        L = 62
        aux_score = -2
    elif not password.isalnum():
        L = 94
        aux_score = 2
    N = len(password)  # password length
    aux_score += check_relation(password)
    attempts = L ** N
    if attempts < 10**6:
        aux_score += 1
    elif attempts < 10**12:
        aux_score += 2
    elif attempts < 10**18:
        aux_score += 3
    else:
        aux_score += 4
    return aux_score


def password_est(name, last, age, dob, father, password):
    score = 0
    if (len(password) >= 8):
        score += 2
    else:
        for i in range(len(password)-1):
            if (not (password[i].isalnum()) and not (password[i+1].isalnum())):
                score += 0
        else:
            score += 1
    if password.isalnum():
        score -= 2
    else:
        score += 4
    aux_score = check_commanpass(password)
    if (aux_score == 0):
        score -= 5
    else:
        score += 3
    aux_score = check_cred(password, name, last, father)
    if aux_score == 0:
        aux_score -= 5
    score += aux_score
    score += check_ent(password)
    score += check_attempts(password)
    score += check_relation(password)

    if score < 0:
        return f"{score}  'Bad'"
    elif score >= 0 and score <= 9:
        return f"{score}  Easy"
    elif score >= 10 and score <= 18:
        return f"{score}  'Moderate'"
    else:
        return f"{score}  'Hard'"


def submit():
    # Get the input values from the entry fields
    name = name_entry.get()
    last = last_entry.get()
    age = int(age_entry.get())
    date_str = dob_entry.get()
    dob = parse(date_str).date()
    father = father_entry.get()
    choice = password_choice.get()

    # Generate or estimate the password based on the user's choice
    if choice == 'Y':
        def check_strength():
            password_list = Listbox(window, width=100, height=100)
            password_list.pack()
            password_list.delete(0, END)
            password = password_entry.get()
            score = password_est(name, last, age, dob, father, password)
            password_list.insert(
                END, f"Password:- {password}    Score:- {score}")

        password_label = Label(window, text="Password:")
        password_label.pack()
        password_entry = Entry(window, show="*")
        password_entry.pack()

        Estimation = Button(
            window, text="Check Strength", command=check_strength)
        Estimation.pack()
    else:
        passwords = generatePassword([name, last, age, dob, father])
        password_list_label = Label(window, text="Generated Passwords:")
        password_list_label.pack()

        password_list = Listbox(window, width=100, height=100)
        password_list.pack()

        password_list.delete(0, END)
        for password in passwords:
            score = password_est(name, last, age, dob, father, password)
            password_list.insert(
                END, f"Password:- {password}    Score:- {score}")


# Create the main window
window = Tk()
window.title("Password Generator")
window.geometry("400x400")

# Create the input fields
name_label = Label(window, text="First Name:")
name_label.pack()
name_entry = Entry(window)
name_entry.pack()

last_label = Label(window, text="Last Name:")
last_label.pack()
last_entry = Entry(window)
last_entry.pack()

age_label = Label(window, text="Age:")
age_label.pack()
age_entry = Entry(window)
age_entry.pack()

dob_label = Label(window, text="Date of Birth:")
dob_label.pack()
dob_entry = Entry(window)
dob_entry.pack()

father_label = Label(window, text="Father's Name:")
father_label.pack()
father_entry = Entry(window)
father_entry.pack()

password_choice = StringVar()
password_choice.set("N")

choice_label = Label(window, text="Do you want to enter your own password?")
choice_label.pack()

yes_button = Radiobutton(
    window, text="Yes", variable=password_choice, value="Y")
yes_button.pack()

no_button = Radiobutton(window, text="No", variable=password_choice, value="N")
no_button.pack()

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack()

window.mainloop()
