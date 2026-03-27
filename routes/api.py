from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Task
from schemas import TaskBase, TaskResponse, TaskCreate
from auth import get_current_user
from typing import List

router = APIRouter()

@router.get("/tasks/", response_model=List[TaskResponse])
def read_tasks(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    tasks = db.query(Task).filter(Task.owner_id == current_user.id).all()
    return tasks

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def read_task(task_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id).filter(Task.owner_id == current_user.id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task

@router.post("/tasks/", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_task = Task(title=task.title, description=task.description, state=task.state, deadline=task.deadline, owner_id=current_user.id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id).filter(Task.owner_id == current_user.id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    db.delete(task)
    db.commit()
    return {"message": "Tarea eliminada"}