# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models
from django.contrib import admin


class FacBinaudits(models.Model):
    binid = models.IntegerField(db_column='BinID') # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID') # Field name made lowercase.
    auditstamp = models.DateTimeField(db_column='AuditStamp') # Field name made lowercase.
    class Meta:
        db_table = u'fac_binaudits'

class FacBincontents(models.Model):
    binid = models.IntegerField(db_column='BinID') # Field name made lowercase.
    supplyid = models.IntegerField(db_column='SupplyID') # Field name made lowercase.
    count = models.IntegerField(db_column='Count') # Field name made lowercase.
    class Meta:
        db_table = u'fac_bincontents'

class FacCabinet(models.Model):
    cabinetid = models.IntegerField(primary_key=True, db_column='CabinetID') # Field name made lowercase.
    datacenterid = models.IntegerField(db_column='DataCenterID') # Field name made lowercase.
    location = models.CharField(max_length=60, db_column='Location') # Field name made lowercase.
    assignedto = models.IntegerField(db_column='AssignedTo') # Field name made lowercase.
    zoneid = models.IntegerField(db_column='ZoneID') # Field name made lowercase.
    cabinetheight = models.IntegerField(db_column='CabinetHeight') # Field name made lowercase.
    model = models.CharField(max_length=240, db_column='Model') # Field name made lowercase.
    keylock = models.CharField(max_length=90, db_column='Keylock') # Field name made lowercase.
    maxkw = models.FloatField(db_column='MaxKW') # Field name made lowercase.
    maxweight = models.IntegerField(db_column='MaxWeight') # Field name made lowercase.
    installationdate = models.DateField(db_column='InstallationDate') # Field name made lowercase.
    sensoripaddress = models.CharField(max_length=60, db_column='SensorIPAddress') # Field name made lowercase.
    sensorcommunity = models.CharField(max_length=120, db_column='SensorCommunity') # Field name made lowercase.
    sensoroid = models.CharField(max_length=240, db_column='SensorOID') # Field name made lowercase.
    mapx1 = models.IntegerField(db_column='MapX1') # Field name made lowercase.
    mapx2 = models.IntegerField(db_column='MapX2') # Field name made lowercase.
    mapy1 = models.IntegerField(db_column='MapY1') # Field name made lowercase.
    mapy2 = models.IntegerField(db_column='MapY2') # Field name made lowercase.
    class Meta:
        db_table = u'fac_cabinet'

class FacCabinetaudit(models.Model):
    cabinetid = models.IntegerField(db_column='CabinetID') # Field name made lowercase.
    userid = models.CharField(max_length=240, db_column='UserID') # Field name made lowercase.
    auditstamp = models.DateTimeField(db_column='AuditStamp') # Field name made lowercase.
    class Meta:
        db_table = u'fac_cabinetaudit'

class FacCabinettemps(models.Model):
    cabinetid = models.IntegerField(primary_key=True, db_column='CabinetID') # Field name made lowercase.
    lastread = models.DateTimeField(db_column='LastRead') # Field name made lowercase.
    temp = models.IntegerField(db_column='Temp') # Field name made lowercase.
    class Meta:
        db_table = u'fac_cabinettemps'

class FacCdutemplate(models.Model):
    templateid = models.IntegerField(primary_key=True, db_column='TemplateID') # Field name made lowercase.
    manufacturerid = models.IntegerField(db_column='ManufacturerID') # Field name made lowercase.
    model = models.CharField(max_length=240, unique=True, db_column='Model') # Field name made lowercase.
    managed = models.IntegerField(db_column='Managed') # Field name made lowercase.
    versionoid = models.CharField(max_length=240, db_column='VersionOID') # Field name made lowercase.
    multiplier = models.CharField(max_length=9, db_column='Multiplier', blank=True) # Field name made lowercase.
    oid1 = models.CharField(max_length=240, db_column='OID1') # Field name made lowercase.
    oid2 = models.CharField(max_length=240, db_column='OID2') # Field name made lowercase.
    oid3 = models.CharField(max_length=240, db_column='OID3') # Field name made lowercase.
    processingprofile = models.CharField(max_length=54, db_column='ProcessingProfile', blank=True) # Field name made lowercase.
    voltage = models.IntegerField(db_column='Voltage') # Field name made lowercase.
    amperage = models.IntegerField(db_column='Amperage') # Field name made lowercase.
    numoutlets = models.IntegerField(db_column='NumOutlets') # Field name made lowercase.
    class Meta:
        db_table = u'fac_cdutemplate'

class FacConfig(models.Model):
    parameter = models.CharField(max_length=120, db_column='Parameter') # Field name made lowercase.
    value = models.CharField(max_length=600, db_column='Value') # Field name made lowercase.
    unitofmeasure = models.CharField(max_length=120, db_column='UnitOfMeasure') # Field name made lowercase.
    valtype = models.CharField(max_length=120, db_column='ValType') # Field name made lowercase.
    defaultval = models.CharField(max_length=600, db_column='DefaultVal') # Field name made lowercase.
    class Meta:
        db_table = u'fac_config'

class FacContact(models.Model):
    contactid = models.IntegerField(primary_key=True, db_column='ContactID') # Field name made lowercase.
    userid = models.CharField(max_length=240, db_column='UserID') # Field name made lowercase.
    lastname = models.CharField(max_length=120, db_column='LastName') # Field name made lowercase.
    firstname = models.CharField(max_length=120, db_column='FirstName') # Field name made lowercase.
    phone1 = models.CharField(max_length=60, db_column='Phone1') # Field name made lowercase.
    phone2 = models.CharField(max_length=60, db_column='Phone2') # Field name made lowercase.
    phone3 = models.CharField(max_length=60, db_column='Phone3') # Field name made lowercase.
    email = models.CharField(max_length=240, db_column='Email') # Field name made lowercase.
    class Meta:
        db_table = u'fac_contact'

class FacDatacenter(models.Model):
    datacenterid = models.IntegerField(primary_key=True, db_column='DataCenterID') # Field name made lowercase.
    name = models.CharField(max_length=765, db_column='Name') # Field name made lowercase.
    squarefootage = models.IntegerField(db_column='SquareFootage') # Field name made lowercase.
    deliveryaddress = models.CharField(max_length=765, db_column='DeliveryAddress') # Field name made lowercase.
    administrator = models.CharField(max_length=240, db_column='Administrator') # Field name made lowercase.
    maxkw = models.IntegerField(db_column='MaxkW') # Field name made lowercase.
    drawingfilename = models.CharField(max_length=765, db_column='DrawingFileName') # Field name made lowercase.
    entrylogging = models.IntegerField(db_column='EntryLogging') # Field name made lowercase.
    class Meta:
        db_table = u'fac_datacenter'

class FacDecommission(models.Model):
    surplusdate = models.DateField(db_column='SurplusDate') # Field name made lowercase.
    label = models.CharField(max_length=240, db_column='Label') # Field name made lowercase.
    serialno = models.CharField(max_length=120, db_column='SerialNo') # Field name made lowercase.
    assettag = models.CharField(max_length=60, db_column='AssetTag') # Field name made lowercase.
    userid = models.CharField(max_length=240, db_column='UserID') # Field name made lowercase.
    class Meta:
        db_table = u'fac_decommission'

class FacDepartment(models.Model):
    deptid = models.IntegerField(primary_key=True, db_column='DeptID') # Field name made lowercase.
    name = models.CharField(max_length=255, unique=True, db_column='Name') # Field name made lowercase.
    execsponsor = models.CharField(max_length=240, db_column='ExecSponsor') # Field name made lowercase.
    sdm = models.CharField(max_length=240, db_column='SDM') # Field name made lowercase.
    classification = models.CharField(max_length=240, db_column='Classification') # Field name made lowercase.
    deptcolor = models.CharField(max_length=21, db_column='DeptColor') # Field name made lowercase.
    class Meta:
        db_table = u'fac_department'

class FacDeptcontacts(models.Model):
    deptid = models.IntegerField(db_column='DeptID') # Field name made lowercase.
    contactid = models.IntegerField(db_column='ContactID') # Field name made lowercase.
    class Meta:
        db_table = u'fac_deptcontacts'

class FacDevice(models.Model):
    deviceid = models.IntegerField(primary_key=True, db_column='DeviceID') # Field name made lowercase.
    label = models.CharField(max_length=240, db_column='Label') # Field name made lowercase.
    serialno = models.CharField(max_length=120, db_column='SerialNo') # Field name made lowercase.
    assettag = models.CharField(max_length=60, db_column='AssetTag') # Field name made lowercase.
    primaryip = models.CharField(max_length=60, db_column='PrimaryIP') # Field name made lowercase.
    snmpcommunity = models.CharField(max_length=240, db_column='SNMPCommunity') # Field name made lowercase.
    esx = models.IntegerField(db_column='ESX') # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner') # Field name made lowercase.
    escalationtimeid = models.IntegerField(db_column='EscalationTimeID') # Field name made lowercase.
    escalationid = models.IntegerField(db_column='EscalationID') # Field name made lowercase.
    primarycontact = models.IntegerField(db_column='PrimaryContact') # Field name made lowercase.
    cabinet = models.IntegerField(db_column='Cabinet') # Field name made lowercase.
    position = models.IntegerField(db_column='Position') # Field name made lowercase.
    height = models.IntegerField(db_column='Height') # Field name made lowercase.
    ports = models.IntegerField(db_column='Ports') # Field name made lowercase.
    templateid = models.IntegerField(db_column='TemplateID') # Field name made lowercase.
    nominalwatts = models.IntegerField(db_column='NominalWatts') # Field name made lowercase.
    powersupplycount = models.IntegerField(db_column='PowerSupplyCount') # Field name made lowercase.
    devicetype = models.CharField(max_length=69, db_column='DeviceType') # Field name made lowercase.
    chassisslots = models.IntegerField(db_column='ChassisSlots') # Field name made lowercase.
    rearchassisslots = models.IntegerField(db_column='RearChassisSlots') # Field name made lowercase.
    parentdevice = models.IntegerField(db_column='ParentDevice') # Field name made lowercase.
    mfgdate = models.DateField(db_column='MfgDate') # Field name made lowercase.
    installdate = models.DateField(db_column='InstallDate') # Field name made lowercase.
    warrantyco = models.CharField(max_length=240, db_column='WarrantyCo') # Field name made lowercase.
    warrantyexpire = models.DateField(null=True, db_column='WarrantyExpire', blank=True) # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True) # Field name made lowercase.
    reservation = models.IntegerField(db_column='Reservation') # Field name made lowercase.
    class Meta:
        db_table = u'fac_device'

class FacDevicetags(models.Model):
    deviceid = models.IntegerField(primary_key=True, db_column='DeviceID') # Field name made lowercase.
    tagid = models.IntegerField(primary_key=True, db_column='TagID') # Field name made lowercase.
    class Meta:
        db_table = u'fac_devicetags'

class FacDevicetemplate(models.Model):
    templateid = models.IntegerField(primary_key=True, db_column='TemplateID') # Field name made lowercase.
    manufacturerid = models.IntegerField(db_column='ManufacturerID') # Field name made lowercase.
    model = models.CharField(max_length=240, db_column='Model') # Field name made lowercase.
    height = models.IntegerField(db_column='Height') # Field name made lowercase.
    weight = models.IntegerField(db_column='Weight') # Field name made lowercase.
    wattage = models.IntegerField(db_column='Wattage') # Field name made lowercase.
    devicetype = models.CharField(max_length=69, db_column='DeviceType') # Field name made lowercase.
    pscount = models.IntegerField(db_column='PSCount') # Field name made lowercase.
    numports = models.IntegerField(db_column='NumPorts') # Field name made lowercase.
    class Meta:
        db_table = u'fac_devicetemplate'

class FacEscalations(models.Model):
    escalationid = models.IntegerField(primary_key=True, db_column='EscalationID') # Field name made lowercase.
    details = models.CharField(max_length=240, db_column='Details', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'fac_escalations'

class FacEscalationtimes(models.Model):
    escalationtimeid = models.IntegerField(primary_key=True, db_column='EscalationTimeID') # Field name made lowercase.
    timeperiod = models.CharField(max_length=240, db_column='TimePeriod') # Field name made lowercase.
    class Meta:
        db_table = u'fac_escalationtimes'

class FacManufacturer(models.Model):
    manufacturerid = models.IntegerField(primary_key=True, db_column='ManufacturerID') # Field name made lowercase.
    name = models.CharField(max_length=240, db_column='Name') # Field name made lowercase.
    class Meta:
        db_table = u'fac_manufacturer'

class FacPanelschedule(models.Model):
    panelid = models.IntegerField(primary_key=True, db_column='PanelID') # Field name made lowercase.
    poleposition = models.IntegerField(db_column='PolePosition') # Field name made lowercase.
    numpoles = models.IntegerField(db_column='NumPoles') # Field name made lowercase.
    label = models.CharField(max_length=240, db_column='Label') # Field name made lowercase.
    class Meta:
        db_table = u'fac_panelschedule'

class FacPatchconnection(models.Model):
    paneldeviceid = models.IntegerField(primary_key=True, db_column='PanelDeviceID') # Field name made lowercase.
    panelportnumber = models.IntegerField(primary_key=True, db_column='PanelPortNumber') # Field name made lowercase.
    frontendpointdeviceid = models.IntegerField(null=True, db_column='FrontEndpointDeviceID', blank=True) # Field name made lowercase.
    frontendpointport = models.IntegerField(null=True, db_column='FrontEndpointPort', blank=True) # Field name made lowercase.
    rearendpointdeviceid = models.IntegerField(null=True, db_column='RearEndpointDeviceID', blank=True) # Field name made lowercase.
    rearendpointport = models.IntegerField(null=True, db_column='RearEndpointPort', blank=True) # Field name made lowercase.
    frontnotes = models.CharField(max_length=240, db_column='FrontNotes', blank=True) # Field name made lowercase.
    rearnotes = models.CharField(max_length=240, db_column='RearNotes', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'fac_patchconnection'

class FacPdustats(models.Model):
    pduid = models.IntegerField(primary_key=True, db_column='PDUID') # Field name made lowercase.
    wattage = models.IntegerField(db_column='Wattage') # Field name made lowercase.
    class Meta:
        db_table = u'fac_pdustats'

class FacPowerconnection(models.Model):
    pduid = models.IntegerField(unique=True, db_column='PDUID') # Field name made lowercase.
    pduposition = models.IntegerField(unique=True, db_column='PDUPosition') # Field name made lowercase.
    deviceid = models.IntegerField(unique=True, db_column='DeviceID') # Field name made lowercase.
    deviceconnnumber = models.IntegerField(unique=True, db_column='DeviceConnNumber') # Field name made lowercase.
    class Meta:
        db_table = u'fac_powerconnection'

class FacPowerdistribution(models.Model):
    pduid = models.IntegerField(primary_key=True, db_column='PDUID') # Field name made lowercase.
    label = models.CharField(max_length=120, db_column='Label') # Field name made lowercase.
    cabinetid = models.IntegerField(db_column='CabinetID') # Field name made lowercase.
    templateid = models.IntegerField(db_column='TemplateID') # Field name made lowercase.
    ipaddress = models.CharField(max_length=48, db_column='IPAddress') # Field name made lowercase.
    snmpcommunity = models.CharField(max_length=150, db_column='SNMPCommunity') # Field name made lowercase.
    firmwareversion = models.CharField(max_length=120, db_column='FirmwareVersion') # Field name made lowercase.
    panelid = models.IntegerField(db_column='PanelID') # Field name made lowercase.
    breakersize = models.IntegerField(db_column='BreakerSize') # Field name made lowercase.
    panelpole = models.IntegerField(db_column='PanelPole') # Field name made lowercase.
    failsafe = models.IntegerField(db_column='FailSafe') # Field name made lowercase.
    panelid2 = models.IntegerField(db_column='PanelID2') # Field name made lowercase.
    panelpole2 = models.IntegerField(db_column='PanelPole2') # Field name made lowercase.
    class Meta:
        db_table = u'fac_powerdistribution'

class FacPowerpanel(models.Model):
    panelid = models.IntegerField(primary_key=True, db_column='PanelID') # Field name made lowercase.
    powersourceid = models.IntegerField(db_column='PowerSourceID') # Field name made lowercase.
    panellabel = models.CharField(max_length=60, db_column='PanelLabel') # Field name made lowercase.
    numberofpoles = models.IntegerField(db_column='NumberOfPoles') # Field name made lowercase.
    mainbreakersize = models.IntegerField(db_column='MainBreakerSize') # Field name made lowercase.
    panelvoltage = models.IntegerField(db_column='PanelVoltage') # Field name made lowercase.
    numberscheme = models.CharField(max_length=30, db_column='NumberScheme') # Field name made lowercase.
    class Meta:
        db_table = u'fac_powerpanel'

class FacPowersource(models.Model):
    powersourceid = models.IntegerField(primary_key=True, db_column='PowerSourceID') # Field name made lowercase.
    sourcename = models.CharField(max_length=240, db_column='SourceName') # Field name made lowercase.
    datacenterid = models.IntegerField(db_column='DataCenterID') # Field name made lowercase.
    ipaddress = models.CharField(max_length=60, db_column='IPAddress') # Field name made lowercase.
    community = models.CharField(max_length=120, db_column='Community') # Field name made lowercase.
    loadoid = models.CharField(max_length=240, db_column='LoadOID') # Field name made lowercase.
    capacity = models.IntegerField(db_column='Capacity') # Field name made lowercase.
    class Meta:
        db_table = u'fac_powersource'

class FacRackrequest(models.Model):
    requestid = models.IntegerField(primary_key=True, db_column='RequestID') # Field name made lowercase.
    requestorid = models.IntegerField(db_column='RequestorID') # Field name made lowercase.
    requesttime = models.DateTimeField(db_column='RequestTime') # Field name made lowercase.
    completetime = models.DateTimeField(db_column='CompleteTime') # Field name made lowercase.
    label = models.CharField(max_length=120, db_column='Label') # Field name made lowercase.
    serialno = models.CharField(max_length=120, db_column='SerialNo') # Field name made lowercase.
    mfgdate = models.DateField(db_column='MfgDate') # Field name made lowercase.
    assettag = models.CharField(max_length=120, db_column='AssetTag') # Field name made lowercase.
    esx = models.IntegerField(db_column='ESX') # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner') # Field name made lowercase.
    deviceheight = models.IntegerField(db_column='DeviceHeight') # Field name made lowercase.
    ethernetcount = models.IntegerField(db_column='EthernetCount') # Field name made lowercase.
    vlanlist = models.CharField(max_length=240, db_column='VLANList') # Field name made lowercase.
    sancount = models.IntegerField(db_column='SANCount') # Field name made lowercase.
    sanlist = models.CharField(max_length=240, db_column='SANList') # Field name made lowercase.
    deviceclass = models.CharField(max_length=240, db_column='DeviceClass') # Field name made lowercase.
    devicetype = models.CharField(max_length=69, db_column='DeviceType') # Field name made lowercase.
    labelcolor = models.CharField(max_length=240, db_column='LabelColor') # Field name made lowercase.
    currentlocation = models.CharField(max_length=360, db_column='CurrentLocation') # Field name made lowercase.
    specialinstructions = models.TextField(db_column='SpecialInstructions') # Field name made lowercase.
    class Meta:
        db_table = u'fac_rackrequest'

class FacSupplies(models.Model):
    supplyid = models.IntegerField(primary_key=True, db_column='SupplyID') # Field name made lowercase.
    partnum = models.CharField(max_length=120, db_column='PartNum') # Field name made lowercase.
    partname = models.CharField(max_length=240, db_column='PartName') # Field name made lowercase.
    minqty = models.IntegerField(db_column='MinQty') # Field name made lowercase.
    maxqty = models.IntegerField(db_column='MaxQty') # Field name made lowercase.
    class Meta:
        db_table = u'fac_supplies'

class FacSupplybin(models.Model):
    binid = models.IntegerField(primary_key=True, db_column='BinID') # Field name made lowercase.
    location = models.CharField(max_length=120, db_column='Location') # Field name made lowercase.
    class Meta:
        db_table = u'fac_supplybin'

class FacSwitchconnection(models.Model):
    switchdeviceid = models.IntegerField(unique=True, db_column='SwitchDeviceID') # Field name made lowercase.
    switchportnumber = models.IntegerField(unique=True, db_column='SwitchPortNumber') # Field name made lowercase.
    endpointdeviceid = models.IntegerField(unique=True, db_column='EndpointDeviceID') # Field name made lowercase.
    endpointport = models.IntegerField(unique=True, db_column='EndpointPort') # Field name made lowercase.
    notes = models.CharField(max_length=240, db_column='Notes') # Field name made lowercase.
    class Meta:
        db_table = u'fac_switchconnection'

class FacTags(models.Model):
    tagid = models.IntegerField(primary_key=True, db_column='TagID') # Field name made lowercase.
    name = models.CharField(max_length=255, unique=True, db_column='Name') # Field name made lowercase.
    class Meta:
        db_table = u'fac_tags'

class FacUser(models.Model):
    userid = models.CharField(max_length=240, primary_key=True, db_column='UserID') # Field name made lowercase.
    name = models.CharField(max_length=240, db_column='Name') # Field name made lowercase.
    readaccess = models.IntegerField(db_column='ReadAccess') # Field name made lowercase.
    writeaccess = models.IntegerField(db_column='WriteAccess') # Field name made lowercase.
    deleteaccess = models.IntegerField(db_column='DeleteAccess') # Field name made lowercase.
    contactadmin = models.IntegerField(db_column='ContactAdmin') # Field name made lowercase.
    rackrequest = models.IntegerField(db_column='RackRequest') # Field name made lowercase.
    rackadmin = models.IntegerField(db_column='RackAdmin') # Field name made lowercase.
    siteadmin = models.IntegerField(db_column='SiteAdmin') # Field name made lowercase.
    disabled = models.IntegerField(db_column='Disabled') # Field name made lowercase.
    class Meta:
        db_table = u'fac_user'

class FacVminventory(models.Model):
    vmindex = models.IntegerField(primary_key=True, db_column='VMIndex') # Field name made lowercase.
    deviceid = models.IntegerField(db_column='DeviceID') # Field name made lowercase.
    lastupdated = models.DateTimeField(db_column='LastUpdated') # Field name made lowercase.
    vmid = models.IntegerField(db_column='vmID') # Field name made lowercase.
    vmname = models.CharField(max_length=240, db_column='vmName') # Field name made lowercase.
    vmstate = models.CharField(max_length=240, db_column='vmState') # Field name made lowercase.
    owner = models.IntegerField(db_column='Owner') # Field name made lowercase.
    class Meta:
        db_table = u'fac_vminventory'

class FacZone(models.Model):
    zoneid = models.IntegerField(primary_key=True, db_column='ZoneID') # Field name made lowercase.
    datacenterid = models.IntegerField(db_column='DataCenterID') # Field name made lowercase.
    description = models.CharField(max_length=360, db_column='Description') # Field name made lowercase.
    class Meta:
        db_table = u'fac_zone'

class FacDeviceAdmin(admin.ModelAdmin):
    fields = ('deviceid', 'cabinet', 'label', 'nominalwatts')

