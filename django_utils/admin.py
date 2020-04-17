from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
from django.contrib.auth.models import User  
from django_utils.models import *                    



# Register your models here.
class CenterAdmin(admin.ModelAdmin):                            
      list_display = ('centerName','centerAbbr')                 

class ProfileInline(admin.StackedInline): 
 	    model = Profile                   
 	    can_delete = False                 
 	    verbose_name_plural = 'Profiles'   
                                            
# Define a new User admin                  
class UserAdmin(BaseUserAdmin):            
 	inlines = (ProfileInline, )           
                                            
                                            
 # Re-register UserAdmin                    
admin.site.unregister(User)                
admin.site.register(User, UserAdmin)       
admin.site.register(Center,CenterAdmin) 

