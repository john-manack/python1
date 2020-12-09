def hello_world(name):
    response = "Hello %s!" % name
    return response

username = input("What is your name?")

greeting = hello_world(username)

print(greeting)