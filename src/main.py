from fastapi import FastAPI, status
# from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def index():
    return {"status": "sucess", "message": "Hellow World!!"}
    # return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"status": "error", "message": "NotFound"})
