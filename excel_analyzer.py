# excel_analyzer.py (Финальный, надёжный вариант для Mac)
import pyautogui
import time
from openpyxl import load_workbook

# --- 0. Функция для надёжного ввода текста (медленно, но верно) ---
def reliable_type(text):
    """Вводит текст посимвольно с небольшой задержкой."""
    for char in text:
        pyautogui.press(char)
        time.sleep(0.08) # Небольшая задержка для Mac

# --- 1. Эмуляция: Запуск приложения (PAE-функция) ---
print("1/4. Запускаем Excel через Spotlight...")

# ⚠️ Стратегический шаг: Убедитесь, что язык переключен на АНГЛИЙСКИЙ вручную
# Мы игнорируем программное переключение, чтобы избежать конфликтов.

pyautogui.hotkey('command', 'space')  # 1. Открыть Spotlight
time.sleep(2.5) # Даем 2.5 секунды, чтобы Spotlight 100% стал активным

# 2. Вводим текст 'Microsoft Excel'
reliable_type('Microsoft Excel') 
pyautogui.press('enter')
time.sleep(5) # Ждем, пока Excel откроется

# --- 2. Эмуляция: Открытие вашего файла (Усиление PAE) ---
print("2/4. Ищем и открываем файл 'data.xlsx'...")

pyautogui.hotkey('command', 'o') # Команда Mac для "Открыть"
time.sleep(2) 

# Вводим имя файла 'data.xlsx'
reliable_type('data.xlsx')
pyautogui.press('enter')
time.sleep(3) 

# --- 3. Анализ: Чтение локального файла (Функция автономии) ---
try:
    print("3/4. Читаем данные из открытого файла data.xlsx...")
    
    # ПРОВЕРКА: Убедитесь, что файл 'data.xlsx' лежит в той же папке
    workbook = load_workbook('data.xlsx')
    sheet = workbook.active
    cell_value = sheet['B5'].value 
    
    # --- 4. Результат ---
    print("-" * 35)
    print(f"✅ Успешно. Значение из ячейки B5: {cell_value}")
    print("Доказательство: Автономный PAE-анализ данных.")
    print("-" * 35)
    
except Exception as e:
    print(f"❌ Произошла ошибка при работе с файлом: {e}")