import os

def load_knowledge():
    kb_path = "knowledge_base"
    knowledge = ""

    for file in os.listdir(kb_path):
        with open(os.path.join(kb_path, file), "r", encoding="utf-8") as f:
            knowledge += f.read() + "\n\n"

    return knowledge