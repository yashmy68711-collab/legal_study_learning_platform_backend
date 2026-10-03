from datetime import datetime, timedelta, timezone

from passlib.context import CryptContext
from jose import jwt, JWTError, ExpiredSignatureError

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


# ============================================================
# PASSWORD HASHING
# ============================================================

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# ============================================================
# JWT SETTINGS
# ============================================================

SECRET_KEY = "change-this-secret-key-for-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


# ============================================================
# CREATE ACCESS TOKEN
# ============================================================

def create_access_token(data: dict) -> str:

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


# ============================================================
# AUTHENTICATION
# ============================================================

security = HTTPBearer()


def verify_access_token(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

        return payload

    except ExpiredSignatureError:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired"
        )

    except JWTError:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )