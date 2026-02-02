import pytest
from httpx import AsyncClient
from starter-code import app

@pytest.mark.asyncio
async def test_crud_flow():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Create
        r = await ac.post("/tasks", json={"title": "Test task", "description": "desc"})
        assert r.status_code == 201
        task = r.json()
        task_id = task["id"]

        # Read
        r = await ac.get(f"/tasks/{task_id}")
        assert r.status_code == 200
        assert r.json()["title"] == "Test task"

        # Update
        r = await ac.put(f"/tasks/{task_id}", json={"title": "Updated", "description": "x", "completed": True})
        assert r.status_code == 200
        assert r.json()["title"] == "Updated"

        # Delete
        r = await ac.delete(f"/tasks/{task_id}")
        assert r.status_code == 204

        # Confirm deletion
        r = await ac.get(f"/tasks/{task_id}")
        assert r.status_code == 404
