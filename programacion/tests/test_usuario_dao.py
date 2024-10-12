import pytest
from unittest.mock import MagicMock, patch
from programacion.dao.usuario_dao import UsuarioDAO  # Asegúrate de que el nombre del archivo sea correcto
import mysql.connector

# Prueba de login exitoso
def test_login_exitoso():
    dao = UsuarioDAO()

    # Simulamos una respuesta exitosa de la base de datos
    dao.connection.cursor = MagicMock(return_value=MagicMock())
    dao.connection.cursor().fetchone = MagicMock(return_value=(1, "Juan", "Pérez", "juan@example.com", "password"))

    with patch('builtins.input', side_effect=["juan@example.com", "password"]):
        user = dao.login()

    assert user is not None
    assert user[1] == "Juan"
    assert user[2] == "Pérez"

# Prueba de login fallido con 3 intentos
def test_login_fallido():
    dao = UsuarioDAO()

    # Simulamos una respuesta fallida de la base de datos (usuario no encontrado)
    dao.connection.cursor = MagicMock(return_value=MagicMock())
    dao.connection.cursor().fetchone = MagicMock(return_value=None)

    with patch('builtins.input', side_effect=["juan@example.com", "wrongpassword", "juan@example.com", "wrongpassword", "juan@example.com", "wrongpassword"]):
        with pytest.raises(SystemExit):  # Esperamos que la aplicación se cierre después de 3 intentos fallidos
            dao.login()

# Prueba de registro de usuario exitoso
def test_registrar_usuario_exitoso():
    dao = UsuarioDAO()

    # Simulamos la inserción exitosa de un usuario
    dao.connection.cursor = MagicMock(return_value=MagicMock())
    dao.connection.commit = MagicMock()

    with patch('builtins.input', side_effect=["Juan", "Pérez", "juan@example.com", "password"]):
        dao.registrar_usuario()

    dao.connection.cursor().execute.assert_called_once()
    dao.connection.commit.assert_called_once()

# Prueba de recuperación de contraseña exitosa
def test_recuperar_contrasena_exitoso():
    dao = UsuarioDAO()

    # Simulamos que la contraseña fue encontrada en la base de datos
    dao.connection.cursor = MagicMock(return_value=MagicMock())
    dao.connection.cursor().fetchone = MagicMock(return_value=("password",))

    with patch('builtins.input', side_effect=["juan@example.com"]):
        dao.recuperar_contrasena()

    dao.connection.cursor().execute.assert_called_once_with("SELECT Contrasena FROM Usuario WHERE Email = %s", ("juan@example.com",))

# Prueba de recuperación de contraseña fallida
def test_recuperar_contrasena_fallido():
    dao = UsuarioDAO()

    # Simulamos que la contraseña no fue encontrada en la base de datos
    dao.connection.cursor = MagicMock(return_value=MagicMock())
    dao.connection.cursor().fetchone = MagicMock(return_value=None)

    with patch('builtins.input', side_effect=["juan@example.com", "juan@example.com", "juan@example.com"]):
        with pytest.raises(SystemExit):  # Esperamos que la aplicación se cierre después de 3 intentos fallidos
            dao.recuperar_contrasena()
