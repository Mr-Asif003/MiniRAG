import json
from langchain_core.documents import Document
from pathlib import Path


Data_File = Path(
    "E:/AiNativeEngineering/langchain_Gen_Ai/projects_langchain/MiniRAG/users.json"
)

def load_documents():
    with open(Data_File,'r',encoding='utf-8') as file:
        users=json.load(file)

    documents=[]

    for user in users:
         content = f"""
        User Name: {user.get("name", "")}
        Age: {user.get("age", "")}
        City: {user.get("city", "")}
        Skills: {", ".join(user.get("skills", []))}
        Education: {user.get("education", "")}
        Interests: {", ".join(user.get("interests", []))}
        """

         document=Document(
             page_content=content,
             metadata={
                 'user_id':user.get('id'),
                 'name':user.get('name')
             }
         )

         documents.append(document)
    return documents