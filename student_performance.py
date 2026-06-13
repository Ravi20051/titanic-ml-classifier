import pandas as pd
import matplotlib.pyplot as plt
au=pd.DataFrame({
    "Studentid":["001","002","003","004","005","006","007","008","009","010"],
    "Name":["Ravi","santhosh","rahul","srikar","amit","john","pooja","lisa","karan","kiran"],
})
marks=pd.DataFrame({
    "Math":[90,89,78,67,89,70,56,78,68,67],
    "Science":[80,78,67,45,65,67,67,68,89,78],
    "English":[78,78,76,54,67,89,76,67,89,56]
})
Attendence=pd.DataFrame({
    "Attendence":[90,78,67,56,78,67,67,56,67,78]
})
df=pd.concat([au,marks,Attendence],axis=1)
df["total_marks"]=df["Math"]+df["Science"]+df["English"]
df["average_marks"]=(df["Math"]+df["Science"]+df["English"])/3
def grade(average_marks):
    if average_marks>=90:
        return "A"
    elif average_marks>=80 and average_marks<90:
        return "B"
    elif average_marks>=70 and average_marks<80:
        return "C"
    elif average_marks>=60 and average_marks<70:
        return "D"
    else:
        return "F"
df["grade"]=df["average_marks"].apply(grade)
def top(average_marks):
    if average_marks>80:
        return "top"
df["top"]=df["average_marks"].apply(top)
print(df)
print("======================")
print("The top 3 students are:")
print(df[df["top"]=="top"]["Name"])
print("======================")
print("Attendence below 75 is :")
print(df[df["Attendence"]<75]["Name"])
print("======================")
plt.figure(figsize=(8,5))
plt.bar(df["Name"].values,df["average_marks"],color="green")
plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.show()

df.to_csv("student_data.csv",index=False)