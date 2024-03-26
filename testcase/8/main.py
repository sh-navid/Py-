def event(callback):
    print("Event")
    callback("data")


def callback(data):
    print("Callback:", data)


event(callback)
