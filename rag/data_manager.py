import json
from pathlib import Path

Data_File = Path(
    "E:/AiNativeEngineering/langchain_Gen_Ai/projects_langchain/MiniRAG/users.json"
)

def load_users():

    if not Data_File.exists():
        return []
    
    with open(Data_File, "r", encoding="utf-8") as file:
        data = json.load(file)

   
    return data



def save_user(user):
    users=load_users()
    user['id']=len(users)+1
    users.append(user)

    with open(Data_File,'w',encoding='utf-8') as file:
        json.dump(users,file,indent=4)

    return user