import csv








def get_results():
    with open("instructor.txt") as csv_read:
        reader = csv.reader(csv_read) 
        for row in reader: # each row becomes a list within the "results" list
            results.append(row)

def menu():
    print("option 1")
    print("option 2")
    print("option 3")
    print("option 4")
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











results = []
get_results()

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
        
        if str(instructor_id) in (item for sublist in results for item in sublist):
            print("Instructor id already exists in the file")
        elif str(instructor_dept) not in (item for sublist in results for item in sublist):
            print("The department does not exist and hence the instructor record cannot be added to the database")
        
        else:
            fields=[instructor_id, instructor_name, instructor_dept]
            with open("instructor.txt", "a", newline='') as csv_write:
                writer = csv.writer(csv_write)
                writer.writerow(fields)
            
        
        save() #not needed, just for debug
        
        
        
        
        
    elif option == 4: #removing record
    
    
    
        results = []
        get_results()

        
        user_id=input("Enter ID to remove:")

        if str(user_id) in (item for sublist in results for item in sublist):
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















#writing results list to a csv text file, could potentially be turned into a function and done at the end of each step in the menu to ensure edits are saved
#with open ("csv_results.txt", "w", newline="") as f:
#    write = csv.writer(f)
#    write.writerows(results)
