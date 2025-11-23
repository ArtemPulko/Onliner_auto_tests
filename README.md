# Часть 1. Реализовать следующий тест на сайте Onliner с использованием модели page object, Selenium, PyTest.
1. Открыть категорию "Мобильные телефоны". Убедиться, что она открыта. 
2. Найти два любых телефона из первых 10 и добавить их для сравнения.
    Проверить, что ссылка для сравнения существует и флажки установлены. 
3. Установить параметры поиска: цена (минимальная и максимальная),
    размер экрана (минимальный и максимальный) - соответствующие  минимальным и максимальным параметрам выбранных телефонов.
    Убедиться, что выбранные телефоны по-прежнему отображаются и флажки установлены. 
4. Перейти на любой из выбранных телефонов.
    Проверить, совпадают ли параметры с предыдущей страницей
    (операционная система, размер экрана, диагональ экрана, объем оперативной памяти).
5. Нажать на ссылку сравнения. Убедиться, что два телефона содержат правильную информацию (описанную в предыдущем шаге) и не совпадают друг с другом.
## Файлы с тестами
•	Файл test_open_catalog содержит тесты для выполнения задачи № 1  
•	Файл test_select_phone содержит тесты для выполнения задачи № 2, 3  
•	Файл test_phone_parametrs содержит тест для выполнения задачи № 4  
•	Файл test_compare содержит тесты для выполнения задачи № 5  
## Установка  
Клонирование репозитория:  
```
git clone https://github.com/ArtemPulko/Onliner_auto_tests.git
```
Перед запуском тестов необходимо выполнить:  
```
pip install -r Onliner_auto_tests/requirements.txt
```
На компьютере должен быть установлен Chrome и соответсвующий ему ChromeDriver.  
Для установки драйвера необходимо:  
1. Поместить файл с драйвером в модуль ```drivers```
2. В  ```__init__.py``` переменной ```driver_name``` писвоить имя файла необходимого драйвера   
```python
def get_chromedriver_path(path):
      driver_name = 'chromedriver.exe' # Тесты будут использовать драйвер - chromedriver.exe
      project_root = path.parents[1]
      return project_root / 'drivers' / driver_name
```
Ссылки на скачивание браузера и драйвера:  
Stable Version: 142.0.7444.175 (r1522585)  
&emsp;Сhrome:  
&emsp;&emsp;Linux64: https://storage.googleapis.com/chrome-for-testing-public/142.0.7444.175/linux64/chrome-linux64.zip  
&emsp;&emsp;win64:&ensp;&ensp;https://storage.googleapis.com/chrome-for-testing-public/142.0.7444.175/win64/chrome-win64.zip  
&emsp;Chromedriver:  
&emsp;&emsp;Linux64: https://storage.googleapis.com/chrome-for-testing-public/142.0.7444.175/linux64/chromedriver-linux64.zip  
&emsp;&emsp;win64:&ensp;&ensp;https://storage.googleapis.com/chrome-for-testing-public/142.0.7444.175/win64/chromedriver-win64.zip  
        
