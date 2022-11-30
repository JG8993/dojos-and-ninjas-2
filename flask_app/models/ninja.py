from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name= data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(dojo_id)s);"
        results = connectToMySQL('dojos_and_ninjas_schema_jg').query_db(query,data)
        return results

    @classmethod
    def getNinja(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema_jg').query_db(query,data)
        return cls(result[0])

    
    
    @classmethod
    def destroyNinja(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema_jg').query_db(query,data)

    @classmethod
    def updateNinja(cls, data):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s WHERE id= %(id)s;"
        return connectToMySQL('dojos_and_ninjas_schema_jg').query_db(query,data)