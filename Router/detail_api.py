from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from Database.db_connect import get_db
from Model.detail_table import Profile
from Schemas.details_schm import (
    ProfileCreate,
    ProfileUpdate,
    ProfileResponse,
)

from Repository.details_repo import (
    create_profile, fetch_all_profiles, get_profile_by_id, update_profile,
    delete_profile,
)

from utils.jwt_token_work import role_based_token



router = APIRouter()


#* ==================================================
# CREATE PROFILE
# Only Owner and admin can create worker profiles
#* ==================================================

owner_and_admin = Depends(role_based_token(["owner" , "admin"]))

@router.post("/",response_model=ProfileResponse,status_code=status.HTTP_201_CREATED,)

def profile_create(profile_data: ProfileCreate, db: Session = Depends(get_db) , _ = owner_and_admin):
    
    return create_profile(db, profile_data)


#* ==================================================
# GET ALL PROFILES
# Only Owner can view all worker profiles
#* ==================================================

@router.get("/", response_model=list[ProfileResponse])

def get_all_profiles(db: Session = Depends(get_db), _ = owner_and_admin):
    
    return fetch_all_profiles(db)


#* ==================================================
# GET PROFILE BY ID
# Only Owner can view a specific profile
#* ==================================================

@router.get("/{profile_id}",response_model=ProfileResponse)

def get_profile_id(
    profile_id: int,
    db: Session = Depends(get_db), _ = owner_and_admin):
    
    profile = get_profile_by_id(db, profile_id)

    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found",
        )

    return profile


#* ==================================================
# UPDATE PROFILE (PATCH)
# Only Owner and admin can update worker profiles
#* ==================================================

@router.patch("/{profile_id}",response_model=ProfileResponse)

def profile_update(
    profile_id: int, profile_data: ProfileUpdate, db: Session = Depends(get_db), _ = owner_and_admin):
    
    profile = update_profile(db, profile_id, profile_data)

    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found",
        )

    return profile


#* ==================================================
# DELETE PROFILE
# Only Owner and admin can delete worker profiles
#* ==================================================

@router.delete("/{profile_id}",response_model=ProfileResponse)

def profile_delete(
    profile_id: int,
    db: Session = Depends(get_db), _ = owner_and_admin):
    
    profile = delete_profile(db, profile_id)

    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found",
        )

    return profile