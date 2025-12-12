format:
	ruff check --select I --fix --config ruff.toml && \
		ruff format --config ruff.toml

validate-local:
	sam validate -t sam-template.yaml --lint

validate-deployment:
	sam validate --lint

# run-sam:
# 	sam build -t template.yaml --use-container && \
# 		sam local start-api \
# 			-t .aws-sam/build/template.yaml \
# 			--env-vars .env.local.json \
# 			--port 3000 \
# 			--docker-network local-dev-network

run-sam:
	sam build -t template.yaml --use-container && \
		sam local start-api \
			-t .aws-sam/build/template.yaml \
			--port 3000 \

clear-docker:
	docker system prune -a --volumes -f