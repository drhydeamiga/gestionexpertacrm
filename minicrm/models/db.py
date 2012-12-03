# -*- coding: utf-8 -*-
import datetime
#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

## if NOT running on Google App Engine use SQLite or other DB
db = DAL('sqlite://storage.sqlite')


## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth, filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)

mail.settings.server = settings.email_server
mail.settings.sender = settings.email_sender
mail.settings.login = settings.email_login





db.define_table('clientes',
    Field('name', 'string', length=128, notnull=True, requires=IS_NOT_EMPTY()),
    Field('fiscalname', 'string', length =128, notnull=True),
    Field('tax_identification', 'string', length =45, notnull=True, requires=IS_NOT_EMPTY()),
    Field('address', 'string', length =196, notnull=True, requires=IS_NOT_EMPTY()),
    Field('city', 'string', length =45, notnull=True, requires=IS_NOT_EMPTY()),
    Field('province', 'string', length =45, notnull=True, requires=IS_NOT_EMPTY()),
    Field('postal_code', 'string', length =10, notnull=True, requires=IS_NOT_EMPTY()),
    Field('phone', 'string', length=20),
    Field('fax', 'string', length=20),
    Field('email','string', length=128, requires=IS_EMAIL(error_message="email incorrecto")),
    Field('created_on','datetime',default=datetime.datetime.now()),
    migrate=True)

db.define_table('servicios',
    Field('name', 'string', length=128, notnull=True, requires=IS_NOT_EMPTY()),
    Field('descripcion','string', length=255, requires=IS_NOT_EMPTY()),
    Field('precio', 'float', requires=IS_NOT_EMPTY(), default=0),
    Field('duracion', 'integer', requires=IS_NOT_EMPTY()),
    Field('created_on','datetime',default=datetime.datetime.now()),
    migrate=True)

db.define_table('contratos',
    Field('cliente', db.clientes), 
    Field('fechainicio','datetime', requires=IS_NOT_EMPTY()),
    Field('duracion', 'integer', requires=IS_NOT_EMPTY()),
    migrate=True)

db.define_table('contrato_servicios',
    Field('contrato', db.contratos), 
    Field('servicio', db.servicios), 
    migrate=True)




