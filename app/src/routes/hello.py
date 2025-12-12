from aws_lambda_powertools import Tracer
from aws_lambda_powertools.event_handler.router import APIGatewayHttpRouter

from custom_utils.sample import sample_func


tracer = Tracer("HELLO-WORLD")
router = APIGatewayHttpRouter()


@router.get("/api/hello")
@tracer.capture_method
def orchestrate_chat() -> str:
    sample_func()
    return "HELLO WORLD!"
