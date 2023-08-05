import backend

rov = backend.ROV(input("Enter ROV IP: "))
rov.connect()

print("Sending packet...")
output = rov.packet([1])

print(output)