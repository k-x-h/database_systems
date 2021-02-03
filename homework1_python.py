import csv



#current problems:


results = []
with open("instructor.txt") as csv_read:
    reader = csv.reader(csv_read) 
    for row in reader: # each row becomes a list within the "results" list
        results.append(row)
        


#this adds a newline to the instructor.txt file so that csv writerow can start from a newline rather than the end of the last entry
with open("instructor.txt", "a", newline='') as csv_write:
    writer = csv.writer(csv_write)
    writer.writerow('')    




def menu():
    print("option 1")
    print("option 2")
    print("option 3")
    print("option 4")
    print("exit")
   
    
def save():
    print("Save-----")


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
            
        
        save() #unsure if a save needs to happen here, since it auto applies to the csv file
        
        
        
        
        
    elif option == 4: #removing record
    
    
    
        results = []
        with open("instructor.txt") as csv_read:
            reader = csv.reader(csv_read) 
            for row in reader: # each row becomes a list within the "results" list
                results.append(row)
        
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
                            
                            
            with open ("csv_results.txt", "w", newline="") as f:
                write = csv.writer(f)
                write.writerows(id_list)
                            
                            
                            
                            
        
            print(id_list)
            save() 
        
        else:
            print("The ID does not appear in the file.")
        
        
        
        
        
        
        
        
        
        
        
    
    
    menu() #continually opening menu function until exit (input == 5)
    option = int(input("Enter your option:"))
        
        
print("program exit")




