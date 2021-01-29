#import/setting up pandas
import pandas as pd
df_instructors = pd.read_csv('instructor.txt', sep=",", header=None)


df_instructors.columns=["instructor_id", "instructor_name", "department_name"] #renaming of columns, potentially get rid of this to keep integrity of dataframe for later saving
df_instructors


def menu():
    print("option 1")
    print("option 2")
    print("option 3")
    print("option 4")
    print("exit")
    
    
menu()
option = int(input("Enter your option:"))


while option != 5:
    if option == 1:
        print("result 1")
    elif option == 2:
        print("result 2")
    elif option == 3: #adding new record
        #print("result 3")
        
        #user input
        user_id=int(input("Enter ID to add:"))
        user_name=str(input("Enter name to add:"))
        user_department=str(input("Enter department to add:"))
        
        
        
        
        if (df_instructors["instructor_id"] == user_id).any():
            print("Instructor id already exists in the file")
        elif user_department not in df_instructors["department_name"].tolist():
            print("The department does not exist and hence the instructor record cannot be added to the database")
        else:
            #print("continuing to add new row")
            df_instructors=df_instructors.append(pd.DataFrame([[user_id, user_name, user_department]], columns=df_instructors.columns))
            print(df_instructors)
        
        
    elif option == 4: #removing record
        #print("result 4")
        
        #user input
        user_remove=int(input("Enter ID to remove:"))

        if (df_instructors["instructor_id"] == user_remove).any():
            df_instructors.drop(df_instructors.loc[df_instructors["instructor_id"]==user_remove].index, inplace=True)
            print(df_instructors)
        else:
            print("The ID does not appear in the file.")
            #print(df_instructors) 
    
    
    
    
    #print()
    #not needed^?
    
     
    menu() #continually opening menu function until exit (input == 5)
    option = int(input("Enter your option:"))
        
        
print("program exit")
#save df to file?