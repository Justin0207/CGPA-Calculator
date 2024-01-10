# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 13:34:15 2024

@author: HP
"""



class GpaCalculator:
    '''
    The GpaCalculator is used to calculate the GPA and CGPA of a student.
    
    It follows the grading principles from the faculty of engineering in the University of Benin. 
    
    For each student, the GPA of a student in the first year only makes up 10% of the total CGPA.
    
    The table below represents the respective GPA weight for each year.
    
    First year (100 level) ------------- 10%
    Second year (200 level) ------------ 15%
    Third year (300 level) ------------- 20%
    Fourth year (400 level) ------------ 25%
    Fifth year (500 level) ------------- 30%
    
    Each grade has a respective number of points. 
    
    GRADE                           POINTS
      A                               5
      B                               4
      C                               3
      D                               2
      E                               1
    ................................
    
    Attributes
    ----------
    
    max_gpa(5.0):
        The maximum GPA a student can have per session
    
    weight_100 (0.10):
        The weight or contribution of the first year GPA to the student's final CGPA
    weight_200 (0.15):
        The weight or contribution of the second year GPA to the student's final CGPA
    weight_300 (0.20):
        The weight or contribution of the third year GPA to the student's final CGPA
    weight_400 (0.25):
        The weight or contribution of the fourth year GPA to the student's final CGPA
    weight_500 (0.30):
        The weight or contribution of the fifth year GPA to the student's final CGPA
        
    ..................................................................................................
    
    gpa_100: float
        A student first year GPA. It is initialized with zero
    credit_load_100: list
        A list containing a student's credit load for each courses done in the first year. 
    score_100 : list
        A list containing the scores or points for each grade a student gets in the second year
    gpa_200: float
        A student second year GPA
    credit_load_200: list
        A list containing a student's credit load for each courses done in the second year
    score_200 : list
        A list containing the scores or points for each grade a student gets in the second year
    gpa_300: float
        A student third year GPA
    credit_load_300: list
        A list containing a student's credit load for each courses done in the third year
    score_300 : list
        A list containing the scores or points for each grade a student gets in the third year
    gpa_400: float
        A student fourth year GPA
    credit_load_400: list
        A list containing a student's credit load for each courses done in the fourth year
    score_400 : list
        A list containing the scores or points for each grade a student gets in the fourth year
    gpa_500: float
        A student fifth year GPA
    credit_load_500: list
        A list containing a student's credit load for each courses done in the fifth year
    score_500 : list
        A list containing the scores or points for each grade a student gets in the fifth year
    courses_100 : list
        A list containing the courses offered by a student in the first year
    courses_200 : list
        A list containing the courses offered by a student in the second year
    courses_300 : list
        A list containing the courses offered by a student in the third year
    courses_400 : list
        A list containing the courses offered by a student in the fourth year
    courses_500 : list
        A list containing the courses offered by a student in the fifth year
    _frac_gpa_100 : float
        Represents the fraction of a student's first year GPA to the final CGPA
    _frac_gpa_200 : float
        Represents the fraction of a student's second year GPA to the final CGPA
    _frac_gpa_300 : float
        Represents the fraction of a student's third year GPA to the final CGPA
    _frac_gpa_400 : float
        Represents the fraction of a student's fourth year GPA to the final CGPA
    _frac_gpa_500 : float
        Represents the fraction of a student's fifth year GPA to the final CGPA
    credits : list
        Repesents the credit load of all courses from year 1 to final year
    grades : list
        Repesents the grades a student has in all his courses from year 1 to final year
    courses : list
        Repesents the courses a student offered from year 1 to final year
    grades_100 : list
        Represents the grade of a student a student has in the first year courses
    grades_200 : list
        Represents the grade of a student a student has in the second year courses
    grades_300 : list
        Represents the grade of a student a student has in the third year courses
    grades_400 : list
        Represents the grade of a student a student has in the fourth year courses
    grades_500 : list
        Represents the grade of a student a student has in the fifth courses
        
    '''
    import pandas as pd
    max_gpa = 5.0          # max_gpa represents the maximum gpa a student can have
    weight_100 = 0.10        # w 
    weight_200 = 0.15
    weight_300 = 0.20
    weight_400 = 0.25
    weight_500 = 0.30
    
    
    def __init__(self):
        self.gpa_100 = 0.0
        self.credit_load_100 = [ ]
        self.score_100 = [ ]
        self.gpa_200 = 0.0
        self.credit_load_200 = [ ]
        self.score_200 = [ ]
        self.gpa_300 = 0.0
        self.credit_load_300 = [ ]
        self.score_300 = [ ]
        self.gpa_400 = 0.0
        self.credit_load_400 = [ ]
        self.score_400 = [ ]
        self.gpa_500 = 0.0
        self.credit_load_500 = [ ]
        self.score_500 = [ ]
        self.courses_100 = [ ]
        self.courses_200 = [ ]
        self.courses_300 = [ ]
        self.courses_400 = [ ]
        self.courses_500 = [ ]
        self._frac_gpa_100 = 0.0
        self._frac_gpa_200 = 0.0
        self._frac_gpa_300 = 0.0
        self._frac_gpa_400 = 0.0
        self._frac_gpa_500 = 0.0
        self.credits = [ ]
        self.grades =[ ]
        self.courses = [ ]
        self.grades_100 = [ ]
        self.grades_200 = [ ]
        self.grades_300 = [ ]
        self.grades_400 = [ ]
        self.grades_500 = [ ]
        
    def add_courses(self, courses, credit_load, grade, level):
        '''
        It id used to input the courses offered by a student

        Parameters
        ----------
        courses : str
            The course offered by a student
        credit_load : int
            The credit load for each course taken
        grade : str
            The grade a student had in the course
        level : int
            The level or year of the student. 100 level represents first year, 200 represents second year and so on

        Returns
        -------
        None.

        '''
        if level == 100:
            self.courses_100.append(courses)
            self.grades_100.append(grade)
            self.credit_load_100.append(credit_load)
            if grade.lower() == 'a':
                self.score_100.append(5)
            elif grade.lower() == 'b':
                self.score_100.append(4)
            elif grade.lower() == 'c':
                self.score_100.append(3)
            elif grade.lower() == 'd':
                self.score_100.append(2)
            elif grade.lower() == 'e':
                self.score_100.append(1)
            else:
                self.score_100.append(0)
                
        if level == 200:
            self.courses_200.append(courses)
            self.grades_200.append(grade)
            self.credit_load_200.append(credit_load)
            if grade.lower() == 'a':
                self.score_200.append(5)
            elif grade.lower() == 'b':
                self.score_200.append(4)
            elif grade.lower() == 'c':
                self.score_200.append(3)
            elif grade.lower() == 'd':
                self.score_200.append(2)
            elif grade.lower() == 'e':
                self.score_200.append(1)
            else:
                self.score_200.append(0)
                
        if level == 300:
            self.courses_300.append(courses)
            self.grades_300.append(grade)
            self.credit_load_300.append(credit_load)
            if grade.lower() == 'a':
                self.score_300.append(5)
            elif grade.lower() == 'b':
                self.score_300.append(4)
            elif grade.lower() == 'c':
                self.score_300.append(3)
            elif grade.lower() == 'd':
                self.score_300.append(2)
            elif grade.lower() == 'e':
                self.score_300.append(1)
            else:
                self.score_300.append(0)
                
        if level == 400:
            self.courses_400.append(courses)
            self.grades_400.append(grade)
            self.credit_load_400.append(credit_load)
            if grade.lower() == 'a':
                self.score_400.append(5)
            elif grade.lower() == 'b':
                self.score_400.append(4)
            elif grade.lower() == 'c':
                self.score_400.append(3)
            elif grade.lower() == 'd':
                self.score_400.append(2)
            elif grade.lower() == 'e':
                self.score_400.append(1)
            else:
                self.score_400.append(0)
                
        if level == 500:
            self.courses_500.append(courses)
            self.grades_500.append(grade)
            self.credit_load_500.append(credit_load)
            if grade.lower() == 'a':
                self.score_500.append(5)
            elif grade.lower() == 'b':
                self.score_500.append(4)
            elif grade.lower() == 'c':
                self.score_500.append(3)
            elif grade.lower() == 'd':
                self.score_500.append(2)
            elif grade.lower() == 'e':
                self.score_500.append(1)
            else:
                self.score_500.append(0)
                
                
    def calculate_GPA(self, level=100):
        '''
        It calculates the GPA of a student

        Parameters
        ----------
        level : int, optional
            The level of the student. The default is 100.

        Returns
        -------
        None.

        '''
        if level == 100:
            score_100 = [ ]
            for i, j in enumerate(range(len(self.credit_load_100))):
                score_100.append(self.credit_load_100[i] * self.score_100[j])
            credit = sum(self.credit_load_100)
            score = sum(score_100)
            self.gpa_100 = score / credit
            self._frac_gpa_100 = self.gpa_100 * GpaCalculator.weight_100
            print("GPA for 100 level is: ", round(self.gpa_100, 2))
        
        elif level == 200:
            score_200 = [ ]
            for i, j in enumerate(range(len(self.credit_load_200))):
                score_200.append(self.credit_load_200[i] * self.score_200[j])
            credit = sum(self.credit_load_200)
            score = sum(score_200)
            self.gpa_200 = score/credit
            self._frac_gpa_200 = self.gpa_200  * GpaCalculator.weight_200
            print("GPA for 200 level is: ", round(self.gpa_200, 2))
            
        elif level == 300:
            score_300 = [ ]
            for i, j in enumerate(range(len(self.credit_load_300))):
                score_300.append(self.credit_load_300[i] * self.score_300[j])
            credit = sum(self.credit_load_300)
            score = sum(score_300)
            self.gpa_300 = score/credit
            self._frac_gpa_300 = self.gpa_300 * GpaCalculator.weight_300
            print("GPA for 300 level is: ", round(self.gpa_300, 2))
        
        elif level == 400:
            score_400 = [ ]
            for i, j in enumerate(range(len(self.credit_load_400))):
                score_400.append(self.credit_load_400[i] * self.score_400[j])
            credit = sum(self.credit_load_400)
            score = sum(score_400)
            self.gpa_400 = score/credit
            self._frac_gpa_400 = self.gpa_400 * GpaCalculator.weight_400
            print("GPA for 400 level is: ", round(self.gpa_400, 2))
            
        else:
            score_500 = [ ]
            for i, j in enumerate(range(len(self.credit_load_500))):
                score_500.append(self.credit_load_500[i] * self.score_500[j])
            credit = sum(self.credit_load_500)
            score = sum(score_500)
            self.gpa_500 = score/credit
            self._frac_gpa_500 = self.gpa_500 * GpaCalculator.weight_500
            print("GPA for 500 level is: ", round(self.gpa_500, 2))
            
            
    def calculate_CGPA(self, upto=500):
        '''
        It calculates the CGPA or cumulative GPA of a student

        Parameters
        ----------
        upto : int, optional
            The level of the student. The default is 500.

        Returns
        -------
        None.

        '''
        if upto == 100:
            cgpa = self.gpa_100
            print('CGPA for {} level is : {}'.format(upto, cgpa))
        elif upto == 200:
            total_frac_gpa= self._frac_gpa_100 + self._frac_gpa_200
            max_cgpa = (GpaCalculator.weight_100 + GpaCalculator.weight_200) * GpaCalculator.max_gpa
            cgpa = (total_frac_gpa/max_cgpa)* GpaCalculator.max_gpa
            print('CGPA for {} level is : {}'.format(upto, cgpa))
        elif upto == 300:
            total_frac_gpa= self._frac_gpa_100 + self._frac_gpa_200 + self._frac_gpa_300
            max_cgpa = (GpaCalculator.weight_100 + GpaCalculator.weight_200 + GpaCalculator.weight_300) * GpaCalculator.max_gpa
            cgpa = (total_frac_gpa/max_cgpa)* GpaCalculator.max_gpa
            print('CGPA for {} level is : {}'.format(upto, cgpa))
        elif upto == 400:
            total_frac_gpa= self._frac_gpa_100 + self._frac_gpa_200 + self._frac_gpa_300 + self._frac_gpa_400
            max_cgpa = (GpaCalculator.weight_100 + GpaCalculator.weight_200 + GpaCalculator.weight_300 + GpaCalculator.weight_400) * GpaCalculator.max_gpa
            cgpa = (total_frac_gpa/max_cgpa)* GpaCalculator.max_gpa
            print('CGPA for {} level is : {}'.format(upto, cgpa))
        else:
            cgpa = self._frac_gpa_100 + self._frac_gpa_200 + self._frac_gpa_300 + self._frac_gpa_400 + self._frac_gpa_500
            print('CGPA for {} level is : {}'.format(upto, cgpa))
        
    
    
    def get_transcript(self):
        '''
        It generates a Dataframe of the courses, grades and credit load of the courses the student offers.

        Returns
        -------
        df : TYPE
            DESCRIPTION.

        '''
        self.credits = self.credit_load_100 + self.credit_load_200 + self.credit_load_300\
                     + self.credit_load_400 + self.credit_load_500
        self.courses = self.courses_100 +self.courses_200 + self.courses_300 + self.courses_400\
                     + self.courses_500
        self.grades = self.grades_100 +self.grades_200 + self.grades_300 + self.grades_400\
                    + self.grades_500
        df = pd.DataFrame(columns = ['Courses Offered', 'Credit Load', 'Grades'])
        df['Courses Offered'] = self.courses
        df['Credit Load'] = self.credits
        df['Grades'] = self.grades
        return df    
            
            
            
            
            
            
calc = GpaCalculator()
calc.add_courses('mth110',3, "A", 100)
calc.add_courses('mth112',3, "A", 100)
calc.add_courses('gst110',2, "A", 100)
calc.add_courses('gst112',2, "A", 100)
calc.add_courses('phy111',3, "A", 100)
calc.add_courses('phy113',3, "A", 100)
calc.add_courses('chm111',3, "A", 100)
calc.add_courses('chm113',3, "A", 100)
calc.add_courses('mth122',3, "A", 100)
calc.add_courses('mth123',3, "A", 100)
calc.add_courses('phy124',4, "B", 100)
calc.add_courses('gst122',2, "B", 100)
calc.add_courses('chm122',3, "A", 100)
calc.add_courses('chm124',3, "A", 100)
calc.add_courses('gst123',2, "A", 100)
calc.add_courses('gst121',2, "C", 100)
calc.add_courses('phy109',2, "B", 100)
calc.add_courses('ema281',2, "B", 200)
calc.add_courses('mee211',3, "E", 200)
calc.add_courses('mee212',3, "C", 200)
calc.add_courses('ens211',2, "A", 200)
calc.add_courses('pre211',2, "A", 200)
calc.add_courses('eee211',3, "B", 200)
calc.add_courses('cve211',3, "A", 200)
calc.add_courses('ela201',2, "A", 200)
calc.add_courses('ecp281',2, "A", 200)
calc.add_courses('ema282',4, "A", 200)
calc.add_courses('che222',3, "A", 200)
calc.add_courses('mee221',3, "B", 200)
calc.add_courses('mee222',3, "B", 200)
calc.add_courses('eee212',3, "A", 200)
calc.add_courses('pre212',2, "A", 200)
calc.add_courses('ela202',2, "A", 200)
calc.add_courses('cpe272',2, "C", 200)
#calc.calculate_GPA(400)
calc.calculate_GPA(100)
#calc.calculate_GPA(300)
calc.calculate_GPA(200)
#calc.calculate_GPA(500)
calc.calculate_CGPA(200)
calc.get_transcript()

