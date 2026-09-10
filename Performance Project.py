import pandas as pd

df = pd.read_csv("C:\\Users\\Mohamed Ashraf\\OneDrive\\Desktop\\Data analysis\\Projects\\Student Performance Project\\student_performance_dataset.csv")

df
df.info()
df.describe()
print(df.isnull().sum())


df['parental_education']=df['parental_education'].fillna('unknown')
print(df.isnull().sum())


avg_final_exam_score = df['final_exam_score'].mean()
print(avg_final_exam_score)


max_final_exam_score = df['final_exam_score'].max()
print(max_final_exam_score)


min_final_exam_score = df['final_exam_score'].min()
print(min_final_exam_score)


df['final_grade'] = df['final_exam_score'].apply(lambda x: 'A' if x >= 90 else ('B' if x >= 80 else ('C' if x >= 70 else ('D' if x >= 60 else 'F'))))
print(df['final_grade'].value_counts())


avg_by_gender = df.groupby('gender')['final_exam_score'].mean()
print(avg_by_gender)


all_students = df['student_id'].count()
print(all_students)


avg_parental_education_by_final_score = df.groupby('parental_education')["final_exam_score"].mean()
print(avg_parental_education_by_final_score)


corr = df['study_time_hours'].corr(df['final_exam_score'])
print(f"(Correlation): {corr:.2f}\n")

df['study_category'] = pd.cut(df['study_time_hours'], 
         bins=[0, 3, 6, 9, 15], 
          labels=['Low (0-3 H)', 'Average (3-6 H)', 'Good (6-9 H)', 'Very High (9+ H)'])

result = df.groupby('study_category')['final_exam_score'].mean()
print("Average Final Exam Scores by Study Time Categories:")
print(result)


avg_attendance_by_final_score = df.groupby('final_exam_score')['attendance_percent'].mean()
print(avg_attendance_by_final_score)


sleep_hours_corr = df['sleep_hours'].corr(df['final_exam_score'])
print(f"(Correlation between sleep hours and final exam score): {sleep_hours_corr:.2f}\n") 


df["extracurricular_activities"].value_counts()
print(df["extracurricular_activities"].value_counts())


grade_map = {
    "A": 4,
    "B": 3,
    "C": 2,
    "D": 1,
    "F": 0
}

df["final_grade_num"] = df["final_grade"].map(grade_map)

avg_extracurricular_by_final_grade = df.groupby("extracurricular_activities")["final_grade_num"].mean()
print(avg_extracurricular_by_final_grade)


pd.crosstab(
    df["part_time_job"],
    df["final_grade"]
)
print(pd.crosstab(
    df["part_time_job"],    
    df["final_grade"]
))


avg_parental_education_by_final_exam_score = df.groupby('parental_education')['final_exam_score'].mean()
print(avg_parental_education_by_final_exam_score)


previous_correlation = df['previous_grade'].corr(df['final_exam_score'])
print(f"(Correlation between previous grade and final exam score): {previous_correlation:.2f}\n")

Gender_by_male_female = df['gender'].value_counts()
print(Gender_by_male_female)



