class Contact:
    def __init__(self,attrs={}) -> None:
        self.id = attrs.get("id")
        self.name = attrs.get("name")
        self.mobileno = attrs.get("mobileno")
        self.city = attrs.get("city")
        self.profession = attrs.get("profession")
        self.user_id = attrs.get("user_id")
        
    def __str__(self) -> str:
        return f"Name = {self.name}, Mobile No. = {self.mobileno}, City = {self.city}, Profession = {self.profession}"