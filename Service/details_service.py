from fastapi import FastAPI , HTTPException , status

from Schemas.details_schm import ProfileCreate , ProfileUpdate , ProfileResponse

from Repository.details_repo import (
    create_profile , get_all_profiles , get_profile_by_id , update_profile , delete_profile) 


