import os

def insecure_command_execution():
    print("Ingrese el comando a ejecutar:")
    user_input = input()
    os.system(user_input)  # Vulnerabilidad: ejecución insegura de comandos

if __name__ == "__main__":
    insecure_command_execution()
