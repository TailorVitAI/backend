from langchain_openai import ChatOpenAI

import apps.main.services.llm.models as MODELS
from apps.main.services.llm.prompts import cv_generator_prompt_template

MODEL_NAME = "gpt-4o-mini"
MODEL_TEMP = 0.1
PROMPT_VERSION = "P1.0"

model = ChatOpenAI(
    model=MODEL_NAME,
    temperature=MODEL_TEMP,
)


def get_agent_generate_cv_meta():
    return {
        "MODEL_NAME": MODEL_NAME,
        "MODEL_TEMP": MODEL_TEMP,
        "PROMPT_VERSION": PROMPT_VERSION,
    }


def agent_generate_cv(
    position: MODELS.PositionModel,
    cv: MODELS.CVModel,
    fullname: str,
    additional: str,
) -> MODELS.CVGeneratorModel:
    args = {
        "fullname": fullname,
        "additional": additional,
    }
    args = args | position.model_dump(mode="json")
    args = args | cv.model_dump(mode="json")

    messages = cv_generator_prompt_template.invoke(args)
    structured_model = model.with_structured_output(MODELS.CVGeneratorModel)
    response = structured_model.invoke(messages)

    return response
