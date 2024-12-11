import shutil
import apps.main.models as MODELS
from apps.main.services.latex import CVTemplate, generate, compile
import apps.main.services.llm.models as LLM_MODELS
from apps.main.services.llm.agent import agent_generate_cv, get_agent_generate_cv_meta
from django.core.files import File
from datetime import datetime


def generate_cv(tailor: MODELS.Tailor):
    experiences = MODELS.Experience.objects.filter(
        profile__user=tailor.profile.user,
    )
    carriers = [
        LLM_MODELS.ExperienceModel(
            title=exp.title,
            role=exp.role,
            type=exp.get_type_display(),
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
            type=exp.get_type_display(),
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
            type=exp.get_type_display(),
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

    cv_template = CVTemplate.TEMPLATE_00

    latex_content = generate(
        cv_template=cv_template,
        data={
            "full_name": tailor.profile.user.full_name,
            "profile": tailor.profile,
            "cv": response.cv,
        },
    )

    meta = get_agent_generate_cv_meta()
    meta["response"] = str(response)  # FIXME: save as json

    cv = MODELS.CurriculumVitae.objects.create(
        tailor=tailor,
        fitness=response.fitness,
        comment=response.comment,
        content=latex_content,
        meta=meta,
    )

    # Generate a unique filename based on CV id and timestamp
    filename = (
        f"cv_{tailor.profile.user.first_name}_"
        f"{tailor.profile.user.last_name}_"
        f"{datetime.now().strftime('%Y-%m-%d-%H-%M')}.pdf"
    )

    # Compile LaTeX content into a PDF file
    output_dir = "./output"  # FIXME: use temp
    compiled_file = compile(
        template=cv_template,
        content=latex_content,
        output_dir=output_dir,
    )

    # Check if the file was successfully created
    try:
        with open(compiled_file, "rb") as pdf_file:
            cv.file.save(filename, File(pdf_file), save=True)
        cv.save()

    finally:
        shutil.rmtree(output_dir)

    return response
