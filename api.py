import shutil
from typing import List
from fastapi import APIRouter, FastAPI, UploadFile, File, Form

from schemas import UploadUserFile, GetUserFile

file_router = APIRouter()

@file_router.post('/upload_file')
async def upload_file(title: str = Form(...), description: str = Form(...), file: UploadFile = File(...)):
    """Загрузка и сохранение файлов на сервер"""

    info = UploadUserFile(title=title, description=description)

    with open(f'{file.filename}', 'wb') as bufer:
        shutil.copyfileobj(file.file, bufer)

    return {'file_name': file.filename, 'info': info}


@file_router.post('/upload_files', status_code=201)
async def upload_files(files: List[UploadFile] = File(...)):
    """Загрузка и сохранение нескольких файлов на сервер"""
    
    for one_file in files:
        with open(f'{one_file.filename}', 'wb') as bufer:
            shutil.copyfileobj(one_file.file, bufer)

    return {'file_name': 'Good'}


@file_router.get('/file', response_model=GetUserFile)
async def get_file():
    user = {'id': 25, 'name': 'Pipec'}
    file = {'title': 'Test', 'description': 'Description'}
    return GetUserFile(user=user, file=file)
