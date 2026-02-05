def authenticate_user(usuario, password):
    # Credenciales hardcodeadas
    valid_users = {
        "admin": "admin",
        "user": "password123"
    }
    
    return valid_users.get(usuario) == password

def is_user_authenticated(session):
    return "usuario" in session

def logout_user(session):
    session.clear()