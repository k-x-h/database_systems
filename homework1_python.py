import csv

def get_instructors(): #use this to get current list of all records in instructor.txt file
    with open("instructor.txt") as csv_read:
        reader = csv.reader(csv_read) 
        for row in reader: # each row becomes a list within the "results" list
            instructors.append(row)

def menu():
    print("1. Enter the instructor ID to get the name of the instructor, affiliated department and the location of that department.")
    print("2. Enter the department name to get the location, budget and names of all instructors that work for the department.")
    print("3. Insert a record about a new instructor.")
    print("4. Delete a record about an instructor.")
    print("exit")
   
    
def save(): #only using this for debug, remove at end
    print("Save-----")










#adding new line to instructor.txt file only if it does not currently end with one (prevents later errors with adding new record)
file=open("instructor.txt", "r")
newline_check=[line.split(",") for line in file.readlines()]
if not newline_check[-1][2].endswith("\n"): #checking to see if the last character in the given file contains a newline
    print("DEBUG: adding newline") #For debug only, remove at end
    with open("instructor.txt", "a", newline='') as csv_write: #appending newline only if the file does not already end with one
        writer = csv.writer(csv_write)
        writer.writerow('')    
else: #For debug only, remove at end
    print("DEBUG: Newline already exists") 











instructors = []
get_instructors()

menu()
option = int(input("Enter your option:"))


while option != 5:
    if option == 1:
        print("result 1")
    elif option == 2:
        print("result 2")
        
        
    elif option == 3: #adding new record
  
        instructor_id = str(input("Enter the instructor id: "))
        instructor_name = str(input("Enter the instructor name: "))
        instructor_dept = str(input("Enter the instructor department: "))
        
        if str(instructor_id) in (item for sublist in instructors for item in sublist):
            print("Instructor id already exists in the file")
        elif str(instructor_dept) not in (item for sublist in instructors for item in sublist):
            print("The department does not exist and hence the instructor record cannot be added to the database")
        
        else:
            fields=[instructor_id, instructor_name, instructor_dept]
            with open("instructor.txt", "a", newline='') as csv_write:
                writer = csv.writer(csv_write)
                writer.writerow(fields)
            
        
        save() #not needed, just for debug
        
        
        
        
        
    elif option == 4: #removing record
    
    
    
        instructors = []
        get_instructors()

        
        user_id=input("Enter ID to remove:")

        if str(user_id) in (item for sublist in instructors for item in sublist):
            print("ID appears ---- Continue")
            
            id_list = []
            
            with open('instructor.txt', 'r') as readFile: 
                reader = csv.reader(readFile)
                for row in reader:
                    id_list.append(row)
                    for field in row:
                        if field == user_id:
                            id_list.remove(row)
                            
                            
            #writing results from the record removal into a txt file
            with open ("csv_results.txt", "w", newline="") as f:  #change this to instructor.txt when finished
                write = csv.writer(f)
                write.writerows(id_list)
                            
                            
                            
                            
        
            print(id_list) #not needed, just for debug
            save()  #not needed, just for debug
        
        else:
            print("The ID does not appear in the file.")
        
        
        
        
        
        
        
        
        
        
        
    
    
    menu() #continually opening menu function until exit (input == 5)
    option = int(input("Enter your option:"))
        
        
print("program exit")

