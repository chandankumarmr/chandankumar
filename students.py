from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
  conn = sqlite3.connect("students.db")
  cursor = conn.cursor()

  cursor.execute("""
      CREATE TABLE IF NOT EXISTS students(
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         name TEXT NOT NULL,
         email TEXT NOT NULL,
         course TEXT NOT NULL
      )
    """)

  conn.commit()
  conn.close()

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    name = data["name"]
    email = data["email"]
    course = data["course"]

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
       "INSERT INTO Students (name, email, course) VALUES(?, ?, ?)",
       (name, email, course)
    )

    conn.commit()
    student_id = cursor.lastrowid
    conn.close()

    return jsonify({
       "message": "Student added successfully",
       "id": student_id
   }), 201

@app.route("/students", methods=["GET"])
def get_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
   
    conn.close()

    students = []

    for row in rows:
        students.append({
           "id": row[0],
           "name": row[1],
           "email": row[2],
           "course": row[3]
        })

    return jsonify(students)

@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE_students
        SET name=?, email=?, course=?
        WHERE id=?
        """, (data["name"], data["email"], data["course"], id))

    conn.commit()
    conn.close()
 
    return jsonify({"mesage" : "Student updated sucessfully"})

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_students(id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=?", (id))

    conn.commit()
    conn.close()

    return jsonify({"messagwe": "Student deleted successfully"})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
    