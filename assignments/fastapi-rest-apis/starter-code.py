from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Tasks API")

class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = ""
    completed: bool = False

# Simple in-memory storage
_tasks: List[Task] = []
_next_id = 1

@app.get("/tasks", response_model=List[Task])
def list_tasks():
    return _tasks

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for t in _tasks:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: Task):
    global _next_id
    task.id = _next_id
    _next_id += 1
    _tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    for idx, t in enumerate(_tasks):
        if t.id == task_id:
            updated = task.copy()
            updated.id = task_id
            _tasks[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for idx, t in enumerate(_tasks):
        if t.id == task_id:
            _tasks.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Task not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
