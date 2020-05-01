from django.contrib import admin
from openrobots.models import *

class StationsAdmin (admin.ModelAdmin):
    list_display =['stationName', 'description']

class ProtocolsTypeAdmin (admin.ModelAdmin):
    list_display =['protocolTypeName', 'description']

class ProtocolTemplateFilesAdmin (admin.ModelAdmin):
    list_display =['station', 'typeOfProtocol', 'protocolTemplateFileName', 'protocolTemplateFileName',
                'authors', 'source', 'apiLevel', 'prepareMasterMix', 'transferMasterMix', 'transferSamples']


class ElutionHardwareAdmin (admin.ModelAdmin):
    list_display =['hardwareType']

class MasterMixTypedmin (admin.ModelAdmin):
    list_display =['MasterMixType', 'description']

class MasterMixLabwareAdmin (admin.ModelAdmin):
    list_display =['MasterMixLabwareType', 'description']

class MasterMixTubeAdmin (admin.ModelAdmin):
    list_display =['MasterMixTube', 'MasterMixRadius']

class PCR_plateLabwareAdmin (admin.ModelAdmin):
    list_display =['PCR_plateLabwareType', 'description']

class Elution_LabwareAdmin (admin.ModelAdmin):
    list_display =['elution_LabwareType', 'elutionHW_type', 'valueInCode']

class MagPlate_Labwaredmin (admin.ModelAdmin):
    list_display =('mag_plateLabwareType', 'description')

class ModuleTypeAdmin (admin.ModelAdmin):
    list_display =('moduleType', 'description')

class ModulesInLabAdmin (admin.ModelAdmin):
    list_display =('moduleType','moduleID', 'description')


class Reagent_LabwareAdmin (admin.ModelAdmin):
    list_display =['reagentLabwareType', 'description']


class Waste_LabwareAdmin (admin.ModelAdmin):
    list_display =['wasteLabwareType', 'description']

class RobotsInventoryAdmin (admin.ModelAdmin):
    list_display =('userName', 'configuration',  'location','robots', 'serialNumber','IP_address','hostName',
            'computer_mac','rightPipette', 'leftPipette', 'rightPipetteID', 'leftPipetteID', 'neededPlugs','observations')


class RequestForStationBAdmin (admin.ModelAdmin):
    list_display =['requestedCodeID','magPlateLabware', 'reagentLabware','wasteLabware', 'elutionLabware', 'numberOfSamples',
                'tipTrack', 'dispenseBeads', 'generatedFile', 'usedTemplateFile','userRequestedBy' , 'userNotes']






class RequestForStationCAdmin (admin.ModelAdmin):
    list_display =['requestedCodeID','masterMixLabware', 'masterMixTubeLabware','pcrPlateLabware', 'elutionLabware', 'masterMixType', 'numberOfSamples',
                'prepareMastermix', 'transferMastermix', 'transferSamples', 'generatedFile', 'usedTemplateFile','userRequestedBy' , 'userNotes']




admin.site.register(Stations , StationsAdmin)
admin.site.register(ProtocolsType , ProtocolsTypeAdmin)
admin.site.register(ProtocolTemplateFiles , ProtocolTemplateFilesAdmin)
admin.site.register(ElutionHardware , ElutionHardwareAdmin)

admin.site.register(MagPlate_Labware , MagPlate_Labwaredmin)


admin.site.register(MasterMixType , MasterMixTypedmin)
admin.site.register(MasterMixLabware , MasterMixLabwareAdmin)
admin.site.register(MasterMixTube , MasterMixTubeAdmin)
admin.site.register(PCR_plateLabware , PCR_plateLabwareAdmin)
admin.site.register(Elution_Labware , Elution_LabwareAdmin)
admin.site.register(ModuleType , ModuleTypeAdmin)
admin.site.register(ModulesInLab , ModulesInLabAdmin)

admin.site.register(Reagent_Labware , Reagent_LabwareAdmin)
admin.site.register(Waste_Labware , Waste_LabwareAdmin)

admin.site.register(RobotsInventory , RobotsInventoryAdmin)

admin.site.register(RequestForStationB , RequestForStationBAdmin)
admin.site.register(RequestForStationC , RequestForStationCAdmin)
