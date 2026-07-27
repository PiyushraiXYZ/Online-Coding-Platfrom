from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database import Base


# =========================
# Problems Table
# =========================

class Problem(Base):
    __tablename__ = "problems"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)

    description = Column(Text, nullable=False)

    difficulty = Column(String(20), nullable=False)

    sample_input = Column(Text)

    sample_output = Column(Text)

    test_cases = relationship(
        "TestCase",
        back_populates="problem",
        cascade="all, delete"
    )

    solutions = relationship(
        "Solution",
        back_populates="problem",
        cascade="all, delete"
    )

    submissions = relationship(
        "Submission",
        back_populates="problem",
        cascade="all, delete"
    )


# =========================
# Test Cases Table
# =========================

class TestCase(Base):
    __tablename__ = "test_cases"

    id = Column(Integer, primary_key=True, index=True)

    problem_id = Column(
        Integer,
        ForeignKey("problems.id"),
        nullable=False
    )

    input_data = Column(Text)

    expected_output = Column(Text)

    is_hidden = Column(
        Boolean,
        default=False
    )

    problem = relationship(
        "Problem",
        back_populates="test_cases"
    )


# =========================
# Solutions Table
# =========================

class Solution(Base):
    __tablename__ = "solutions"

    id = Column(Integer, primary_key=True)

    problem_id = Column(
        Integer,
        ForeignKey("problems.id"),
        nullable=False
    )

    language = Column(String(50))

    code = Column(Text)

    problem = relationship(
        "Problem",
        back_populates="solutions"
    )


# =========================
# User Submissions Table
# =========================

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)

    problem_id = Column(
        Integer,
        ForeignKey("problems.id"),
        nullable=False
    )

    language = Column(
        String(50),
        nullable=False
    )

    code = Column(
        Text,
        nullable=False
    )

    verdict = Column(String(50))

    score = Column(Integer)

    execution_time = Column(String(20))

    memory_used = Column(String(20))

    problem = relationship(
        "Problem",
        back_populates="submissions"
    )


# =========================
# Test Sessions Table
# =========================

class TestSession(Base):
    __tablename__ = "test_sessions"

    id = Column(Integer, primary_key=True, index=True)

    total_questions = Column(Integer, default=3)

    score = Column(Integer, default=0)

    questions = relationship(
        "TestSessionQuestion",
        back_populates="session",
        cascade="all, delete"
    )


# =========================
# Test Session Questions
# =========================

class TestSessionQuestion(Base):
    __tablename__ = "test_session_questions"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(
        Integer,
        ForeignKey("test_sessions.id"),
        nullable=False
    )

    problem_id = Column(
        Integer,
        ForeignKey("problems.id"),
        nullable=False
    )

    session = relationship(
        "TestSession",
        back_populates="questions"
    )

    problem = relationship(
        "Problem"
    )