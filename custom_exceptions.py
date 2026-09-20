class AgeError(Exception):
    pass

age = 16

try:
    if age < 18:
        raise AgeError("Age must be 18 or above.")
    print("Eligible")

except AgeError as e:
    print(e)
