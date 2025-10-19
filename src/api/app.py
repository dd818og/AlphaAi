# FastAPI stub for wallet management and agent interfaces
from fastapi import FastAPI
app = FastAPI()
@app.get('/health')
def health():
    return {'status':'ok'}
@app.get('/wallets')
def list_wallets():
    return []
