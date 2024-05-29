API_TOKEN=${GITLAB_ACCESS_TOKEN}
SOURCE_PROJECT_ID="460"
SOURCE_FILE="config%2Fmodel.avsc"
SOURCE_URL="https://gitlab.kmf.kz/api/v4/projects/${SOURCE_PROJECT_ID}/repository/files/${SOURCE_FILE}/raw?ref=dev"
AVRO_MODEL_FILE="models.avsc"
RESULT_FILE="result.txt"

get_model:
	@curl -s -H 'PRIVATE-TOKEN: ${API_TOKEN}' ${SOURCE_URL}

get_model_file:
	@curl -s -H 'PRIVATE-TOKEN: ${API_TOKEN}' ${SOURCE_URL} > ${AVRO_MODEL_FILE}

html: get_model_file
	@cat ${AVRO_MODEL_FILE} | python3 main.py --format=html > ${RESULT_FILE}

simple_grid: get_model_file
	@cat ${AVRO_MODEL_FILE} | python3 main.py --format=simple_grid > ${RESULT_FILE}
