import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv('enrollment.csv')
#print(df.describe())
# print(df.head())

#DATA EXPLORATION

spring_Semester_enroll=df[df['Semester']=='Spring'][['Semester','Prof','Grad','Ungrad','Post-Doc' ,'Year']]
#print(spring_Semester_enroll)

avg_spring_prof_enroll=df[df['Semester']=='Spring']['Prof'].mean()
print(avg_spring_prof_enroll)

avg_spring_grad_enroll=df[df['Semester']=='Spring']['Grad'].mean()
print(avg_spring_grad_enroll)

avg_spring_ungrad_enroll=df[df['Semester']=='Spring']['Ungrad'].mean()
print(avg_spring_ungrad_enroll)

avg_spring_post_Doc_enroll=df[df['Semester']=='Spring']['Post-Doc'].mean()
print(avg_spring_post_Doc_enroll)


#DATA VISUALISATION

plt.barh(df['Semester'],df['Total'])
plt.show()


#MARITAL STATUS
    # plt.bar(avg_income_by_marital_status['Marital_Status'], avg_income_by_marital_status['Income'], color='skyblue')
    # plt.title('Average Income by Marital Status')
    # plt.xlabel('Marital Status')
    # plt.ylabel('Average Income')

