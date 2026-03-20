from pwdlib import PasswordHash


class Crypto:
    def __init__(self) -> None:
        self.password_hash: PasswordHash = PasswordHash.recommended()

    def encrypt(self, secret: str) -> str:
        return self.password_hash.hash(secret)

    def verify(self, secret: str, hashed: str) -> bool:
        return self.password_hash.verify(secret, hashed)
