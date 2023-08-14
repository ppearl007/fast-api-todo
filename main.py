from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

#get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

#get single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "No todos found"}

#create a todo
@app.post("/todos")
async def create_todo(todo: Todo):
    todos.append(todo)
    return {"todos": todos}
    # return {"message": "todo created"}


#delete a todo
@app.delete("/todos/{todo_id}")
async def del_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"todos": todos}
    return {"message": "todo not found"}

#update a todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, new_todo: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.item = new_todo.item
            return {"todos": todos}
    return {"message": "no todo found to update"}