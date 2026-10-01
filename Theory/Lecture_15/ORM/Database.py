from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, CheckConstraint
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import date

# ==============================================================================
# Lecture 15: Data Modeling with SQLAlchemy ORM
# Topic: Student Management System Data Model & CRUD Operations
# ==============================================================================

# 1. Database Connection & Setup
DATABASE_URL = "sqlite:///students.db"
engine = create_engine(DATABASE_URL, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# ==============================================================================
# 2. ORM Models with Bidirectional Relationships (back_populates)
# ==============================================================================

class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    building = Column(String(50))
    
    # Bidirectional relationships
    students = relationship("Student", back_populates="department", cascade="all, delete-orphan")
    courses = relationship("Course", back_populates="department")
    faculties = relationship("Faculty", back_populates="department")

    def __repr__(self):
        return f"<Department(id={self.id}, name='{self.name}')>"


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
        return f"<Faculty(id={self.id}, name='{self.name}', designation='{self.designation}')>"


class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    branch = Column(String(50))
    enrollment_date = Column(Date)
    department_id = Column(Integer, ForeignKey("departments.id"))
    
    # Relationship to Department
    department = relationship("Department", back_populates="students")
    
    # Relationship to Enrollment with CASCADE DELETE
    # When a Student is deleted, all their enrollment records are also automatically deleted
    enrollments = relationship("Enrollment", back_populates="student", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', branch='{self.branch}', email='{self.email}')>"


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
        return f"<Course(id='{self.id}', title='{self.title}', credits={self.credits})>"


class Enrollment(Base):
    __tablename__ = "enrollments"
    
    student_id = Column(Integer, ForeignKey("students.id"), primary_key=True)
    course_id = Column(String(10), ForeignKey("courses.id"), primary_key=True)
    semester = Column(String(20))
    grade = Column(String(2))
    
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, course_id='{self.course_id}', semester='{self.semester}', grade='{self.grade}')>"


# ==============================================================================
# 3. Create Tables
# ==============================================================================
def init_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("[OK] Database tables created successfully.")


# ==============================================================================
# 4. CRUD Operations & Cascade Verification Demonstration
# ==============================================================================
def run_crud_demonstration():
    print("=" * 70)
    print("LECTURE 15: SQLALCHEMY CRUD OPERATIONS & CASCADE BEHAVIOR")
    print("=" * 70)

    # Clean existing demonstration records if present
    session.query(Enrollment).delete()
    session.query(Student).delete()
    session.query(Course).delete()
    session.query(Faculty).delete()
    session.query(Department).delete()
    session.commit()

    # --------------------------------------------------------------------------
    # Step 1: CREATE (Seeding Department, Faculty, and Course)
    # --------------------------------------------------------------------------
    print("\n--- 1. CREATE: Department & Course ---")
    cs_dept = Department(name="Computer Science & Engineering", building="Block 9")
    session.add(cs_dept)
    session.commit()
    print(f"Created Department: {cs_dept} (ID: {cs_dept.id})")

    faculty = Faculty(name="Dr. Sharma", email="dr.sharma@upes.ac.in", designation="Associate Professor", department_id=cs_dept.id)
    session.add(faculty)
    session.commit()
    print(f"Created Faculty: {faculty}")

    course_cs101 = Course(id="CS101", title="Data Structures & Algorithms", credits=4, department_id=cs_dept.id, faculty_id=faculty.id)
    course_cs102 = Course(id="CS102", title="Database Management Systems", credits=3, department_id=cs_dept.id, faculty_id=faculty.id)
    session.add_all([course_cs101, course_cs102])
    session.commit()
    print(f"Created Courses: {course_cs101}, {course_cs102}")

    # --------------------------------------------------------------------------
    # Step 2: CREATE: Student with Department Assignment & Enrollment
    # --------------------------------------------------------------------------
    print("\n--- 2. CREATE: Student with Department Assignment ---")
    new_student = Student(
        name="Aarav",
        email="aarav@upes.ac.in",
        branch="CSE",
        enrollment_date=date(2024, 8, 1),
        department_id=cs_dept.id
    )
    session.add(new_student)
    session.commit()
    print(f"Student added: {new_student} assigned to Department: '{new_student.department.name}'")

    # Add student enrollment in CS101
    enrollment = Enrollment(student_id=new_student.id, course_id="CS101", semester="Semester 3", grade="A")
    session.add(enrollment)
    session.commit()
    print(f"Enrolled {new_student.name} into CS101: {enrollment}")

    # Add a second student for branch queries
    student2 = Student(
        name="Priya",
        email="priya@upes.ac.in",
        branch="CSE",
        enrollment_date=date(2024, 8, 1),
        department_id=cs_dept.id
    )
    session.add(student2)
    session.commit()
    print(f"Student added: {student2}")

    # --------------------------------------------------------------------------
    # Step 3: READ: Retrieving Data (By branch and by ID)
    # --------------------------------------------------------------------------
    print("\n--- 3. READ: Retrieving Data ---")
    cse_students = session.query(Student).filter(Student.branch == "CSE").all()
    student_by_id = session.query(Student).filter_by(id=new_student.id).first()

    print(f"Retrieved student (ID {new_student.id}): {student_by_id.name if student_by_id else 'Not Found'}")
    print(f"Retrieved all CSE students: {[s.name for s in cse_students]}")
    print(f"Student '{student_by_id.name}' is enrolled in: {[e.course_id for e in student_by_id.enrollments]}")

    # --------------------------------------------------------------------------
    # Step 4: UPDATE: Modifying Data
    # --------------------------------------------------------------------------
    print("\n--- 4. UPDATE: Modifying Student Branch ---")
    if student_by_id:
        print(f"Current branch: {student_by_id.branch}")
        student_by_id.branch = "ECE"
        session.commit()
        
        # Verify update from database
        updated_student = session.query(Student).filter_by(id=new_student.id).first()
        print(f"Updated branch in DB: Student {updated_student.name} -> {updated_student.branch}")

    # --------------------------------------------------------------------------
    # Step 5: DELETE & CASCADE BEHAVIOR VERIFICATION
    # --------------------------------------------------------------------------
    print("\n--- 5. DELETE & CASCADE BEHAVIOR VERIFICATION ---")
    student_to_delete = session.query(Student).filter_by(name="Aarav").first()
    if student_to_delete:
        target_id = student_to_delete.id
        # Check enrollments before deletion
        enrollments_before = session.query(Enrollment).filter_by(student_id=target_id).all()
        print(f"Enrollments before student deletion for Student ID {target_id}: {enrollments_before}")

        # Delete student
        session.delete(student_to_delete)
        session.commit()
        print(f"Executed session.delete(student_to_delete) for '{student_to_delete.name}'.")

        # Verify student deletion
        check_student = session.query(Student).filter_by(id=target_id).first()
        print(f"Student exists in DB? {check_student is not None}")

        # Verify cascade deletion of enrollments
        enrollments_after = session.query(Enrollment).filter_by(student_id=target_id).all()
        print(f"Enrollments after student deletion for Student ID {target_id}: {enrollments_after}")
        
        if len(enrollments_after) == 0:
            print("[SUCCESS] Cascade verified: All child enrollment records were automatically removed!")
        else:
            print("[ERROR] Orphan enrollments still remain!")
    else:
        print("Student 'Aarav' not found for deletion.")

    print("\n" + "=" * 70)
    print("ALL LECTURE 15 SQLALCHEMY CRUD & CASCADE DEMONSTRATIONS COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    init_db()
    run_crud_demonstration()
