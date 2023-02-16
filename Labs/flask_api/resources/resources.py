from flask import request, Response, jsonify
from flask_restful import Resource
from database.models import Product 
from mongoengine.queryset.visitor import Q

class ProductApi(Resource):
    def get(self):
        buses=Product.objects().to_json()
        return Response(buses, mimetype="application/json", status=200)
    
    def post(self):
        body=request.get_json()
        #veh=Vehicle(**body).save()
        veh = Product(name=body["name"],price=body["price"], desc=body["desc"]).save()
        id=veh.id
        return {'id':str(id)},200

class ProductApiById(Resource):
    def get(self,id):
        try:
            veh=Product.objects.get(id=id).to_json()
            return Response(veh,mimetype="application/json",status=200)
        except:
            message = {
            "status code": 404,
            "message": "Product not found"
         }

            resp = jsonify(message)
            resp.status_code = 404
            return resp

    def put(self,id):
        try:
            body=request.get_json()
            Product.objects.get(id=id).update(**body)
            return {'id':str(id)},200
        except:
            message = {
            "status code": 404,
            "message": "Product not found"
         }

            resp = jsonify(message)
            resp.status_code = 404
            return resp


    def delete(self,id):
        try:
            Product.objects.get(id=id).delete()
        except:
            message = {
            "status code": 404,
            "message": "Product not found"
         }

            resp = jsonify(message)
            resp.status_code = 404
            return resp
class ProductLimit(Resource):
    def get(self, limit):
        if limit==0:
            return jsonify('Limit should be greate than 0')
        buses=Product.objects().limit(limit).to_json()
        return Response(buses, mimetype="application/json", status=200)


class ProductSearch(Resource):
    
    
    def get(self, name):
        try:
            product=Product.objects.get(name=name).to_json()
            return Response(product, mimetype="application/json", status=200)
        except Product.DoesNotExist:
            message = {
            "status code": 404,
            "message": "Product not found"
         }

            resp = jsonify(message)
            resp.status_code = 404
            return resp
            # return not_found()
 
           
        
            
            #  return jsonify("not found")

class ProductName(Resource):
    
    
    def put(self,name):
        try:
            body=request.get_json()
            Product.objects.get(name=name).update(**body)
            return {'id':str(id)},200
        except:
            message = {
            "status code": 404,
            "message": "Product not found"
         }

            resp = jsonify(message)
            resp.status_code = 404
            return resp
    def delete(self,name):
        try:
            Product.objects.get(name=name).delete()
        except:
            message = {
            "status code": 404,
            "message": "Product not found"
         }

            resp = jsonify(message)
            resp.status_code = 404
            return resp

class ProductFilter(Resource):
      def get(self, query):
        try:
            books = Product.objects(Q(name__icontains=query) | Q(desc__icontains=query))
            if not books or books==[]:
                message = {
                    "status code": 404,
                    "message": "Product not found"
                    }

                resp = jsonify(message)
                resp.status_code = 404
                return resp
            else:
                return jsonify(books)
        except:
            message = {
            "status code": 404,
            "message": "Product not found"
         }

            resp = jsonify(message)
            resp.status_code = 404
            return resp



# class ProductSearchByDesc(Resource):
#     def get(self, name):
#         product=Product.objects.get(name=name)
#         return Response(product.to_json(), mimetype="application/json", status=200)




# class searchContact(Resource):
#       def get(self,name):
#           contact=Contacts.objects.get(name=name)
#           return Response(contact.to_json(), mimetype="application/json", status=200)

