class User:
    def __init__(self,attrs={}) -> None:
        self.email = attrs.get("email")
        self.password = attrs.get("password") 
        
    def __str__(self) -> str:
        return f"Email = {self.email}, Passsword = {self.password}"