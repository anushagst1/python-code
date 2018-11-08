from mongoengine import connect,DynamicDocument
from mongoengine.fields import *
import datetime
#import config
from mongoengine import Document, EmbeddedDocument, StringField, DateTimeField, EmbeddedDocumentField, ListField
from werkzeug.security import  check_password_hash,generate_password_hash
from flask import Flask, request, url_for, redirect, render_template, abort , Response,session,jsonify,flash,send_file

app = Flask(__name__)
app.secret_key = 'secret'

connect(host='localhost', port=27017, username='', password='')

class UserSignup(DynamicDocument):
     username = StringField()
     email = EmailField()
     mobile = StringField()
     password = StringField()
     usertype = StringField()
     registered_on = DateTimeField( "Date",format="%Y-%m-%d",default=datetime.date.today())
     status = StringField(default='Inactive')
     userid = StringField(default='None')
     def is_authenticated(self):
        return True

     def is_active(self):
        return True

     def is_anonymous(self): 
        return False

     def get_id(self):
          
        return unicode(self.id)

     def __repr__(self):
        return '<User %r>' % (self.username)

class Info(EmbeddedDocument):
     name = StringField()
     email = EmailField()
class Anusha(DynamicDocument):
     sno = StringField()
     details = ListField(EmbeddedDocumentField(Info))

     
@app.route('/createadmin', methods = ['GET', 'POST','PUT'])
def createAdmin():
    
        createUser = UserSignup(username="admin", email="admin@gmail.com", mobile="9812345678", password =generate_password_hash("Admin#123"),usertype="Admin")
        createUser.save()
        return "Admin created successfully."

@app.route('/anu', methods = ['GET', 'POST','PUT'])
def anu():
    
        createUser = Anusha(sno="1")
        #createUser.save()
        data=Info(name='anusha',email='anu@gmail.com')
        createUser.details.append(data)
        createUser.save()
        return "successfully."
@app.route('/sairam')
def sairam():
     for a in Anusha.objects(details__match={ "name": "anusha", "email": "anu@gmail.com" }):
          return 'success'
          
     return 'fail'



if __name__ == '__main__':
    app.run(host="127.0.0.1",port=80)




