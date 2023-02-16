from .resources import  ProductApi, ProductApiById, ProductLimit, ProductSearch, ProductFilter, ProductName

def initialize_routes(api):
    api.add_resource(ProductApi, '/api/products')
    # api.add_resource(Test, "/api/test")
    api.add_resource(ProductApiById, "/api/products/<id>")
    api.add_resource(ProductLimit, "/api/product/<int:limit>")
    # api.add_resource(ProductSearch, "/api/product/<name>")
    api.add_resource(ProductFilter, "/api/produc/<query>")
    api.add_resource(ProductName, "/api/prod/<name>")
    # api.add_resource(ProductSearchByDesc, "/api/products/<desc>")
    # api.add_resource(ContactsAPI, "/api/contacts")
    # api.add_resource(ContactCRUDAPI,"/api/contacts/<id>")
    # api.add_resource(searchContact,"/api/searchcontacts/<name>")
    #api.add_resource(Hello, '/api/')
    #api.add_resource(Square, '/square/<int:num>')