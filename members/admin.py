from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display=('firstname', 'lastname', 'joined_date') #passing a list option 

admin.site.register(Member,MemberAdmin) #takes the information and displays it to the coloums







#Double-click sqlite3.exe to open command prompt. 5. Run the following command to reset the password to a null #(blank) password: update users set passwd = null where user_name = '[application username]';
