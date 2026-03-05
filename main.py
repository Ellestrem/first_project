# print('Hello from repository!')

# Импорт load_dotenv.
from dotenv import load_dotenv 

# Импорт библиотеки для работы с окружением.
import os  

def print_author():
    # Загрузка переменных из .env
    load_dotenv(dotenv_path='/Users/ell/documents/study/terminal/my_project/first_project/.env')

    # Теперь переменные доступны через os.environ
    author = os.getenv('AUTHOR')

    print(f"Автор проекта: {author}")

print_author()