from fastapi import APIRouter, Query, HTTPException
from services.excel_service import get_all_tables, get_table_rows, get_row_sum

router = APIRouter()

@router.get("/list_tables")
def list_tables():
    try:
        return {"tables": get_all_tables()}
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_table_details")
def get_table_details(table_name: str = Query(...)):
    try:
        return get_table_rows(table_name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except (FileNotFoundError, RuntimeError) as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/row_sum")
def row_sum(table_name: str = Query(...), row_name: str = Query(...)):
    try:
        return get_row_sum(table_name, row_name)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except (FileNotFoundError, RuntimeError) as e:
        raise HTTPException(status_code=500, detail=str(e))
