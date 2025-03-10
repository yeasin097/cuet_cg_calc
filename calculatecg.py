result = open("result.txt", "r")


grade_conversion = {
    "A+": 4.00,
    "A": 3.75,
    "A-": 3.50,
    "B+": 3.25,
    "B": 3.00,
    "B-": 2.75,
    "C+": 2.50,
    "C": 2.25,
    "D": 2.00,
    "F": 0,
}

term_wise_credit_and_grade = {
    "11": 0,
    "12": 0,
    "21": 0,
    "22": 0,
    "31": 0,
    "32": 0,
    "41": 0,
    "42": 0,
}

term_wise_credit = {
    "11": 0,
    "12": 0,
    "21": 0,
    "22": 0,
    "31": 0,
    "32": 0,
    "41": 0,
    "42": 0,
}



count = 0
sum_of_credit_and_grade = 0
sum_of_credit = 0

for line in result:
    words = line.split()
    credit = float ((words[1]))
    grade = grade_conversion[words[8]]
    if(grade==0):
        continue

    level_term = int(words[3]) * 10 + int(words[6])

    sum_of_credit_and_grade = sum_of_credit_and_grade + (credit*grade)
    sum_of_credit = sum_of_credit + credit

    term_wise_credit_and_grade[str(level_term)] = term_wise_credit_and_grade[str(level_term)] + (credit*grade)
    term_wise_credit[str(level_term)] = term_wise_credit[str(level_term)] + credit
    
    count = count + 1


print("Term wise CGPA")
for term in term_wise_credit:
    print("Level:",int(int(term)/10)," Term:",int(term)%10,end=" CGPA: ")
    if(int(term_wise_credit[term]) != 0):
        print(round(term_wise_credit_and_grade[term]/term_wise_credit[term],2))
    else:
        print(0.00)


print("Total ", count, "Subjects Calculated, Avergae CGPA = ", round(sum_of_credit_and_grade/sum_of_credit,2))
        
