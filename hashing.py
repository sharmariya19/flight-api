from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    @staticmethod
    def get_password_hash(plain_password):
        return pwd_context.hash(plain_password)
