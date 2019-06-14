# Date: 02/27/2019
# Developer: Miromar J. Lima
# Description: Generate status query for nodes.

#Tests

# db = DAL("postgres://postgres:postgres@pgsql.jmenzen.com.br:5432/jmenzen", pool_size=10)
db = DAL("postgres://postgres:postgres@localhost:5432/jmenzen", pool_size=10)
# Server
# db = DAL("postgres://postgres:postgres@191.4.204.167:5432/intelligentfactory", pool_size=10)

migrate = True

db.define_table('email',
    Field('emailid', type='id'),
    Field('id', type='string', length=100),
    Field('email_title', type='string', length=100),
    Field('email_text', type='string', length=500),
    Field('email_dataset_id', type='integer'),
    Field('email_date', type='datetime'),
    Field('email_user_id', type='integer'),
    migrate=migrate)

db.define_table('email_feeling',
    Field('feelingid', type='id'),
    Field('id', type='string', length=100),
    Field('probability', type='integer'),
    Field('emailid', type='string', length=100),
    migrate=migrate)

db.define_table('feeling',
    Field('feelingid', type='id'),
    Field('feeling_name', type='string', length=100),
    Field('id', type='string', length=100),
    migrate=migrate)

db.define_table('sender_to',
    Field('id', type='string', length=100),
    #Field('emailid', type='id'),
    Field('email_to', type='string', length=100),
    migrate=migrate)

db.define_table('sender_email',
    Field('sender_emailid',    type='id'),
    Field('id', type='string', length=100),
    #Field('emailid', type='id'),
    Field('email_sender', type='string', length=100),
    migrate=migrate)


db.define_table('dataset_emails',
    Field('dataset_emailsid', type='id'),
    Field('dataset_emails', type='string', length=100),
    migrate=migrate)
