from fastapi import APIRouter
from datetime import datetime
from app.models.predict_go_to_college import ResponsePredict, InputPredict
from app.logic.predict import perform_prediction

router = APIRouter(
    prefix='/predict',
    tags=['predict'],
    responses={400: {'description': 'Bad Request'}}
)


@router.post('', response_model=ResponsePredict)
def predict(item: InputPredict):

    will_go_to_college = perform_prediction(item)
    return {
        'will_go_to_college': will_go_to_college
    }
