# api/routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.schemas import LoginRequest, PatientRequest, UserCreate
from api.jwt_auth import require_role
from core.dependencies import get_predictor
from core.jwt_service import JWTService
from core.password_service import PasswordService
from core.inference import DiabetesPredictor
from db.dependencies import get_db
from db.models.service import get_user_by_email
from db.models.user import User
from services.prediction_service import PredictionService

# Содержит зарегистрированные эндпоинты
# APIRouter - это способ разделить маршруты по модулям
router = APIRouter()


# Корневой эндпоинт
@router.get("/", summary="Приветственное сообщение", tags=["Предсказание диабета"])
def root():
    return {"message": "ML Diabetes Prediction API"}


@router.post("/predict", summary="Отправка данных на проверку",
             tags=["Проверка показателей на диабет"])
def predict(
        data: PatientRequest,
        # pylint: disable=W0613 (unused-argument)
        user=Depends(require_role(["user", "admin"])),
        predictor: DiabetesPredictor = Depends(get_predictor),
        db: Session = Depends(get_db),
):
    service = PredictionService(predictor=predictor)

    prediction = service.predict_and_save(db=db, data=data)

    return {
        "id": prediction.id,
        "prediction": prediction.result
    }


@router.post("/register", summary="Регистрация пользователей")
def register(data: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(email=data.email, db=db)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    user = User(
        email=data.email,
        password_hash=PasswordService.hash_password(data.password),
        role="user",
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "User created"}


@router.post("/login", summary="Вход в приложение")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = get_user_by_email(email=data.email, db=db)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    if not PasswordService.verify_password(
            password=data.password,
            password_hash=user.password_hash,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    token = JWTService.create_access_token(
        {
            "sub": str(user.id),
            "role": user.role,
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user.role,
    }


@router.get("/admin/health")
def admin_health(
        # pylint: disable=W0613 (unused-argument)
        user=Depends(require_role(["admin"]))
):
    return {"status": "ok"}
