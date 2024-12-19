from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.nlp.analyzer import KeywordAnalyzer
from src.database.models import KeywordResult

router = APIRouter()

class KeywordRequest(BaseModel):
    text: str

@router.post("/analyze-keywords", response_model=KeywordResult)
async def analyze_keywords(request: KeywordRequest):
    try:
        analyzer = KeywordAnalyzer()
        keywords = analyzer.generate_keywords(request.text)
        result = KeywordResult(keywords=keywords)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))