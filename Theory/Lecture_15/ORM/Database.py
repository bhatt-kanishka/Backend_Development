from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import date

# Database setup
DATABASE_URL = "sqlite:///students.db"
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# ------------------------------------------------------------------------------
# Models with bidirectional relationships
# ------------------------------------------------------------------------------

class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    building = Column(String(50))
    
    students = relationship("Student", back_populates="department", cascade="all, delete-orphan")
    courses = relationship("Course", back_populates="department")
    faculties = relationship("Faculty", back_populates="department")

    def __repr__(self):
        return f"<Department: {self.name}>"


class Faculty(Base):
    __tablename__ = "faculties"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    designation = Column(String(50))
    department_id = Column(Integer, ForeignKey("departments.id"))
    
    department = relationship("Department", back_populates="faculties")
    courses = relationship("Course", back_populates="faculty")

    def __repr__(self):
        return f"<Faculty: {self.name} ({self.designation})>"


class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    branch = Column(String(50))
    enrollment_date = Column(Date)
    department_id = Column(Integer, ForeignKey("departments.id"))
    
    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Student: {self.name}, {self.branch}>"


class Course(Base):
    __tablename__ = "courses"
    
    id = Column(String(10), primary_key=True)
    title = Column(String(100), nullable=False)
    credits = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey("departments.id"))
    faculty_id = Column(Integer, ForeignKey("faculties.id"), nullable=True)
    
    department = relationship("Department", back_populates="courses")
    faculty = relationship("Faculty", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Course: {self.id} - {self.title}>"


class Enrollment(Base):
    __tablename__ = "enrollments"
    
    student_id = Column(Integer, ForeignKey("students.id"), primary_key=True)
    course_id = Column(String(10), ForeignKey("courses.id"), primary_key=True)
    semester = Column(String(20))
    grade = Column(String(2))
    
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

    def __repr__(self):
        return f"<Enrollment: Student {self.student_id} in {self.course_id}>"


def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Database tables created successfully.")


def run_crud():
    # 1. Create Department, Faculty, and Courses
    cs_dept = Department(name="Computer Science & Engineering", building="Block 9")
    session.add(cs_dept)
    session.commit()
    print(f"Created department: {cs_dept.name} successfully.")

    faculty = Faculty(name="Dr. Sharma", email="dr.sharma@upes.ac.in", designation="Associate Professor", department_id=cs_dept.id)
    session.add(faculty)
    session.commit()
    print(f"Created faculty: {faculty.name} ({faculty.designation}) successfully.")

    course1 = Course(id="CS101", title="Data Structures & Algorithms", credits=4, department_id=cs_dept.id, faculty_id=faculty.id)
    course2 = Course(id="CS102", title="Database Management Systems", credits=3, department_id=cs_dept.id, faculty_id=faculty.id)
    session.add_all([course1, course2])
    session.commit()
    print("Created courses CS101 and CS102 successfully.")

    # 2. Create Student with department assignment and enrollment
    new_student = Student(
        name="Aarav",
        email="aarav@upes.ac.in",
        branch="CSE",
        enrollment_date=date(2024, 8, 1),
        department_id=cs_dept.id
    )
    session.add(new_student)
    session.commit()
    print(f"Added student: {new_student.name} assigned to {cs_dept.name} successfully.")

    enrollment = Enrollment(student_id=new_student.id, course_id="CS101", semester="Semester 3", grade="A")
    session.add(enrollment)
    session.commit()
    print(f"Enrolled {new_student.name} in CS101 successfully.")

    student2 = Student(
        name="Priya",
        email="priya@upes.ac.in",
        branch="CSE",
        enrollment_date=date(2024, 8, 1),
        department_id=cs_dept.id
    )
    session.add(student2)
    session.commit()
    print(f"Added student: {student2.name} successfully.")

    # 3. Read Data
    cse_students = session.query(Student).filter(Student.branch == "CSE").all()
    student_by_id = session.query(Student).filter_by(id=new_student.id).first()
    print(f"Retrieved student by ID {new_student.id}: {student_by_id.name}")
    print(f"Retrieved CSE students: {[s.name for s in cse_students]}")

    # 4. Update
    if student_by_id:
        student_by_id.branch = "ECE"
        session.commit()
        print(f"Updated {student_by_id.name}'s branch to ECE successfully.")

    # 5. Delete & Cascade verification
    student_to_delete = session.query(Student).filter_by(name="Aarav").first()
    if student_to_delete:
        target_id = student_to_delete.id
        session.delete(student_to_delete)
        session.commit()
        
        # Verify enrollment cascade deletion
        remaining_enrollments = session.query(Enrollment).filter_by(student_id=target_id).all()
        if len(remaining_enrollments) == 0:
            print(f"Deleted student Aarav and verified cascade deletion of enrollments successfully.")
        else:
            print(f"Student deleted, but child enrollments remained.")


if __name__ == "__main__":
    init_db()
    run_crud()
