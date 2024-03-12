# -*- coding: utf-8 -*-
'''
Created on Mon Mar 11 11:41:11 2024

@author: HP
'''

import streamlit as st
import numpy as np





# Loading the saved models

# sidebar for navigation



grade_to_point = {
'A': 5,
'B': 4,
'C': 3,
'D': 2,
'E': 1,
'F': 0,
}
grades = list(grade_to_point.keys())


def calculate_gpa(
    grade: np.array,
    credit: np.array,
    previous_cgpa = 0.00,
    previous_credit = 0,
):
    # grade = np.array([grade_to_point[g] for g in grade])
    total_credit = credit.sum() 
    total_grade = (grade * credit).sum() #+ previous_cgpa * previous_credit
    return round(total_grade / total_credit, 2)

def gpa_division(cgpa):
    if cgpa >= 4.5:
        division = 'First Class'
        st.success('CGPA Division: {}'.format(division), icon='✅')
        st.balloons()
    elif cgpa >= 3.5 and cgpa <4.5:
        division = 'Second Class Upper'
        st.success('CGPA Division: {}'.format(division), icon='✅')
        st.snow()
    elif cgpa >= 2.4 and cgpa < 3.5:
        division = 'Second Class Lower'
        st.warning('CGPA Division: {}'.format(division), icon='⚠️')
    else:
        division = 'Third Class'
        st.error('CGPA Division: {}'.format(division), icon='🚨')
        


st.title('CGPA Calculator')



number_of_subjects = st.number_input('Number of Courses offered',
    min_value = 1,
    max_value = 100,
    value = 5,
)

ans = st.selectbox('Do you wish to calculate your CGPA? : ', options = ['No', 'Yes'])
if ans == 'Yes':

    level = st.selectbox('Level  : ', options = ['100 Level', '200 Level', '300 Level', '400 Level', '500 Level'])
    if level == '200 Level':
        cols = st.columns(2)
        gpa_100 = cols[0].number_input(
            label ='100 Level GPA',
            help = 'Enter Your CGPA up to the previous semester',
            min_value = 0.00,
            value = 0.00,
            step = 0.01,
            key = '2gpa_100'
        )
        
    ############################################################################################################
    elif  level == '300 Level':
        cols = st.columns(2)
        gpa_100 = cols[0].number_input(
            label = '100 Level GPA',
            help = 'Enter Your CGPA up to the previous semester',
            min_value = 0.00,
            value = 0.00,
            step = 0.01,
            key = '3gpa_100'
        )
    

        gpa_200 = cols[1].number_input(
        label = '200 Level GPA',
        help = 'Enter Your CGPA up to the previous semester',
        min_value = 0.00,
        value = 0.00,
        step = 0.01,
        key = '3_gpa_200'
        )
    
    ##########################################################################################
       
    
    elif  level == '400 Level':
        cols = st.columns(3)
        gpa_100 = cols[0].number_input(
            label = '100 Level GPA',
            help = 'Enter Your CGPA up to the previous semester',
            min_value = 0.00,
            value = 0.00,
            step = 0.01,
            key = '4gpa_100'
        )
    

        gpa_200 = cols[1].number_input(
        label = '200 Level GPA',
        help = 'Enter Your CGPA up to the previous semester',
        min_value = 0.00,
        value = 0.00,
        step = 0.01,
        key = '4_gpa_200'
        )

        
        gpa_300 = cols[2].number_input(
            label = '300 Level CGPA',
            help = 'Enter Your CGPA up to the previous semester',
            min_value = 0.00,
            value = 0.00,
            step = 0.01,
            key = '4_gpa_300'
        )
        
        
    ########################################################################################
    
    elif case == '500 Level':
        cols = st.columns(4)
        gpa_100 = cols[0].number_input(
            label = '100 Level GPA',
            help = 'Enter Your CGPA up to the previous semester',
            min_value = 0.00,
            value = 0.00,
            step = 0.01,
            key = '5gpa_100'
        )
        
    
        gpa_200 = cols[1].number_input(
        label = '200 Level GPA',
        help = 'Enter Your CGPA up to the previous semester',
        min_value = 0.00,
        value = 0.00,
        step = 0.01,
        key = '5_gpa_200'
        )
        gpa_300 = cols[2].number_input(
            label = '300 Level CGPA',
            help = 'Enter Your CGPA up to the previous semester',
            min_value = 0.00,
            value = 0.00,
            step = 0.01,
            key = '5_gpa_300'
        )
        
        gpa_400 = cols[3].number_input(
            label = '400 Level CGPA',
            help = 'Enter Your CGPA up to the previous semester',
            min_value = 0.00,
            value = 0.00,
            step = 0.01,
            key = '5_gpa_400'
        )
    
grade = np.array([0] * number_of_subjects)
credit = np.array([0] * number_of_subjects)
for i in range(number_of_subjects):
    st.subheader(f'Course #{i+1}')
    cols = st.columns(2)
    grade[i] = grade_to_point[
        cols[0].selectbox(
            label = 'Grade',
            options = grades,
            key = f'grades{i}',
        )
    ]

    credit[i] = cols[1].number_input(
        label='Credit',
        min_value = 1,
        max_value = 6,
        value = 3,
        step = 1,
        key = f'credits{i}',
    )

present_gpa = calculate_gpa(grade, credit)

if st.button('Calculate'):
    st.info('Your semester GPA : {}' .format(present_gpa))
    if ans == 'Yes':
        if level == '100 Level':
            cgpa = present_gpa
            st.success('Your current CGPA : {}' .format(cgpa))
            gpa_division(cgpa)
        
        elif level == '200 Level':
            ur_cgpa = (0.1 * gpa_100) + (0.15 * present_gpa)
            expected_cgpa = 0.5 + 0.75
            cgpa = round(((ur_cgpa / expected_cgpa) * 5), 2)
            st.success('Your current CGPA : {}' .format(cgpa))
            gpa_division(cgpa)
        
        elif level == '300 Level':
            ur_cgpa = (0.1 * gpa_100) + (0.15 * gpa_200) + (0.2 * present_gpa)
            expected_cgpa = 0.5 + 0.75 + 1
            cgpa = round(((ur_cgpa / expected_cgpa) * 5), 2)
            st.success('Your current CGPA : {}' .format(cgpa))
            gpa_division(cgpa)
        
        elif level == '400 Level':
            ur_cgpa = (0.1 * gpa_100) + (0.15 * gpa_200) + (0.2 * gpa_300) +(0.25 * present_gpa)
            expected_cgpa = 0.5 + 0.75 + 1 + 1.25
            cgpa = round(((ur_cgpa / expected_cgpa) * 5), 2)
            st.success('Your current CGPA : {}' .format(cgpa))
            gpa_division(cgpa)
        
        elif level == '500 Level':
            ur_cgpa = (0.1 * gpa_100) + (0.15 * gpa_200) + (0.2 * gpa_300) +(0.25 * gpa_400) + (0.3 * present_gpa)
            expected_cgpa = 0.5 + 0.75 + 1 + 1.25 + 1.5
            cgpa = round(((ur_cgpa / expected_cgpa) * 5), 2)
            st.success('Your current CGPA : {}' .format(cgpa))
            gpa_division(cgpa)
                
                
                
                
st.markdown("Made with ❤️ by [Anyanwu Justice](https://github.com/Justin0207)")
st.write(
    """
    <style>
        footer {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
        


    
