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

    """
    Este endpoint retorna se a pessoa vai ao college ou não de acordo com os dados fornecidos.
 
    **Exemplo:**
    ```
    {
        "type_school": "Academic",
        "school_accreditation": A,
        "interest": "Less Interested",
        "gender": "Male",
        "residence": "Urban",
        "parent_was_in_college": false
    }
    ```
    """

    will_go_to_college = perform_prediction(item)
    return {
        'will_go_to_college': will_go_to_college
    }
