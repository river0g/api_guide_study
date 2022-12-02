from fastapi import Request, Response
from fastapi import APIRouter
from jsonrpcserver import Success, Result, dispatch, method
from pydantic import BaseModel
from typing import Optional, List


""" description
title: WebAPIのレベルを理解する。
description: rpc(json-rpc)と他のwebapiについて理解する。
"""

router = APIRouter()


class Body(BaseModel):
    method: str
    params: Optional[str]  # e.g) param1,param2


def add(*params):
    curr = 0
    for param in params:
        curr += int(param)

    return curr


def multiple(*params):
    curr = 1
    for param in params:
        curr *= int(param)

    return curr


def echo5():
    return "5"


@router.post("/lesson1/rpc")
async def rpc(data: Body):
    res = 0
    try:
        method = data.method
        params = data.params

        if params:
            res = eval(f"{method}({params})")
        else:
            res = eval(f"{method}()")
    except Exception as e:
        return {"msg": str(e)}

    return {"msg": "success", "res": res}


class JsonRPCBody(BaseModel):
    jsonrpc: str
    method: str
    # params: Optional[List[str]]
    id: str


class JsonRPCBody1(BaseModel):
    jsonrpc: str
    method: str
    params: Optional[List[str]]
    id: str


@method  # jsonrpc
def add_10(*params) -> Result:
    curr = 0
    for param in params:
        curr += int(param)

    return Success(curr)


@router.post("/lesson1/jsonrpc")
async def jsonrpc(request: Request, data: JsonRPCBody1):
    return Response(dispatch(await request.body()))


@method
def ping() -> Result:
    return Success("pong")


@router.post("/lesson1/jsonrpc1")
async def index(request: Request, data: JsonRPCBody):
    return Response(dispatch(await request.body()))


if __name__ == "__main__":
    uvicorn.run(app, port=5000)
