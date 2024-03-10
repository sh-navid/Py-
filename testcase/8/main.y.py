def event(callback):
    print("Event")
    callback("data")

event(data):
    print("Callback:",data)