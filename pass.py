import hashlib



def lines():
	print("="*30)


for i in range(0, 12):
	print("\n")
	i+=1

lines()
pswd = input("Your pass: ")
rst = hashlib.md5(pswd.encode())
final_password = rst.hexdigest()
usr_password = hashlib.sha256(final_password.encode())
lines()
print(f"Your password is encriped sucessfully!")
print(f"{usr_password.hexdigest()}")
lines()
