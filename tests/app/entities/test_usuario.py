import pytest
from src.app.errors.entity_errors import ParamNotValidated
from src.app.entities.usuario import Usuario

class Test_Usuario:
    def test_usuario(self):
        usuario = Usuario("test", "0000" ,"00000-0", 2000)
        assert usuario.name == "test"
        assert usuario.agency == "0000"
        assert usuario.current_balance == 2000