from . import admin


@admin.route('/')
def index():
    return "<h1 style='color:red'>this is the admin</h1>"
