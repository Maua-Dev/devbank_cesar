from typing import Dict, Optional, List, Tuple
from app.entities.usuario import Usuario
from app.entities.trasacao import Transacao

class Usuario_repository:
    users: Dict[int, Usuario]

    def __init__(self):
        self.users = {}

    def create_user(self, user: Usuario, user_id: int) -> Usuario:
        
        self.users[user_id] = user
        return user

    def get_user(self, user_id: int) -> Optional[Usuario]:
        return self.users.get(user_id, None)