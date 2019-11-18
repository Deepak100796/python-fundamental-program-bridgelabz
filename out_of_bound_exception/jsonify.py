"""
import statement:
"""
try:
    import json
except ImportError:
    print("invalid module you are imported: ")

a = {"name":"john", "age":24,"address":"bengaluru"}

# conversion to JSON done by dumps() function
b = json.dumps(a)
print(b)