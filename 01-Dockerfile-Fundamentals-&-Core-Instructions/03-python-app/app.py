import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory store (resets on restart). Swap for a DB/Volume later
tasks = []
next_id = 1

@app.get("/")
def index():
    return jsonify(message="Todo API is running", docs="GET/POST /tasks, GET/PUT/DELETE /tasks/<id>")

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/tasks")
def list_tasks():
    return jsonify(tasks)

@app.post("/tasks")
def create_task():
    global next_id
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    if not title:
        return jsonify(error="'title' is required"), 400
    task = {"id": next_id, "title": title, "done": False}
    next_id += 1
    tasks.append(task)
    return jsonify(task), 201
 
 
@app.get("/tasks/<int:task_id>")
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify(error="task not found"), 404
    return jsonify(task)
 
 
@app.put("/tasks/<int:task_id>")
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify(error="task not found"), 404
    data = request.get_json(silent=True) or {}
    if "title" in data:
        task["title"] = str(data["title"]).strip()
    if "done" in data:
        task["done"] = bool(data["done"])
    return jsonify(task)
 
 
@app.delete("/tasks/<int:task_id>")
def delete_task(task_id):
    global tasks
    if not any(t["id"] == task_id for t in tasks):
        return jsonify(error="task not found"), 404
    tasks = [t for t in tasks if t["id"] != task_id]
    return "", 204
 
 
if __name__ == "__main__":
    # Config via environment variables -> easy to override in Docker
    port = int(os.getenv("PORT", "5000"))
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    # 0.0.0.0 is required so the app is reachable from outside a container
    app.run(host="0.0.0.0", port=port, debug=debug)
 
