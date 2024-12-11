from langchain_core.prompts import ChatPromptTemplate

cv_generator_prompt_template = ChatPromptTemplate(
    [
        (
            "system",
            "You are a Human Resources expert and a helpful assistant. You help users to fine-tune their CV to increase their chance to be selected for the position.",
        ),
        (
            "user",
            """\
You are provided with a CV and a position description. The goal is to match user's CV with the position. Your task is to analyse user's profile, skills, experiences, education and tech-stack alongside the job description. Then you should professionally adjust user's CV based on the adjustment criteria mentioned bellow. You should also score the user's cv fitness to the position from 0 to 5 (where 0 means no match at all and 5 means the best match). You also provide comment on the area that the users need to focus to improve to get the position with bullet-points, considering their current CV to increase their chance to get the position.

### Adjustment Criteria 
- align the summary
- correct any dictation and grammatical mistakes
- increase the readability of the descriptions
- it is important to keep other experiments (carries, projects, and educations)
- order the skills based on the requirements
- highlight the keywords in the description in the LaTex format; Use the `textcolor` command with the color labeled as 'golden'. Each keyword should be enclosed within curly brackets immediately following the color designation, without spaces. 


User's name: {fullname}

### Position 
Title: {title}
Description: 
{description}
---
### User's CV
#### General Information
Skills:
```json
{skills}
```
Languages:
```json
{languages}
```
Hobbies:
```json
{hobbies}
```
Interests:
```json
{interests}
```
#### Carriers
```json
{carriers}
```
#### Projects
```json
{projects}
```
#### Educations
```json
{educations}
```
---
Here is the user's additional comment you might consider:
{additional}
""",
        ),
    ]
)
