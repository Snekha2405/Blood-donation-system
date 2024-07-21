from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk,simpledialog
from PIL import Image, ImageTk  # Import Pillow modules


db_host = "localhost"
db_name = "blooddonation"
db_user = "root"
db_password = "Snekha@2402"
def connect_to_database():
    try:
        connection = mysql.connector.connect(host=db_host, database=db_name, user=db_user, password=db_password)
        return connection
    except mysql.connector.Error as err:
        messagebox.showerror(title="Database Error", message=err)
        return None


# Function to check login credentials
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Replace these with your actual credentials (or a mechanism to store them securely)
    correct_username = "admin"
    correct_password = "123"

    if username == correct_username and password == correct_password:
        messagebox.showinfo(title="Login Successful!", message="Welcome to DONATE4LIFE!")
        destroy_login_page()
        create_home_page()
    else:
        messagebox.showerror(title="Error", message="Invalid username or password.")

# Function to destroy the login page
def destroy_login_page():
    login_frame.destroy()

# Function to create the home page
def create_home_page():
    # Create a new window for the home page
    home_window = Toplevel()
    home_window.title("DONATE4LIFE - Home Page")

    # Get screen width and height
    screen_width = home_window.winfo_screenwidth()
    screen_height = home_window.winfo_screenheight()

    # Set the geometry of the window to cover the entire screen
    home_window.geometry(f"{screen_width}x{screen_height}")

    # Load background image for home page
    home_background_image = Image.open("home.jpg")
    home_background_image = home_background_image.resize((screen_width, screen_height))
    home_background_photo = ImageTk.PhotoImage(home_background_image)

    # Create a label to display the background image
    home_background_label = Label(home_window, image=home_background_photo)
    home_background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create buttons for blood donation management system project
    # Example buttons, you can customize as needed
    donors_button = Button(home_window, text="DONATER DETAILS",bg="lightgrey" ,font=("Times New Roman", 12,"bold"),height=3, width=50,command=donors)
    donors_button.place(x=150, y=150)

    receiver_button = Button(home_window, text="RECEIVER DETAILS", bg="lightgrey",font=("Times New Roman", 12,"bold"),height=3, width=50,command=receiver)
    receiver_button.place(x=150, y=230)
    
   

    logout_button = Button(home_window, text="LOGOUT",bg="lightgrey" ,font=("Times New Roman", 12,"bold"),height=3, width=50,command=logout)
    logout_button.place(x=150,y=310)

    

    # Add more buttons or options as needed

    # Run the home window's main loop
    home_window.mainloop()

# Functions to handle button commands (example functions, customize as needed)
# Function to create the Donater Details page
def create_donater_details_page():
    # Create a new window for the Donater Details page
    
    donater_details_window = Toplevel()
    donater_details_window.title("DONATE4LIFE - Donater Details")

    # Get screen width and height
    screen_width = donater_details_window.winfo_screenwidth()
    screen_height = donater_details_window.winfo_screenheight()

    # Set the geometry of the window to cover the entire screen
    donater_details_window.geometry(f"{screen_width}x{screen_height}")
    background_image = Image.open("bg1.jpg")
    background_image = background_image.resize((screen_width, screen_height))
    background_photo = ImageTk.PhotoImage(background_image)

        # Create a label to display the background image
    background_label = Label(donater_details_window, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Ensure that the image is not garbage collected
    background_label.image = background_photo

    # Create a label to display the background image
    

    # Function to view the donors table
    # Function to view the donors table
    def view_donors_table():
        # Create a new window for displaying donor details
        donors_table_window = Toplevel()
        donors_table_window.title("DONATE4LIFE - Donors Table")

        # Get screen width and height
        screen_width = donors_table_window.winfo_screenwidth()
        screen_height = donors_table_window.winfo_screenheight()

        # Set the geometry of the window (optional for full screen)
        donors_table_window.geometry(f"{screen_width}x{screen_height}")

        connection = connect_to_database()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM donors")
            donor_data = cursor.fetchall()

            # Create a Treeview widget to display donor data
            donor_table = ttk.Treeview(donors_table_window, columns=("donor_id", "donor_name", "age", "gender", "address", "phone_number", "blood_group", "other_medical_details"), show="headings")
            donor_table.heading("donor_id", text="ID")
            donor_table.heading("donor_name", text="Donor Name")
            donor_table.heading("age", text="Age")
            donor_table.heading("gender", text="Gender")
            donor_table.heading("address", text="Address")
            donor_table.heading("phone_number", text="Phone Number")
            donor_table.heading("blood_group", text="Blood Group")
            donor_table.heading("other_medical_details", text="Other Medical Details")
            
            donor_table.grid(row=0, columnspan=1, padx=5, pady=5)

            # Insert data into the Treeview
            for donor in donor_data:
                donor_table.insert("", "end", values=donor)

            # Adjusting column widths
            donor_table.column("donor_id", width=50)
            donor_table.column("donor_name", width=150)
            donor_table.column("age", width=50)
            donor_table.column("gender", width=80)
            donor_table.column("address", width=200)
            donor_table.column("phone_number", width=120)
            donor_table.column("blood_group", width=80)
            donor_table.column("other_medical_details", width=200)
            

            # Function to handle delete button clicks
            

        except mysql.connector.Error as err:
            messagebox.showerror(title="Database Error", message=err)
        finally:
            if connection:
                connection.close()

        # Run the window's main loop
        donors_table_window.mainloop()




    


    # Function to handle saving donor details
    def save_donor_details():
        connection = connect_to_database()
        if not connection:
            return
        donor_name = donor_name_entry.get()
        age=age_entry.get()
        gender = gender_var.get()
        address = address_entry.get()
        phone_number = phone_number_entry.get()
        blood_group = blood_group_entry.get()
        other_medical_details = other_medical_details_entry.get("1.0", END)  # Retrieve text from Text widget


        try:
            cursor = connection.cursor()
            sql = ("INSERT INTO donors (donor_name, age, gender, address, phone_number, blood_group, other_medical_details) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)")
            cursor.execute(sql, (donor_name, age, gender, address, phone_number, blood_group, other_medical_details))
            connection.commit()
            messagebox.showinfo("Success", "Donor details saved successfully!")

        except mysql.connector.Error as err:
            messagebox.showerror(title="Database Error", message=err)
        finally:
            if connection:
                connection.close()

    

        # Here, you can add code to save the donor details to a database or perform other actions







    
        
        # Example: Print the donor details
        print("Donor Name:", donor_name)
        print("Age:", age)
        print("Gender:", gender)
        print("Address:", address)
        print("Phone Number:", phone_number)
        print("Blood Group:", blood_group)
        print("Other Medical Details:", other_medical_details)

    def delete_donor_by_id():
        donor_id = simpledialog.askinteger("Input", "Enter Donor ID to delete:")
        if donor_id is None:
            return

        connection = connect_to_database()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            cursor.callproc("delete_donor_id", [donor_id])
            connection.commit()
            messagebox.showinfo("Success", "Donor record deleted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror(title="Database Error", message=err)
        finally:
            if connection:
                connection.close()
    
    def update_donor_details():
        def save_changes():
            donor_id = donor_id_entry.get()
            new_name = entry_values[0].get()
            new_age = entry_values[1].get()
            new_gender = gender_var.get()
            new_address = entry_values[3].get()
            new_phone_number = entry_values[4].get()
            new_blood_type = entry_values[5].get()

            if not all([donor_id, new_name, new_age, new_gender, new_address, new_phone_number, new_blood_type]):
                messagebox.showerror(title="Input Error", message="All fields are required.")
                return

            connection = connect_to_database()
            if not connection:
                return

            try:
                cursor = connection.cursor()
                cursor.callproc('update_donor_id', [donor_id, new_name, new_age, new_gender, new_address, new_phone_number, new_blood_type])
                connection.commit()
                messagebox.showinfo(title="Success", message=f"Donor ID {donor_id} updated successfully.")
                donor_details_window.destroy()  # Close the window after successful update
            except mysql.connector.Error as err:
                messagebox.showerror(title="Error", message=str(err))
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        donor_details_window = Toplevel()
        donor_details_window.title("Update Donor Details")

        # Donor ID Label and Entry
        donor_id_label = Label(donor_details_window, text="Donor ID:", font=("Times New Roman", 16))
        donor_id_label.grid(row=0, column=0, padx=10, pady=10)
        donor_id_entry = Entry(donor_details_window, font=("Times New Roman", 16))
        donor_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Other Donor Details Labels and Entries
        details_labels = ["Name:", "Age:", "Gender:", "Address:", "Phone Number:", "Blood Type:"]
        entry_values = [StringVar() for _ in range(len(details_labels))]
        for i, label_text in enumerate(details_labels):
            label = Label(donor_details_window, text=label_text, font=("Times New Roman", 16))
            label.grid(row=i+1, column=0, padx=10, pady=10)
            entry = Entry(donor_details_window, font=("Times New Roman", 16), textvariable=entry_values[i])
            entry.grid(row=i+1, column=1, padx=10, pady=10)
            if i == 2:  # Gender dropdown
                gender_options = ["Male", "Female", "Other"]
                gender_var = StringVar(donor_details_window)
                gender_var.set(gender_options[0])  # Default value
                gender_dropdown = OptionMenu(donor_details_window, gender_var, *gender_options)
                gender_dropdown.config(font=("Times New Roman", 12))
                gender_dropdown.grid(row=i+1, column=1, padx=10, pady=10)

        save_button = Button(donor_details_window, text="Save", command=save_changes, font=("Times New Roman", 16))
        save_button.grid(row=len(details_labels)+1, columnspan=2, pady=10)

        donor_details_window.mainloop()



    # Optionally, show a success message

# Create input fields for donor details
    donor_name_label = Label(donater_details_window, text="Donor Name:", font=("Times New Roman", 16))
    donor_name_label.grid(row=0, column=0, padx=10, pady=10)
    donor_name_entry = Entry(donater_details_window, font=("Times New Roman", 16))
    donor_name_entry.grid(row=0, column=1, padx=10, pady=10)

    age_label = Label(donater_details_window, text="Age:", font=(None, 16))
    age_label.grid(row=1, column=0, padx=10, pady=10)
    age_entry = Entry(donater_details_window, font=("Times New Roman", 16))
    age_entry.grid(row=1, column=1, padx=10, pady=10)

    gender_label = Label(donater_details_window, text="Gender:", font=(None, 16))
    gender_label.grid(row=2, column=0, padx=10, pady=10)
    gender_var = StringVar(donater_details_window)
    gender_var.set("Male")
    gender_options = ["Male", "Female", "Other"]
    gender_dropdown = OptionMenu(donater_details_window, gender_var, *gender_options)
    gender_dropdown.config(font=(None, 16))
    gender_dropdown.grid(row=2, column=1, padx=10, pady=10)

    address_label = Label(donater_details_window, text="Address:", font=("Times New Roman", 16))
    address_label.grid(row=3, column=0, padx=10, pady=10)
    address_entry = Entry(donater_details_window, font=("Times New Roman", 16))
    address_entry.grid(row=3, column=1, padx=10, pady=10)

    phone_number_label = Label(donater_details_window, text="Phone Number:", font=("Times New Roman", 16))
    phone_number_label.grid(row=4, column=0, padx=10, pady=10)
    phone_number_entry = Entry(donater_details_window, font=("Times New Roman", 16))
    phone_number_entry.grid(row=4, column=1, padx=10, pady=10)

    blood_group_label = Label(donater_details_window, text="Blood Group:", font=("Times New Roman", 16))
    blood_group_label.grid(row=5, column=0, padx=10, pady=10)
    blood_group_entry = Entry(donater_details_window, font=("Times New Roman", 16))
    blood_group_entry.grid(row=5, column=1, padx=10, pady=10)

    other_medical_details_label = Label(donater_details_window, text="Other Medical Details:", font=("Times New Roman", 16))
    other_medical_details_label.grid(row=6, column=0, padx=10, pady=10)
    other_medical_details_entry = Text(donater_details_window, font=("Times New Roman", 16), height=5, width=30)
    other_medical_details_entry.grid(row=6, column=1, padx=10, pady=10)

    # Create a button to save donor details
    save_button = Button(donater_details_window, text="Save", command=save_donor_details, font=("Times New Roman", 16))
    save_button.grid(row=7, columnspan=2, pady=10)

    view_donors_button = Button(donater_details_window, text="View Donors", command=view_donors_table, font=("Times New Roman", 16))
    view_donors_button.grid(row=9, columnspan=2, pady=10)

    delete_button = Button(donater_details_window, text="Delete", command=delete_donor_by_id, font=("Times New Roman", 16))
    delete_button.grid(row=10, columnspan=2, pady=10)

    update_button = Button(donater_details_window, text="Modify", command=update_donor_details, font=("Times New Roman", 16))
    update_button.grid(row=11, columnspan=2, pady=10)


    # Run the Donater Details window's main loop
    donater_details_window.mainloop()

# Modify the donors() function to open the Donater Details page
def donors():
    create_donater_details_page()

def create_receiver_details_page():
    # Create a new window for the Donater Details page
    
    receiver_details_window = Toplevel()
    receiver_details_window.title("DONATE4LIFE - Receiver Details")

    # Get screen width and height
    screen_width = receiver_details_window.winfo_screenwidth()
    screen_height = receiver_details_window.winfo_screenheight()

    # Set the geometry of the window to cover the entire screen
    receiver_details_window.geometry(f"{screen_width}x{screen_height}")
    
    background_image = Image.open("bg1.jpg")
    background_image = background_image.resize((screen_width, screen_height))
    background_photo = ImageTk.PhotoImage(background_image)

        # Create a label to display the background image
    background_label = Label(receiver_details_window, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Ensure that the image is not garbage collected
    background_label.image = background_photo

    # Create a label to display the background image
    

    # Function to view the donors table
    # Function to view the donors table
    def view_receiver_table():
        # Create a new window for displaying donor details
        receiver_table_window = Toplevel()
        receiver_table_window.title("DONATE4LIFE - Receiver Table")

        # Get screen width and height
        screen_width = receiver_table_window.winfo_screenwidth()
        screen_height = receiver_table_window.winfo_screenheight()

        # Set the geometry of the window (optional for full screen)
        receiver_table_window.geometry(f"{screen_width}x{screen_height}")

        connection = connect_to_database()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM receiver")
            receiver_data = cursor.fetchall()

            # Create a Treeview widget to display donor data
            receiver_table = ttk.Treeview(receiver_table_window, columns=("receiver_id", "receiver_name", "age", "gender", "address", "phone_number", "blood_group", "other_medical_details"), show="headings")
            receiver_table.heading("receiver_id", text="ID")
            receiver_table.heading("receiver_name", text="Receiver Name")
            receiver_table.heading("age", text="Age")
            receiver_table.heading("gender", text="Gender")
            receiver_table.heading("address", text="Address")
            receiver_table.heading("phone_number", text="Phone Number")
            receiver_table.heading("blood_group", text="Blood Group")
            receiver_table.heading("other_medical_details", text="Other Medical Details")
            
            receiver_table.grid(row=0, columnspan=1, padx=5, pady=5)

            # Insert data into the Treeview
            for receiver in receiver_data:
                receiver_table.insert("", "end", values=receiver)

            # Adjusting column widths
            receiver_table.column("receiver_id", width=50)
            receiver_table.column("receiver_name", width=150)
            receiver_table.column("age", width=50)
            receiver_table.column("gender", width=80)
            receiver_table.column("address", width=200)
            receiver_table.column("phone_number", width=120)
            receiver_table.column("blood_group", width=80)
            receiver_table.column("other_medical_details", width=200)
            

            # Function to handle delete button clicks
            

        except mysql.connector.Error as err:
            messagebox.showerror(title="Database Error", message=err)
        finally:
            if connection:
                connection.close()

        # Run the window's main loop
        receiver_table_window.mainloop()




    


    # Function to handle saving donor details
    def save_receiver_details():
        connection = connect_to_database()
        if not connection:
            return
        receiver_name = receiver_name_entry.get()
        age=age_entry.get()
        gender = gender_var.get()
        address = address_entry.get()
        phone_number = phone_number_entry.get()
        blood_group = blood_group_entry.get()
        other_medical_details = other_medical_details_entry.get("1.0", END)  # Retrieve text from Text widget


        try:
            cursor = connection.cursor()
            sql = ("INSERT INTO receiver (receiver_name, age, gender, address, phone_number, blood_group, other_medical_details) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)")
            cursor.execute(sql, (receiver_name, age, gender, address, phone_number, blood_group, other_medical_details))
            connection.commit()
            messagebox.showinfo("Success", "Receiver details saved successfully!")

        except mysql.connector.Error as err:
            messagebox.showerror(title="Database Error", message=err)
        finally:
            if connection:
                connection.close()

    

        # Here, you can add code to save the donor details to a database or perform other actions







    
        
        # Example: Print the donor details
        print("Receiver Name:", receiver_name)
        print("Age:", age)
        print("Gender:", gender)
        print("Address:", address)
        print("Phone Number:", phone_number)
        print("Blood Group:", blood_group)
        print("Any diseases:", other_medical_details)

    def delete_receiver_by_id():
        receiver_id = simpledialog.askinteger("Input", "Enter Receiver ID to delete:")
        if receiver_id is None:
            return

        connection = connect_to_database()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            cursor.callproc("delete_receiver_id", [receiver_id])
            connection.commit()
            messagebox.showinfo("Success", "Receiver record deleted successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror(title="Database Error", message=err)
        finally:
            if connection:
                connection.close()
    
    def update_receiver_details():
        def save_changes():
            receiver_id = receiver_id_entry.get()
            new_name = entry_values[0].get()
            new_age = entry_values[1].get()
            new_gender = gender_var.get()
            new_address = entry_values[3].get()
            new_phone_number = entry_values[4].get()
            new_blood_type = entry_values[5].get()

            if not all([receiver_id, new_name, new_age, new_gender, new_address, new_phone_number, new_blood_type]):
                messagebox.showerror(title="Input Error", message="All fields are required.")
                return

            connection = connect_to_database()
            if not connection:
                return

            try:
                cursor = connection.cursor()
                cursor.callproc('update_receiver_id', [receiver_id, new_name, new_age, new_gender, new_address, new_phone_number, new_blood_type])
                connection.commit()
                messagebox.showinfo(title="Success", message=f"Receiver ID {receiver_id} updated successfully.")
                receiver_details_window.destroy()  # Close the window after successful update
            except mysql.connector.Error as err:
                messagebox.showerror(title="Error", message=str(err))
            finally:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

        receiver_details_window = Toplevel()
        receiver_details_window.title("Update Receiver Details")

        # Donor ID Label and Entry
        receiver_id_label = Label(receiver_details_window, text="Receiver ID:", font=("Times New Roman", 16))
        receiver_id_label.grid(row=0, column=0, padx=10, pady=10)
        receiver_id_entry = Entry(receiver_details_window, font=("Times New Roman", 16))
        receiver_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Other Donor Details Labels and Entries
        details_labels = ["Name:", "Age:", "Gender:", "Address:", "Phone Number:", "Blood Type:"]
        entry_values = [StringVar() for _ in range(len(details_labels))]
        for i, label_text in enumerate(details_labels):
            label = Label(receiver_details_window, text=label_text, font=("Times New Roman", 16))
            label.grid(row=i+1, column=0, padx=10, pady=10)
            entry = Entry(receiver_details_window, font=("Times New Roman", 16), textvariable=entry_values[i])
            entry.grid(row=i+1, column=1, padx=10, pady=10)
            if i == 2:  # Gender dropdown
                gender_options = ["Male", "Female", "Other"]
                gender_var = StringVar(receiver_details_window)
                gender_var.set(gender_options[0])  # Default value
                gender_dropdown = OptionMenu(receiver_details_window, gender_var, *gender_options)
                gender_dropdown.config(font=("Times New Roman", 12))
                gender_dropdown.grid(row=i+1, column=1, padx=10, pady=10)

        save_button = Button(receiver_details_window, text="Save", command=save_changes, font=("Times New Roman", 16))
        save_button.grid(row=len(details_labels)+1, columnspan=2, pady=10)

        receiver_details_window.mainloop()


    # Function to handle saving donor details
    

    # Create input fields for donor details
    receiver_name_label = Label(receiver_details_window, text="Receiver Name:", font=("Times New Roman", 16))
    receiver_name_label.grid(row=0, column=0, padx=10, pady=10)
    receiver_name_entry = Entry(receiver_details_window, font=("Times New Roman", 16))
    receiver_name_entry.grid(row=0, column=1, padx=10, pady=10)

    age_label = Label(receiver_details_window, text="Age:", font=(None, 16))
    age_label.grid(row=1, column=0, padx=10, pady=10)
    age_entry = Entry(receiver_details_window, font=("Times New Roman", 16))
    age_entry.grid(row=1, column=1, padx=10, pady=10)

    gender_label = Label(receiver_details_window, text="Gender:", font=(None, 16))
    gender_label.grid(row=2, column=0, padx=10, pady=10)
    gender_var = StringVar(receiver_details_window)
    gender_var.set("Male")
    gender_options = ["Male", "Female", "Other"]
    gender_dropdown = OptionMenu(receiver_details_window, gender_var, *gender_options)
    gender_dropdown.config(font=(None, 16))
    gender_dropdown.grid(row=2, column=1, padx=10, pady=10)

    address_label = Label(receiver_details_window, text="Address:", font=("Times New Roman", 16))
    address_label.grid(row=3, column=0, padx=10, pady=10)
    address_entry = Entry(receiver_details_window, font=("Times New Roman", 16))
    address_entry.grid(row=3, column=1, padx=10, pady=10)

    phone_number_label = Label(receiver_details_window, text="Phone Number:", font=("Times New Roman", 16))
    phone_number_label.grid(row=4, column=0, padx=10, pady=10)
    phone_number_entry = Entry(receiver_details_window, font=("Times New Roman", 16))
    phone_number_entry.grid(row=4, column=1, padx=10, pady=10)

    blood_group_label = Label(receiver_details_window, text="Blood Group:", font=("Times New Roman", 16))
    blood_group_label.grid(row=5, column=0, padx=10, pady=10)
    blood_group_entry = Entry(receiver_details_window, font=("Times New Roman", 16))
    blood_group_entry.grid(row=5, column=1, padx=10, pady=10)

    other_medical_details_label = Label(receiver_details_window, text="Any diseases:", font=("Times New Roman", 16))
    other_medical_details_label.grid(row=6, column=0, padx=10, pady=10)
    other_medical_details_entry = Text(receiver_details_window, font=("Times New Roman", 16), height=5, width=30)
    other_medical_details_entry.grid(row=6, column=1, padx=10, pady=10)

    # Create a button to save donor details
    save_button = Button(receiver_details_window, text="Save", command=save_receiver_details, font=("Times New Roman", 16))
    save_button.grid(row=7, columnspan=2, pady=10)

    view_receiver_button = Button(receiver_details_window, text="View Receivers", command=view_receiver_table, font=("Times New Roman", 16))
    view_receiver_button.grid(row=9, columnspan=2, pady=10)

    delete_button = Button(receiver_details_window, text="Delete", command=delete_receiver_by_id, font=("Times New Roman", 16))
    delete_button.grid(row=10, columnspan=2, pady=10)

    update_button = Button(receiver_details_window, text="Modify", command=update_receiver_details, font=("Times New Roman", 16))
    update_button.grid(row=11, columnspan=2, pady=10)

    # Run the Donater Details window's main loop
    receiver_details_window.mainloop()

def receiver():
    create_receiver_details_page()

    
def logout():
    messagebox.showinfo(title="Logout", message="You have been logged out.")

# Create the main window for the login page
root = Tk()
root.title("Login Page")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the geometry of the window to cover the entire screen
root.geometry(f"{screen_width}x{screen_height}")

# Load background image for login page
login_background_image = Image.open("bg2.jpg")
login_background_image = login_background_image.resize((screen_width, screen_height))
login_background_photo = ImageTk.PhotoImage(login_background_image)
# Create a label for the login page title


# Create a label to display the background image
login_background_label = Label(root, image=login_background_photo)
login_background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a login frame
login_frame = Frame(root, bg="white")
login_frame.place(relx=0.65, rely=0.5, anchor=CENTER)
login_title_label = Label(root, text=" DONATE4LIFE", font=("Helvetica", 30,), fg="red")
login_title_label.pack(side=TOP, fill=X)
# Create elements inside the login frame
username_label = Label(login_frame, text="Username:", font=(None, 16))
username_label.grid(row=0, column=0)

username_entry = Entry(login_frame, font=(None, 16), width=30)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = Label(login_frame, text="Password:", font=(None, 16))
password_label.grid(row=1, column=0)

password_entry = Entry(login_frame, font=(None, 16), show="*", width=30)
password_entry.grid(row=1, column=1, padx=5, pady=5)

login_button = Button(login_frame, text="Login", command=login, font=("Helvetica", 16))
login_button.grid(row=2, columnspan=2, pady=10)

# Run the main loop for the login page
root.mainloop()
