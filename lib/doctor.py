from config import cursor, conn

class Doctor:
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
        