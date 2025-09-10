from sqlalchemy import create_engine, text


db_connection_string = "postgresql://postgres:theylfrfrfz-nj12@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO users(\"user_id\", \"user_email\",\"subject_id\") VALUES (:new_id,:new_email,:new_subject)")
    connection.execute(sql, {"new_id": 1343, "new_email": "buuo@mail.ru", "new_subject": 1})

    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("UPDATE users SET user_id = :user, subject_id = :subject WHERE user_email = :email")
    connection.execute(sql, {"user": '123', "subject": '3', "email": 'buuo@mail.ru'})

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("DELETE FROM users WHERE user_email = :email")
    connection.execute(sql, {"email": 'buuo@mail.ru'})

    transaction.commit()
    connection.close()
