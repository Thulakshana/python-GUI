import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import pyodbc
from datetime import datetime

CONFIG_FILE = "config.json"

# ---------------- Database Connection ----------------
def load_server():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
                return data.get("server", "").strip()
        except json.JSONDecodeError:
            return ""
    return ""

def get_connection():
    server_name = load_server()
    if server_name == "":
        raise Exception("Server name not configured.")
    # Replace 'pr' with your database name
    conn_str = f'DRIVER={{SQL Server}};SERVER={server_name};DATABASE=fingerprint;Trusted_Connection=yes;'
    conn = pyodbc.connect(conn_str)
    return conn

# ---------------- Server Config Window ----------------
class ServerConfigWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Server Configuration")
        self.geometry("400x220")
        self.resizable(False, False)

        tk.Label(self, text="SQL Server Name", font=("Arial", 11)).pack(pady=10)
        self.server_entry = tk.Entry(self, width=45)
        self.server_entry.pack(pady=5)

        tk.Button(
            self,
            text="Save & Continue",
            width=25,
            command=lambda: save_server(self.server_entry, self)
        ).pack(pady=20)

def save_server(server_value, window):
    server = server_value.get().strip()
    if server == "":
        messagebox.showwarning("Input Error", "Server name cannot be empty")
        return
    with open(CONFIG_FILE, "w") as f:
        json.dump({"server": server}, f, indent=4)
    messagebox.showinfo("Success", "Server name saved successfully")
    window.destroy()
    LoginWindow().mainloop()

# ---------------- Login Window ----------------
class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("400x250")
        self.resizable(False, False)

        tk.Label(self, text="Username", font=("Arial", 11)).pack(pady=10)
        self.username_entry = tk.Entry(self, width=35)
        self.username_entry.pack(pady=5)

        tk.Label(self, text="Password", font=("Arial", 11)).pack(pady=10)
        self.password_entry = tk.Entry(self, width=35, show="*")
        self.password_entry.pack(pady=5)

        tk.Button(
            self,
            text="Login",
            width=25,
            command=self.check_login
        ).pack(pady=20)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "admin" and password == "admin":
            self.destroy()
            app = AttendanceApp()
            app.show_dashboard()
            app.mainloop()
        else:
            messagebox.showerror("Login Failed", "Username or password is incorrect")

# ---------------- Main Attendance App ----------------
class AttendanceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fingerprint Attendance System")
        self.geometry("1200x650")

        self.server_name = load_server()

        # Layout frames
        self.navbar = tk.Frame(self, bg="#2c3e50", width=220)
        self.navbar.pack(side="left", fill="y")

        self.content = tk.Frame(self, bg="#ecf0f1")
        self.content.pack(side="right", fill="both", expand=True)

        self.create_navbar()
        self.show_dashboard()

    def create_navbar(self):
        tk.Label(self.navbar, text="ATTENDANCE", fg="white", bg="#2c3e50",
                 font=("Arial", 16, "bold")).pack(pady=20)
        buttons = [
            ("Dashboard", self.show_dashboard),
            ("Employees", self.show_employees),
            ("Shifts & Schedules", self.show_shifts),
            ("Attendance", self.show_attendance),
            ("Reports", self.show_reports),
            ("Leave Management", self.show_leave),
            ("Payroll", self.show_payroll),
            ("Devices & Import", self.show_devices),
            ("Settings", self.show_settings),
            ("Logging", self.show_logging),
            ("Logout", self.quit)
        ]
        for text, cmd in buttons:
            btn = tk.Button(self.navbar, text=text, command=cmd, anchor="w", padx=20,
                            relief="flat", bg="#34495e", fg="white",
                            activebackground="#1abc9c", activeforeground="white")
            btn.pack(fill="x", pady=2)

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_content()
        tk.Label(self.content, text="Dashboard", font=("Arial", 22), bg="#ecf0f1").pack(pady=20)

    # ---------------- Employees Page ----------------
    def show_employees(self):
        self.clear_content()
        tk.Label(self.content, text="Employees", font=("Arial", 22), bg="#ecf0f1").pack(pady=20)

        frame = tk.Frame(self.content, bg="#ecf0f1")
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        # --- Left side: form ---
        form_frame = tk.Frame(frame, bg="#ecf0f1")
        form_frame.pack(side="left", fill="y", padx=10)

        tk.Label(form_frame, text="Employee ID", font=("Arial", 12), bg="#ecf0f1").grid(row=0, column=0, pady=5, sticky="w")
        tk.Label(form_frame, text="Employee NIC", font=("Arial", 12), bg="#ecf0f1").grid(row=1, column=0, pady=5, sticky="w")
        tk.Label(form_frame, text="Employee Name", font=("Arial", 12), bg="#ecf0f1").grid(row=2, column=0, pady=5, sticky="w")
        tk.Label(form_frame, text="Department", font=("Arial", 12), bg="#ecf0f1").grid(row=3, column=0, pady=5, sticky="w")
        tk.Label(form_frame, text="Designation", font=("Arial", 12), bg="#ecf0f1").grid(row=4, column=0, pady=5, sticky="w")
        tk.Label(form_frame, text="status", font=("Arial", 12), bg="#ecf0f1").grid(row=5, column=0, pady=5, sticky="w")

        
        employeeid_entry = tk.Entry(form_frame, width=30)
        employeeid_entry.grid(row=0, column=1, pady=5, padx=5)

        employeenic_entry = tk.Entry(form_frame, width=30)
        employeenic_entry.grid(row=1, column=1, pady=5, padx=5)

        employeename_entry = tk.Entry(form_frame, width=30)
        employeename_entry.grid(row=2, column=1, pady=5, padx=5)

        department_entry = tk.Entry(form_frame, width=30)
        department_entry.grid(row=3, column=1, pady=5, padx=5)

        designation_entry = tk.Entry(form_frame, width=30)
        designation_entry.grid(row=4, column=1, pady=5, padx=5)

        

        status_var = tk.StringVar()
        status_entry = ttk.Combobox(
        form_frame,
        textvariable=status_var,
        values=["Active", "Inactive", "Suspended"],
        state="readonly",
        width=30)
        status_entry.grid(row=5, column=1, pady=5, padx=5)
        #*************************************************************************************************************************
        
        #name_entry = tk.Entry(form_frame, width=30)
        #name_entry.grid(row=0, column=1, pady=5, padx=5)

        #age_entry = tk.Entry(form_frame, width=30)
        #age_entry.grid(row=1, column=1, pady=5, padx=5)
#**********************************************************************************************************************************
        def save_employee():
            employeeid=employeeid_entry.get().strip()
            employeenic=employeenic_entry.get().strip()
            employeename=employeename_entry.get().strip()
            department=department_entry.get().strip()
            designation=designation_entry.get().strip()
            status=status_var.get().strip()

            ###########################################################################################
            #name = name_entry.get().strip()
            #age = age_entry.get().strip()
            #########################################################################################
            if not employeeid or not employeenic or not employeename or not department or not designation or not status:
                messagebox.showwarning("Input Error", "Please enter all employee details")
                return
            try:
               # age_int = int(age)
                empid=int(employeeid)
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO [users] (employee_id, nic_number , employee_name, department,designation,status) VALUES (?, ?,?,?,?,?)", (empid,employeenic,employeename,department,designation,status))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Employee saved successfully")
                #********************************************************************************************
               # name_entry.delete(0, tk.END)
               # age_entry.delete(0, tk.END)
                #*******************************************************************************************

                employeeid.delete(0, tk.END)
                employeenic.delete(0, tk.END)
                employeename.delete(0, tk.END)
                department.delete(0, tk.END)
                designation.delete(0, tk.END)
                status_entry.current(0)
                load_table()
            except ValueError:
                messagebox.showerror("Error", "Employee ID must be a number")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        tk.Button(form_frame, text="Save Employee", width=20, command=save_employee).grid(
            row=6, column=0, columnspan=2, pady=10
        )

        # --- Right side: table ---
        table_frame = tk.Frame(frame, bg="#ecf0f1")
        table_frame.pack(side="left", fill="both", expand=True, padx=20)

        tree = ttk.Treeview(table_frame, columns=("employee_id", "nic_number", "employee_name", "department", "designation", "status"), show="headings")
        tree.heading("employee_id", text="Employee ID")
        tree.heading("nic_number", text="NIC")
        tree.heading("employee_name", text="Name")
        tree.heading("department", text="Department")
        tree.heading("designation", text="Designation")
        tree.heading("status", text="Status")


        tree.column("employee_id", width=80, anchor="center")
        tree.column("nic_number", width=120, anchor="center")
        tree.column("employee_name", width=150, anchor="center")
        tree.column("department", width=120, anchor="center")
        tree.column("designation", width=120, anchor="center")
        tree.column("status", width=100, anchor="center")

        tree.pack(fill="both", expand=True)

        def load_table():
            for row in tree.get_children():
                tree.delete(row)
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT employee_id,nic_number,employee_name,department,designation,status FROM [users]")
            for r in cursor.fetchall():
                tree.insert("", tk.END, values=r)
            conn.close()

        load_table()

    # ---------------- Other Pages ----------------
    def show_shifts(self):
        self.clear_content()
        tk.Label(self.content, text="Shifts & Schedules", font=("Arial", 22), bg="#ecf0f1").pack(pady=20)

        frame = tk.Frame(self.content, bg="#ecf0f1")
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        form_frame = tk.Frame(frame, bg="#ecf0f1")
        form_frame.pack(side="left", fill="y", padx=10)

        tk.Label(form_frame, text="Shift ID", font=("Arial", 12), bg="#ecf0f1").grid(row=0, column=0, pady=5, sticky="w")
        tk.Label(form_frame, text="Shift Name", font=("Arial", 12), bg="#ecf0f1").grid(row=1, column=0, pady=5, sticky="w")
        tk.Label(form_frame, text="Start Time", font=("Arial", 12), bg="#ecf0f1").grid(row=2, column=0, pady=5, sticky="w")
        tk.Label(form_frame, text="End Time", font=("Arial", 12), bg="#ecf0f1").grid(row=3, column=0, pady=5, sticky="w")

#************************************************************************************************
       
        def get_datetime(hour_cb, minute_cb):
            hour = hour_cb.get()
            minute = minute_cb.get()

            if not hour or not minute:
                return None

            today = datetime.today().strftime("%Y-%m-%d")

            try:
                return datetime.strptime(
                    f"{today} {hour}:{minute}:00",
                    "%Y-%m-%d %H:%M:%S"
                )
            except ValueError:
                messagebox.showerror(
                    "Invalid Time",
                    "Please select valid hour and minute"
                )
            return None


       #**************************************************************************************
        # Shift ID
        shiftid_entry = tk.Entry(form_frame, width=30)
        shiftid_entry.grid(row=0, column=1, pady=5, padx=5)

# Shift Name
        shiftname_entry = tk.Entry(form_frame, width=30)
        shiftname_entry.grid(row=1, column=1, pady=5, padx=5)

        # ---------------- Start Time ----------------
        tk.Label(form_frame, text="Start Time").grid(row=2, column=0, pady=5, padx=5, sticky="e")

        start_hour_cb = ttk.Combobox(
            form_frame,
            values=[f"{i:02d}" for i in range(24)],
            width=5,
            state="readonly"
        )
        start_hour_cb.grid(row=2, column=1, sticky="w", padx=(5, 0))
        start_hour_cb.set("08")

        start_minute_cb = ttk.Combobox(
            form_frame,
            values=[f"{i:02d}" for i in range(60)],
            width=5,
            state="readonly"
        )
        start_minute_cb.grid(row=2, column=1, sticky="w", padx=(70, 0))
        start_minute_cb.set("00")

        # ---------------- End Time ----------------
        tk.Label(form_frame, text="End Time").grid(row=3, column=0, pady=5, padx=5, sticky="e")

        end_hour_cb = ttk.Combobox(
            form_frame,
            values=[f"{i:02d}" for i in range(24)],
            width=5,
            state="readonly"
        )
        end_hour_cb.grid(row=3, column=1, sticky="w", padx=(5, 0))
        end_hour_cb.set("17")

        end_minute_cb = ttk.Combobox(
            form_frame,
            values=[f"{i:02d}" for i in range(60)],
            width=5,
            state="readonly"
        )
        end_minute_cb.grid(row=3, column=1, sticky="w", padx=(70, 0))
        end_minute_cb.set("00")

        def save_shift():
            shiftid = shiftid_entry.get().strip()
            shiftname = shiftname_entry.get().strip()

            starttime = get_datetime(start_hour_cb, start_minute_cb)
            endtime = get_datetime(end_hour_cb, end_minute_cb)

            if not shiftid or not shiftname or not starttime or not endtime:
                messagebox.showwarning("Input Error", "Please enter all shift details")
                return

            try:
                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute("""
                    INSERT INTO shifts (shift_id, shift_name, start_time, end_time)
                    VALUES (?, ?, ?, ?)
                """, (shiftid, shiftname, starttime, endtime))

                conn.commit()
                conn.close()

                messagebox.showinfo("Success", "Shift saved successfully")

                # Clear inputs
                shiftid_entry.delete(0, tk.END)
                shiftname_entry.delete(0, tk.END)
                start_hour_cb.set("")
                start_minute_cb.set("")
                end_hour_cb.set("")
                end_minute_cb.set("")

                load_table()

            except Exception as e:
                messagebox.showerror("Error", str(e))


            
        #*************************************************************************************************************************        


        tk.Button(form_frame, text="Save Shift", width=20, command=save_shift).grid(
            row=4, column=0, columnspan=2, pady=10
        )
        

        table_frame = tk.Frame(frame, bg="#ecf0f1")
        table_frame.pack(side="left", fill="both", expand=True, padx=20)

        tree = ttk.Treeview(table_frame, columns=("shift_id", "shift_name", "start_time", "end_time"), show="headings")

        tree.heading("shift_id", text="shift ID")
        tree.heading("shift_name",text="shift Name")
        tree.heading("start_time",text="start Time")
        tree.heading("end_time",text="end_time")

        tree.column("shift_id", width=80, anchor="center")
        tree.column("shift_name", width=120, anchor="center")
        tree.column("start_time", width=150, anchor="center")
        tree.column("end_time", width=120, anchor="center")





        tree.pack(fill="both", expand=True)
        def load_table():
            for row in tree.get_children():
                tree.delete(row)
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT shift_id,shift_name,start_time,end_time FROM [shifts]")
            for r in cursor.fetchall():
                tree.insert("", tk.END, values=r)
            conn.close()

        load_table()



        
      #*****************************************************************************************************************************************  

    def show_attendance(self):
        self.clear_content()
        tk.Label(self.content, text="Attendance", font=("Arial", 22), bg="#ecf0f1").pack(pady=20)

    def show_reports(self):
        self.clear_content()
        tk.Label(self.content, text="Reports", font=("Arial", 22), bg="#ecf0f1").pack(pady=20)

    def show_leave(self):
        self.clear_content()
        tk.Label(self.content, text="Leave Management", font=("Arial", 22), bg="#ecf0f1").pack(pady=20)

    def show_payroll(self):
        self.clear_content()
        tk.Label(self.content, text="Payroll Attendance", font=("Arial", 22), bg="#ecf0f1").pack(pady=20)

    def show_devices(self):
        self.clear_content()
        tk.Label(self.content, text="Devices & Import", font=("Arial", 22), bg="#ecf0f1").pack(pady=20)

    def show_settings(self):
        self.clear_content()
        tk.Label(self.content, text="Settings", font=("Arial", 22), bg="#ecf0f1").pack(pady=20)

    def show_logging(self):
        self.clear_content()
        tk.Label(self.content, text="Logging", font=("Arial", 22), bg="#ecf0f1").pack(pady=20)
        tk.Label(self.content, text=f"Connected Server: {self.server_name}", font=("Arial", 14), bg="#ecf0f1").pack(pady=10)

# ---------------- App Start ----------------
if __name__ == "__main__":
    existing_server = load_server()
    if existing_server:
        LoginWindow().mainloop()
    else:
        ServerConfigWindow().mainloop()
