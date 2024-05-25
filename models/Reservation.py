class Reservation:
    def __init__(self, id, user_id, name, room_type, check_in, check_out):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.room_type = room_type
        self.check_in = check_in
        self.check_out = check_out

    @classmethod
    def add_reservation(cls, db, reservation):
        cursor = db.connection.cursor()
        sql = """INSERT INTO reservations (user_id, name, room_type, check_in, check_out) 
                 VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (reservation.user_id, reservation.name, reservation.room_type, reservation.check_in, reservation.check_out))
        db.connection.commit()
        cursor.close()
