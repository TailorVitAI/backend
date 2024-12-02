import apps.main.models as MODELS
from apps.main.services.latex import CVTemplate, generate
import apps.main.services.llm.models as LLM_MODELS
from apps.main.services.llm.agent import agent_generate_cv, get_agent_generate_cv_meta


def generate_cv(tailor: MODELS.Tailor):
    experiences = MODELS.Experience.objects.filter(
        profile__user=tailor.profile.user,
    )
    carriers = [
        LLM_MODELS.ExperienceModel(
            title=exp.title,
            role=exp.role,
            location=exp.location,
            description=exp.description,
            url=exp.url,
            starting=exp.starting,
            ending=exp.ending,
        )
        for exp in experiences
        if exp.category == MODELS.Experience.Category.CARRIER
    ]
    educations = [
        LLM_MODELS.ExperienceModel(
            title=exp.title,
            role=exp.role,
            location=exp.location,
            description=exp.description,
            url=exp.url,
            starting=exp.starting,
            ending=exp.ending,
        )
        for exp in experiences
        if exp.category == MODELS.Experience.Category.EDUCATION
    ]
    projects = [
        LLM_MODELS.ExperienceModel(
            title=exp.title,
            role=exp.role,
            location=exp.location,
            description=exp.description,
            url=exp.url,
            starting=exp.starting,
            ending=exp.ending,
        )
        for exp in experiences
        if exp.category == MODELS.Experience.Category.PROJECT
    ]
    cv = LLM_MODELS.CVModel(
        summary="",
        title="",
        skills=tailor.profile.skills,
        hobbies=tailor.profile.hobbies,
        interests=tailor.profile.interests,
        languages=tailor.profile.languages,
        carriers=carriers,
        educations=educations,
        projects=projects,
    )

    position = LLM_MODELS.PositionModel(
        title=tailor.title,
        description=tailor.description,
    )

    response = agent_generate_cv(
        position=position,
        cv=cv,
        fullname=tailor.profile.user.full_name,
        additional=tailor.additional,
    )

    latex_content = generate(
        cv_template=CVTemplate.TEMPLATE_00,
        data={
            "full_name": tailor.profile.user.full_name,
            "profile": tailor.profile,
            "cv": response.cv,
        },
    )

    meta = get_agent_generate_cv_meta()
    meta["response"] = str(response)  # FIXME: save as json

    _ = MODELS.CurriculumVitae.objects.create(
        tailor=tailor,
        uri="xxx",
        fitness=response.fitness,
        comment=response.comment,
        content=latex_content,
        meta=meta,
    )

    return response
