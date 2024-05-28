from pydantic import BaseModel

class UserStory(BaseModel): 
    user_id: int
    story_id: int