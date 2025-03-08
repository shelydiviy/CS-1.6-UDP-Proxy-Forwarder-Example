import random

# Путь к файлу с именами серверов
hostname_file = "/home/user/mirror/udp_16/config/hostnames.txt"

# Количество файлов для генерации
num_files = 700

# Чтение имен серверов из файла
with open(hostname_file, "r", encoding="utf-8") as file:
    hostnames = [line.strip() for line in file if line.strip()]

# Генерация новых файлов
for i in range(num_files):
    # Выбор случайного имени из списка
    random_hostname = random.choice(hostnames)
    
    # Создание содержимого нового файла
    config_content = f'hostname "{random_hostname}"\n'
    
    # Имя нового файла конфигурации
    config_filename = f"s{i}.cfg"
    
    # Запись содержимого в новый файл
    with open(config_filename, "w", encoding="utf-8") as config_file:
        config_file.write(config_content)

print(f"Создано {num_files} файлов конфигурации.")
