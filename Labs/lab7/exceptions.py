class DatabaseConnectivityError(Exception):
    def __init__(self, message="Cannot connect to Database with given Parameters !") -> None:
        print(message)
        
        
class contactInsertionError(Exception):
    def __init__(self, message="Cannot insert new contact !") -> None:
        print(message)


 

# if __name__=="__main__":
#     try:
#         raise UserAlreadyExistsError 
#     except (AccountNotFoundError, UserAlreadyExistsError) as e:
#         pass