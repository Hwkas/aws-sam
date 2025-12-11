from typing import Any, Dict

from aws_lambda_powertools import Tracer
from aws_lambda_powertools.event_handler import APIGatewayHttpResolver
from aws_lambda_powertools.utilities.typing import LambdaContext

from routes import hello

tracer = Tracer()
app = APIGatewayHttpResolver(enable_validation=True)
app.include_router(hello.router)


@tracer.capture_lambda_handler
def lambda_handler(
    event: Dict[str, Any],
    context: LambdaContext,
) -> Dict[str, Any]:
    return app.resolve(event, context)
