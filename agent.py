from retriever import load_knowledge
from llm import call_llm

def placement_agent(resume, job_desc):
    knowledge = load_knowledge()

    prompt = f"""
You are a Placement AI Assistant.

Analyze the following resume and job description.

Resume:
{resume}

Job Description:
{job_desc}

Provide the output in EXACTLY this format:

STRENGTHS:
- ...

GAPS:
- ...

IMPROVEMENTS:
- ...

INTERVIEW QUESTIONS:
- Question 1
- Question 2
- Question 3

READINESS SCORE:
<number between 0 and 100 ONLY>

IMPORTANT:
- Do NOT write "/100"
- Do NOT add explanation after the number
- Output the number on a new line
"""
    return call_llm(prompt)