from config import cursor, conn

class Doctor:
    # all = {
    #     key: Value
    #     1: instance
    # }
    def __init__(self, id, first_name, last_name, gender, phone, yop, speciality, location):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.phone = phone
        self.yop = yop
        self.speciality = speciality
        self.location = location

    @classmethod
    def create_table(cls):
        """This method is going to create the doctors table"""
        sql = '''
        CREATE TABLE IF NOT EXISTS doctors(
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            gender TEXT, 
            phone TEXT,
            yop INTEGER,
            speciality TEXT,
            location TEXT
        )
        '''
        cursor.execute(sql)
        conn.commit()

    @classmethod
    def drop_table(cls):
        """This method is going to drop the doctors table"""
        sql = '''
        DROP TABLE IF EXISTS doctors;
        '''
        cursor.execute(sql)
        conn.commit()
    
    def __repr__(self) -> str:
        return f"Doctor {self.first_name} {self.last_name}, Gender: {self.gender}, Phone: {self.phone}, Experience: {self.yop}, Speciality: {self.speciality}, Location: {self.location}"
    
    def save(self):
        sql = """
            INSERT INTO doctors(
            first_name,
            last_name, 
            gender,
            phone,
            yop,
            speciality,
            location
            ) VALUES (?, ?, ?, ?, ?, ?, ?);
        """
        cursor.execute(sql, (
            self.first_name,
            self.last_name,
            self.gender,
            self.phone,
            self.yop,
            self.speciality,
            self.location
        ))
        conn.commit()

    def update(self):
        sql = '''
            UPDATE doctors SET first_name = ?,last_name = ?, gender =?, phone = ?, yop = ?, speciality = ?, location = ?
            WHERE id = ?
        '''

        cursor.execute(sql, (
            self.first_name,
            self.last_name,
            self.gender,
            self.phone,
            self.yop,
            self.speciality,
            self.location,
            self.id
        ))

        conn.commit()

        # maping a database raw to a python object

        # ty

        @classmethod
        def instance_from_db(cls, row):
            doctor = cls.all.get()

            if doctor:
                doctor.first_name = row[1]
                doctor.last_name = row[3]
                doctor.gender = row[3]
                doctor.phone = row[4]
                doctor.yop = row[4]
                doctor.speciality = row[5]
                doctor.location= row[6]
            else:
                # if the instance does not exist inside or all dictionary, create a doctor instance
                doctor = cls(
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7]
                )

                #key
                doctor.id = row[0]

                cls.all[doctor.id] = doctor

            return doctor
        
        @classmethod
        def fetch_by_id(cls,id):
            sql = '''
                SELECT * FROM doctors WHERE id = ?
            '''

            row = cursor.execute(sql, (id,)).fetchone()
            return cls.instance_from_db(row) if row else None
        

        classmethod
        def fetch_all(cls, rows):
            sql = '''
                SELECT * FROM doctors
        '''
            row = cursor.execute(sql).fetchall()
            # use of list comprehension to loop through the list and output a list containing python objects
            return [cls.instance_from_db(row) for row in rows] 