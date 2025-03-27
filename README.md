Основные команды (примеры)

    Открыть браузер: "Открой браузер".

    Управление громкостью: "Увеличь громкость", "Уменьши громкость".

    Выключение ПК: "Выключи компьютер".

    Завершение работы ассистента: "Пока".

Советы по улучшению

    Ключевое слово: Добавьте активацию по слову (например, "Алиса") для экономии ресурсов.

    Больше команд:

        Открытие приложений через subprocess.run(["notepad.exe"]).

        Поиск в Google: webbrowser.open(f"https://google.com/search?q={query}").

    ИИ-интеграция: Используйте OpenAI API для сложных запросов:
    python
    Copy

    import openai
    openai.api_key = "ВАШ_API_КЛЮЧ"
    response = openai.Completion.create(engine="davinci", prompt=command)
    speak(response.choices[0].text)

Запуск

    Запустите скрипт через терминал:
    bash

    python assistant.py
