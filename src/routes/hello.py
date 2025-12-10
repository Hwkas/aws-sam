from aws_lambda_powertools import Tracer
from aws_lambda_powertools.event_handler.router import APIGatewayHttpRouter

tracer = Tracer("HELLO-WORLD")
router = APIGatewayHttpRouter()


@router.get("/api/hello")
@tracer.capture_method
def orchestrate_chat() -> str:
    return "HELLO WORLD!"
