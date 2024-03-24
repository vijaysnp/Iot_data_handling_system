
from pydantic import BaseModel, validator, Extra, EmailStr



class Mqttdataschema(BaseModel):
    city: str
    temperature: float
    email: EmailStr

    
    class Config:
        orm_mode = True
        extra = Extra.allow
        schema_extra = {"example":
                        {"city":'pune', 
                        "temperature": 38,
                        "email":'test@example.com'
                         }
                    }