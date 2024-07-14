import re
import ipywidgets as widgets
from IPython.display import display

def validate_password(password):
   
    if len(password) < 8:
        return False
    
 
    if not re.search(r'[A-Z]', password):
        return False
    
   
    if not re.search(r'[a-z]', password):
        return False
    
   
    if not re.search(r'\d', password):
        return False
    
   
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    
    return True

def on_button_click(b):
    password = password_input.value
    is_valid = validate_password(password)
    result_output.clear_output()
    with result_output:
        if is_valid:
            print("Valid Password.")
        else:
            print("Password does not meet requirements.")


password_input = widgets.Password(description="Password:")

check_button = widgets.Button(description="Check Password")

check_button.on_click(on_button_click)

result_output = widgets.Output()


display(password_input, check_button, result_output)
