from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Text, DateTime
from sqlalchemy.orm import relationship
from auth import User
from datetime import datetime

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    state = Column(String)
    deadline = Column(DateTime)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="tasks")

    def __repr__(self):
        return f'Task {self.title}'

class TaskHistory(Base):
    __tablename__ = 'task_history'
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey('tasks.id'))
    task = relationship("Task", back_populates="history")
    state = Column(String)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'TaskHistory {self.task_id}'

User.tasks = relationship("Task", back_populates="owner")
Task.history = relationship("TaskHistory", back_populates="task")