import mysql.connector

class DbConnect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="ASWIN@123",
                database="company_db"
            )
            return self.connection
        except Exception as e:
            return None

class EmployeeManager(DbConnect):
    def get_object(self,id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from employee where id=%s"
            value = (id,)
            self.cursor.execute(query,value)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)

    def post(self, **kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = """
                        insert into employee (name,place,mobile,email,department,salary,joining_date)
                        values (%s,%s,%s,%s,%s,%s,%s)
                    """
            values = [v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print(" New Employee Added Successfully")
        except Exception as e :
            print(e)

    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from employee"
            self.cursor.execute(query)
            record = self.cursor.fetchall()
            # for data in record:
            #     print(data)
            return record
        except Exception as e:
            # print(e)
            return []
    def retrieve(self,id=None):
        try:
            record=self.get_object(id=id)
            if record == None:
                print("No Employee Found")
            print(record)
        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            record = self.get_object(id=id)
            if record != None:
                placeholder=""
                for k in kwargs.keys():
                    placeholder += k + "=%s ,"
                    placeholder = placeholder.rstrip(",")
                    query = f"update employee set {placeholder} where id=%s "
                    value = [v for v in kwargs.values()]
                    value.append(id)
                    self.cursor.execute(query,value)
                    self.connect.commit()
                    print("Employee Updated Successfully")
            else:
                print("No Employee Found")
        except Exception as e:
            print(e)

    def delete(self,id=None):
        try:
            record = self.get_object(id=id)
            if record != None:
                query="delete from employee where id=%s"
                value=(id,)
                self.cursor.execute(query,value)
                self.connect.commit()
                print("Employee Deleted Successfully")
            else:
                print("No Employee Found")
        except Exception as e:
            print(e)

# connection_instance = DbConnect()
# print(connection_instance.get_connection())

employee_instance = EmployeeManager()
# employee_instance.post(name="Aljin",place="Kottapuram",mobile="7865875490",email="aljin@gmail.com",department="HR",salary=35000,joining_date="2026-01-12")
# employee_instance.post(name="Aswin",place="Ernakulam",mobile="9895929469",email="aswin@yahoo.com",department="Coding",salary=35000,joining_date="2026-03-01")
# employee_instance.post(name="Manu",place="Kochi",mobile="9809453465",email="manu@gmail.com",department="Accounting",salary=40000,joining_date="2025-02-28")
# employee_instance.post(name="Adi",place="Angamaly",mobile="8976098756",email="adi@luminar.com",department="IT",salary=25000,joining_date="2026-05-30")
# employee_instance.retrieve(id=3)
# employee_instance.put(id=3,name="Benhur")
# employee_instance.delete(id=1)
employee_instance.get()
