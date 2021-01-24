import shutil
from typing import List
from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.post('/upload_file')
async def upload_file(file: UploadFile = File(...)):
    """Загрузка и сохранение файлов на сервер"""

    with open(f'{file.filename}', 'wb') as bufer:
        shutil.copyfileobj(file.file, bufer)

    return {'file_name': file.filename}


@app.post('/upload_files')
async def upload_files(files: List[UploadFile] = File(...)):
    """Загрузка и сохранение нескольких файлов на сервер"""
    
    for one_file in files:
        with open(f'{one_file.filename}', 'wb') as bufer:
            shutil.copyfileobj(one_file.file, bufer)

    return {'file_name': 'Good'}
