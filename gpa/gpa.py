import random
with open("generated.txt", "rb") as file:
        content = file.readlines()
        grade_points = {'A':5,'B':4, 'C':3, 'D':2, 'E':1}
        courses = {'MAT-111':None, 'CHM-112':None, 'PHY-111':None, 'ITE-111':None, 'ITE-112':None}
        grades = ['A', 'B', 'C', 'D', 'E', 'F']
        subjects = {'MAT-111':3, 'CHM-112':2, 'PHY-111':3, 'ITE-111':1, 'ITE-112':1}
        scores = [1, 2, 3]
        for name in content:
            name.upper()
            name = str(name)

            #name.rstrip('')
            # Create files for all name in the general names file
            with open(name, 'w') as f:
                f.write("Federal University of Technology\n")
                f.write(name.center(5) + '\n')
                f.write('='*len(content) + '\n')
                f.write('SUBJECT\t\t'.ljust(30))
                f.write('GRADES\t\t'.center(10))
                f.write('UNITS\t\t\n'.rjust(30) )
                f.write('='*len(content) + '\n')
                #generate random grades for the courses
                for course in courses:
                    courses[course] = random.choice(grades)
                    print(courses.items())

                #for units in subjects.values():
                    #units = str(units)
            #        scores = []
            #        scores += units
            #    for i in scores:
            #        print(i)
                    #unit_prt = random.choice(scores)
                    #print(unit_prt)

                for coursei, gradesi in courses.items():
                    calc_num = 0
                    if gradesi == 'A':
                        calc_num = 5
                    elif gradesi == 'B':
                        calc_num = 4
                    elif gradesi == 'C':
                        calc_num = 3
                    elif gradesi == 'D':
                        calc_num = 2
                    elif gradesi == 'E':
                        calc_num = 1
                    else :
                        calc_num = 0.5
                    unit_total = []
                    grade_total_list = []
                    f.write((coursei).ljust(20))
                    f.write(gradesi.center(40))
                    random_unit = str(random.choice(scores))
                    unit_total.append(int(random_unit))
                    grade_total = calc_num * int(random_unit)
                    grade_total_list.append(grade_total)
                    #subject = random.choice(subject)
                    f.write(random_unit.rjust(22) + '\n')
                gpa_var = sum(grade_total_list)
                gpa_var2 = sum(unit_total)
                gpa = gpa_var/gpa_var2
                f.write('G.P.A: ' + str(gpa))
                    #f.write(unit_used + '\n')
        #for first in names:
        #    last = []
        #    removed = first.pop()
        #    last.append(removed)
        #rint(first, last))

#courses = {'MAT-111':3, 'CHM-111':2, 'ITE-111':1}
#grade_points = {'A':, 'B':, 'C':, 'D':, 'E': }
