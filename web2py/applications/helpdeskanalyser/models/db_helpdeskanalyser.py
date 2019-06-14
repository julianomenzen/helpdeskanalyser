# Date: 02/27/2019
# Developer: Miromar J. Lima
# Description: Generate status query for nodes.

#Tests

db = DAL("postgres://postgres:postgres@pgsql.jmenzen.com.br:5432/jmenzen", pool_size=10)

# Server
# db = DAL("postgres://postgres:postgres@191.4.204.167:5432/intelligentfactory", pool_size=10)

migrate = True

db.define_table('statusnode',
    Field('statusnodeid', type='id'),
    Field('description', type='string', length=200, label = 'Detailed description to identify the status of the node, according to the events.',  requires = IS_UPPER()),
    migrate=migrate)
'''
db.define_table('devicegroup',
    Field('devicegroupid', type='id'),
    Field('name', type='string', length=100, unique=True,  label='Description Group', requires = IS_UPPER()),
    migrate=migrate)

db.define_table('devicetype',
    Field('devicetypeid', type='id'),
    Field('description', type='string', length=100,  label='Description Type', requires = IS_UPPER()),
    migrate=migrate)

db.define_table('serialnumber',
    Field('serialnumberid', type='id'),
    Field('serialnumber', type='string', length=100, unique=True,  label='Description Serial Number', requires = IS_UPPER()),
    migrate=migrate)

db.define_table('device',
    Field('deviceid', type='id'),
    Field('devicegroupid', type='reference devicegroup', requires = IS_IN_DB(db, db.devicegroup.devicegroupid, '%(name)s')),
    Field('devicetypeid', type='reference devicetype', requires = IS_IN_DB(db, db.devicetype.devicetypeid, '%(description)s')),
    Field('serialnumberid', type='reference serialnumber', unique=True, requires = IS_IN_DB(db, db.serialnumber.serialnumberid, '%(serialnumber)s')),
    Field('description', type='string', length=100, label='Description Device', requires = IS_UPPER()),
    Field('name', type='string', length=100, label='Name Device', requires = IS_UPPER()),
    Field('active', type='boolean'),
    Field('applied', type='boolean'),
    migrate=migrate)

db.define_table('location',
    Field('locationid', type='id'),
    Field('description', type='string', length=200, label='Description Location', requires = IS_UPPER()),
    Field('locationimage', 'upload'),
    migrate=migrate)


db.define_table('device_location',
    Field('deviceid', type='reference device', requires = IS_IN_DB(db, db.device.deviceid, '%(description)s')),
    Field('locationid', type='reference location', requires = IS_IN_DB(db, db.location.locationid, '%(description)s')),
    Field('active', type='boolean'),
    Field('device_locationid', type='id', unique=True),
    Field('change_date', type='datetime', default=request.now),
    primarykey=['locationid', 'deviceid'],
    migrate=migrate)

db.define_table('eventdata',
    Field('eventdataid', type='id'),
    Field('logicalsensorid', type='reference logicalsensor'),
    Field('hubeventid', type='reference hubevent'),
    Field('status', type='integer'),
    Field('timestampdata', type='datetime'),
    Field('measure', type='double'),
    migrate=migrate)


db.define_table('hub',
    Field('hubid', type='id'),
    Field('name', type='string', length=40, unique=True, label='Name HUB', requires=IS_IN_SET(('HUB0','HUB01','HUB02','HUB03','HUB04','HUB05','HUB06','HUB07','HUB08','HUB09','HUB10','HUB11','HUB12','HUB13','HUB14','HUB15','HUB16','HUB17','HUB18','HUB19','HUB20','HUB21','HUB22','HUB23','HUB24','HUB25','HUB26','HUB27','HUB28','HUB29','HUB30','HUB31','HUB32','HUB33','HUB34','HUB35','HUB36','HUB37','HUB38','HUB39','HUB40','HUB41','HUB42','HUB43','HUB44','HUB45','HUB46','HUB47','HUB48','HUB49','HUB50'))),
    Field('description', type='string', length=200, requires = IS_UPPER()),
    migrate=migrate)


db.define_table('hubevent',
    Field('hubeventid', type='id'),
    Field('hubid', type='reference hub_operation_node.operationid'),
    Field('operationid', type='reference hub_operation_node.hubid'),
    Field('nodeid', type='reference hub_operation_node.nodeid'),
    Field('stringdata', type='string', length=240),
    Field('timestampevent', type='datetime'),
    migrate=migrate)

db.define_table('rfboard',
    Field('rfboardid', type='id'),
    Field('deviceid', type='reference device', requires = IS_IN_DB(db, db.device.deviceid, '%(description)s')),
    Field('mqttclientembedded', type='boolean'),
    Field('lastdateconfig', type='date'),
    Field('firmwareversion', type='string', length=40, requires = IS_UPPER()),
    Field('specification', type='string', length=100, requires = IS_UPPER()),
    migrate=migrate)

db.define_table('minipcgroup',
    Field('minipcgroupid', type='id'),
    Field('name', type='string', length=100, unique=True, requires = IS_UPPER()),
    migrate=migrate)

db.define_table('minipc',
    Field('minipcid', type='id'),
    Field('serialnumberid', type='reference serialnumber', requires = IS_IN_DB(db, db.serialnumber.serialnumberid, '%(serialnumber)s')),
    Field('rfboardid', type='reference rfboard', requires = IS_IN_DB(db, db.rfboard.rfboardid, '%(specification)s')),
    Field('minipcgroupid', type='reference minipcgroup', requires = IS_IN_DB(db, db.minipcgroup.minipcgroupid, '%(name)s')),
    Field('description', type='string', length=100, requires = IS_UPPER()),
    Field('processor', type='string', length=100, requires = IS_UPPER()),
    Field('hd', type='string', length=100, requires = IS_UPPER()),
    Field('motherboard', type='string', length=100, requires = IS_UPPER()),
    Field('memory', type='string', length=100),
    Field('minipcname', type='string', length=100),
    Field('active', type='boolean'),
    Field('applied', type='boolean'),
    migrate=migrate)

db.define_table('hub_minipc',
    Field('hub_minipcid', type='id', unique=True),
    Field('minipcid', type='reference minipc', label='Mini PC', requires = IS_IN_DB(db, db.minipc.minipcid, '%(description)s')),
    Field('hubid', type='reference hub', label='HUB', requires = IS_IN_DB(db, db.hub.hubid, '%(name)s')),
    Field('locationid', type='reference location', label='Location', requires = IS_IN_DB(db, db.location.locationid, '%(description)s')),
    primarykey=['minipcid', 'hubid'],
    migrate=migrate)

db.define_table('operation',
    Field('operationid', type='id'),
    Field('name', type='string', label='Name Operation', length=40, unique=True, requires=IS_IN_SET(('CONFIG','CONTROL','DATA','STATUS'))),
    Field('description', type='string', length=200, requires = IS_UPPER()),
    migrate=migrate)


db.define_table('node',
    Field('nodeid', type='id'),
    Field('name', type='string', length=40, unique=True, label='Name Node',requires=IS_IN_SET(('NODE0', 'NODE01','NODE02','NODE03','NODE04','NODE05','NODE06','NODE07','NODE08','NODE09','NODE10','NODE11','NODE12','NODE13','NODE14','NODE15','NODE16','NODE17','NODE18','NODE19','NODE20','NODE21','NODE22','NODE23','NODE24','NODE25','NODE26','NODE27','NODE28','NODE29','NODE30','NODE31','NODE32','NODE33','NODE34','NODE35','NODE36','NODE37','NODE38','NODE39','NODE40','NODE41','NODE42','NODE43','NODE44','NODE45','NODE46','NODE47','NODE48','NODE49','NODE50'))),
    Field('description', type='string', length=200, requires = IS_UPPER()),
    Field('maxdelay', type='integer'),
    Field('connected', type='boolean',  default = False, writable=False),
    migrate=migrate)

db.define_table('hub_operation_node',
    Field('hub_operation_nodeid', type='id'),
    Field('hubid', type='reference hub', requires = IS_IN_DB(db, db.hub.hubid, '%(name)s')),
    Field('operationid', type='reference operation', requires = IS_IN_DB(db, db.operation.operationid, '%(name)s')),
    Field('nodeid', type='reference node', requires = IS_IN_DB(db, db.node.nodeid, '%(name)s')),
    Field('topichub', type='string', length=240, requires = IS_UPPER()),
    Field('topicmultilevel', type='string', length=240, requires = IS_UPPER()),
    primarykey=['hubid', 'operationid', 'nodeid'],
    migrate=migrate)

db.define_table('integratedboardgroup',
    Field('intboardgroupid', type='id'),
    Field('name', type='string', length=100, unique=True, label='Integrated Board Group Name', requires = IS_UPPER()),
    migrate=migrate)


db.define_table('integratedboard',
    Field('intboardid', type='id'),
    Field('serialnumberid', type='reference serialnumber', requires = IS_IN_DB(db, db.serialnumber.serialnumberid, '%(serialnumber)s')),
    Field('intboardgroupid', type='reference integratedboardgroup', requires = IS_IN_DB(db, db.integratedboardgroup.intboardgroupid, '%(name)s')),
    Field('rfboardid', type='reference rfboard', requires = IS_IN_DB(db, db.rfboard.rfboardid, '%(specification)s')),
    Field('description', type='string', length=100, label='Description Integrated Board'),
    Field('active', type='boolean'),
    Field('applied', type='boolean'),
    migrate=migrate)


# definition of temp
#db.define_table('temp',
#                Field('id_temp', db.parameters),
#                Field('id_temp', type='reference parameters'),
#                )

db.define_table('measurement',
    Field('measurementid', type='id'),
    Field('name', type='string', length=10, label='Name Meas.', requires = IS_UPPER()),
    Field('description', type='string', length=100, label='Desc. Meas.', requires = IS_UPPER()),
    migrate=migrate)


db.define_table('parameters',
    Field('parametersid', type='id'),
    Field('maxlimitma', type='double'),
    Field('minlimitma', type='double'),
    Field('portgain', type='double'),
    Field('portoffset', type='double'),
    Field('locationimage', 'upload'),
    migrate=migrate)

#Variables for Initial Parameters
varPortOffest = 0.0
varMaxlimitma = 0.0
varMinlimitma = 0.0
varPortgain = 0.0
if ( db(db.parameters).count() > 0):
    row = db().select(db.parameters.ALL).first()
    varPortOffest = row.portoffset
    varMaxlimitma = row.maxlimitma
    varMinlimitma = row.minlimitma
    varPortgain = row.portgain


db.define_table('logicalsensor',
    Field('logicalsensorid', type='id'),
    Field('deviceid', type='reference device', label='Device', requires = IS_IN_DB(db, db.device.deviceid, '%(description)s')),
    Field('measurementid', type='reference measurement', label='Measurement', requires = IS_IN_DB(db, db.measurement.measurementid, '%(description)s')),
    Field('intboardid', type='reference integratedboard', label='Integrated Board', requires = IS_IN_DB(db, db.integratedboard.intboardid, '%(description)s')),
    Field('channel', type='integer', requires=IS_INT_IN_RANGE(1, 15)),
    Field('threshold', type='string', length=10),
    Field('portoffset', type='double', default = varPortOffest),
    Field('portgain', type='double', default = varPortgain),
    Field('maxmeasuresensor', type='double',  requires = IS_NOT_EMPTY()),
    Field('minmeasuresensor', type='double', requires = IS_NOT_EMPTY()),
    Field('maxlimitma', type='double', default = varMaxlimitma),
    Field('minlimitma', type='double', default = varMinlimitma),
    Field('connected', type='boolean', default = False, writable = False),
    Field('application', type='string', length=100, default = 'REPORT AN APPLICATION', requires = IS_UPPER()),
    migrate=migrate)

db.define_table('nodeevent',
    Field('nodeeventid', type='id'),
    Field('userid', type='integer'),
    Field('operationid', type='reference node_operation_hub.operationid'),
    Field('nodeid', type='reference node_operation_hub.nodeid'),
    Field('stringconfig', type='string', length=240),
    Field('hubid', type='reference node_operation_hub.hubid'),
    migrate=migrate)

db.define_table('node_integratedboard',
    Field('node_integratedboardid', type='id'),
    Field('intboardid', type='reference integratedboard', label='Integrated Board',requires = IS_IN_DB(db, db.integratedboard.intboardid, '%(description)s')),
    Field('nodeid', type='reference node', label='Node',requires = IS_IN_DB(db, db.node.nodeid, '%(name)s')),
    Field('locationid', type='reference location', requires = IS_IN_DB(db, db.location.locationid, '%(description)s')),
    Field('statusnodeid', type='statusnode', default = 0, writable=True),
    primarykey=['intboardid', 'nodeid'],
    migrate=migrate)
#db.node_integratedboard.boardstatus.requires = [IS_NOT_IN_DB(db, True)]

db.define_table('node_operation_hub',
    Field('node_operation_hubid', type='id'),
    Field('nodeid', type='reference node', label='Node',requires = IS_IN_DB(db, db.node.nodeid, '%(name)s')),
    Field('operationid', type='reference operation', label='Operation',requires = IS_IN_DB(db, db.operation.operationid, '%(name)s')),
    Field('hubid', type='reference hub', label='HUB',requires = IS_IN_DB(db, db.hub.hubid, '%(name)s')),
    Field('topicnode', type='string', length=240, requires = IS_UPPER()),
    Field('topicmultilevel', type='string', length=240, requires = IS_UPPER()),
    primarykey=['nodeid', 'operationid', 'hubid'],
    migrate=migrate)

db.define_table('nodecontrol',
    Field('nodecontrolid', type='id'),
    Field('description', type='string', length=200, requires = IS_UPPER()),
    migrate=migrate)

db.define_table('nodecontrol_events',
    Field('nodecontrol_eventsid', type='id'),
    #Field('node_integratedboardid', type='reference node_integratedboard', label='Node Integrated Board',requires = IS_IN_DB(db, db.node_integratedboard.node_integratedboardid, '%(node_integratedboardid)s')),
    Field('nodeid', type='reference node', label='Node',requires = IS_IN_DB(db, db.node.nodeid, '%(name)s', sort=True)),
    Field('nodecontrolid', type='reference nodecontrol', label='Node Control', requires = IS_IN_DB(db, db.nodecontrol.nodecontrolid, '%(description)s', sort=True)),
    Field('description', type='string', length=200, default='REPORT OR REASON FOR GENERATING THIS CONTROL', requires = IS_UPPER()),
    Field('action_date', type='datetime', default = request.now),
    Field('executed', type='boolean', default = False, writable=False),
    primarykey=['nodecontrol_eventsid'],
    migrate=migrate)

db.define_table('Sensores_nodes_view',
    Field('id', type='id'),
    Field('nodeid', type='integer'),
    Field('name', type='string', length=40),
    Field('maxdelay', type='double'),
    Field('threashold', type='string', length=10),
    Field('logicalsensorid', type='integer'),
    Field('description_device', type='string', length=100, requires = IS_UPPER()),
    Field('locationid', type='integer'),
    Field('descripion_location', type='string', length=200),
    migrate=migrate)

db.define_table('node_parameters',
    Field('parametersnodeid', type='id'),
    Field('hubid', type='integer'),
    Field('nodeid', type='integer'),
    Field('lastevent_date', type='datetime'),
    migrate=migrate)

db.define_table('usergroup',
    Field('usergroupid', type='id'),
    Field('name', type='string', length=40, unique=True),
    Field('description', type='string', length=100),
    migrate=migrate)

db.define_table('users',
    Field('userid', type='id'),
    Field('usergroupid', type='reference usergroup'),
    Field('email', type='string', length=40, unique=True),
    Field('password', type='string', length=100),
    migrate=migrate)
'''
