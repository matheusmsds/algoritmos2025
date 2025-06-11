import os

email = input("")
msg_commit =  input("msg_commit: ")
comando = f"git config user.email \"{email}\""
os.system(comando)
comando = f"git add *"
os.system(comando)
comando = f"git commit -m \"{msg_commit}\""
os.system(comando)
comando = f"git push --set-upstream origin master"
os.system(comando)
print("Comandos executados com sucesso, programa finalizado.")