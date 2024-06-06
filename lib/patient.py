from config import cursor, conn


class Patient:
    def __init__(self, first_name, last_name, age, gender, phone, doctor_id, id = None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.doctor_id = doctor_id
        
    @classmethod
    def create_table(cls):
        """This method is going to create the doctors table"""
        sql = '''
        CREATE TABLE IF NOT EXISTS doctors(
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER
            gender TEXT, 
            phone TEXT,
            doctor_id INTEGER
            FOREIGN KEY (doctor_id)REFERENCES doctors(id)
        )
        '''

    @classmethod
    def drop_table(cls):
        """This method is going to drop the patients table"""
        sql = '''
        DROP TABLE IF EXISTS patients;
        '''
        cursor.execute(sql)
        conn.commit()

        cursor.execute(sql)
        conn.commit()

    def save(self):
        sql = """
            INSERT INTO patients(
            first_name,
            last_name, 
            age,
            gender,
            phone,
            doctor_id
            ) VALUES (?, ?, ?, ?, ?, ?);
        """

        cursor.execute(sql, (
            self.first_name,
            self.last_name,
            self.age,
            self.gender,
            self.phone,
            self.doctor_id
        ))
        conn.commit()


        #update patient id
        self.id = cursor.lastrowid


    @classmethod
    def create(cls, first_name, last_name, age, gender, phone, doctor_id):
        patient = cls(first_name, last_name, age, gender, phone, doctor_id)

        return patient
    
    def upddate(self):
        sql = '''
            UPDATE patient SET first_name = ?,last_name = ?, gender =?, phone = ?, doctor_id = ?
            WHERE id = ?
        '''

        cursor.execute(sql, (
            self.first_name,
            self.last_name,
            self.age,
            self.gender,
            self.phone,
            self.doctor_id
        ))

        conn.commit()

    def delete(self):
        pass

    @classmethod
    def instance_from_db(cls, row):
        pass

    @classmethod
    def fetch_by_id(cls,id):
        pass

