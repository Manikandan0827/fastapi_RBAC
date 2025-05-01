from fastapi import APIRouter, Depends, HTTPException, Security
from sqlmodel import Session, select
from models import Project
from schemas import ProjectCreate
from database import get_session
from dependencies import get_current_user, require_admin
from auth import oauth2_scheme  # import the oauth2_scheme defined in auth.py

router = APIRouter()

# Authenticated users (user/admin) can view projects
@router.get("/projects")
def get_projects(
    session: Session = Depends(get_session),
    token: str = Security(oauth2_scheme),
    user=Depends(get_current_user)
):
    return session.exec(select(Project)).all()

# Admin-only: create a project
@router.post("/projects")
def create_project(
    data: ProjectCreate,
    session: Session = Depends(get_session),
    token: str = Security(oauth2_scheme),
    admin=Depends(require_admin)
):
    project = Project(name=data.name, description=data.description)
    session.add(project)
    session.commit()
    session.refresh(project)
    return project

# Admin-only: update a project
@router.put("/projects/{project_id}")
def update_project(
    project_id: int,
    data: ProjectCreate,
    session: Session = Depends(get_session),
    token: str = Security(oauth2_scheme),
    admin=Depends(require_admin)
):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    project.name = data.name
    project.description = data.description
    session.add(project)
    session.commit()
    return {"message": "updated successfully"}

# Admin-only: delete a project
@router.delete("/projects/{project_id}")
def delete_project(
    project_id: int,
    session: Session = Depends(get_session),
    token: str = Security(oauth2_scheme),
    admin=Depends(require_admin)
):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    session.delete(project)
    session.commit()
    return {"detail": "Project deleted"}
