# -*- coding: utf-8 -*-
"""
Конфигурация бота EmSystem by Yevgeniya Em.

Бот поддерживает 4 языка интерфейса: русский, английский, итальянский, французский.
Все тексты, кнопки и FAQ переведены на каждый язык и лежат в словаре TEXTS.

Как добавить/убрать язык:
  1. Добавьте/удалите код языка в LANGUAGES (ключ — код, значение — подпись кнопки).
  2. Добавьте/удалите соответствующий блок в TEXTS с тем же кодом языка.
Все ключи внутри TEXTS["ru"], TEXTS["it"], TEXTS["fr"] должны совпадать -
bot.py обращается к ним по этим именам.

Сам код логики бота лежит в bot.py и трогать его для правки текстов не нужно.
"""

import os

# ============================================================
# ТОКЕН БОТА
# ============================================================
# Получить/перевыпустить токен: @BotFather -> /mybots -> @MethodEmbrowBot
# -> API Token -> Revoke current token (если старый токен утерян/скомпрометирован)
# Токен лучше не хранить в коде, а положить в переменную окружения BOT_TOKEN
# (см. .env.example) либо через export BOT_TOKEN=... перед запуском.
BOT_TOKEN = os.getenv("BOT_TOKEN", "8582789594:AAEQBRo3D6DvWNF_bMLIpn7zOUmmwzAPszw")

# ============================================================
# ССЫЛКА НА ПОКУПКУ КУРСА
# ============================================================
BUY_URL = "http://emsystem.me/"

# ============================================================
# ВИДЕО
# ============================================================
# ВАЖНО про видео в Telegram-ботах:
# Обычный Bot API умеет принимать от бота файл на отправку размером
# ДО 50 МБ. Если у видео больше — отправить его напрямую с диска бот
# не сможет.
#
# Как решить (любой из вариантов):
#   1) Сжать видео до <50 МБ - самый простой путь.
#   2) Один раз отправить видео вручную боту, после чего Telegram сам
#      присвоит файлу постоянный file_id. Взять update.message.video.file_id
#      из лога (см. get_file_id.py в этом проекте) и вставить сюда.
#      После этого бот будет мгновенно пересылать видео по file_id,
#      без повторной загрузки.
#   3) Поднять локальный Bot API сервер (telegram-bot-api), который
#      снимает лимит в 50 МБ (до 2 ГБ).
#
# Видео сейчас общее для всех языков (одно и то же для "О курсе" и
# для "Бесплатного урока" на всех языках). Если понадобятся отдельные
# видео на разных языках - можно расширить структуру до словаря вида
# {"ru": "...", "it": "...", "fr": "..."} и поменять send_course_video
# в bot.py соответственно.
VIDEO_ABOUT_FILE_ID = os.getenv("VIDEO_ABOUT_FILE_ID", "BAACAgIAAxkBAAPIanSS4GULisUdJIhMrhf2l0kLcGkAAnOpAAIBCKhLBKjMThbFhmI9BA")
VIDEO_ABOUT_PATH = os.getenv("VIDEO_ABOUT_PATH", "assets/welcome.mp4")

VIDEO_LESSON_FILE_ID = os.getenv("VIDEO_LESSON_FILE_ID", "BAACAgIAAxkBAAPKanSS8DlSBVt1zl6F0ync7DOvh50AAnWpAAIBCKhLduBuY83Dy0o9BA")
VIDEO_LESSON_PATH = os.getenv("VIDEO_LESSON_PATH", "assets/welcome2.mp4")

# ============================================================
# МЕДИА ДЛЯ РАЗДЕЛА "РАБОТЫ УЧЕНИКОВ"
# ============================================================
# Фото/видео разбиты по вкладкам (До/после, Отзывы, Сертификаты, Видео).
# Внутри каждой вкладки фото выдаются порциями (по WORKS_PHOTOS_PAGE_SIZE
# штук за раз) с кнопкой "Показать ещё", чтобы не заваливать клиента
# всеми фото разом.
WORKS_PHOTOS_PAGE_SIZE = 10

WORKS_VIDEOS = [
    "BAACAgIAAxkBAAIBamp0xKppSI1rZxFZYSvHO44ic4aOAALtqwACAQioS8f37phu3na7PQQ",
    "BAACAgIAAxkBAAIBa2p0xKpudDQiB5g4WmE2k4wIvRwQAALuqwACAQioS116B1VdD_FXPQQ",
    "BAACAgIAAxkBAAIBbGp0xKqQo_TNgLYxzHVuD-dnln8RAALvqwACAQioS28Zo_BoTZKlPQQ",
]

# 33 фото поровну на 3 категории: 11 / 11 / 11
WORKS_PHOTOS_BEFORE_AFTER = [
    "AgACAgIAAxkBAAIBWGp0xJ_Rhr93kAmfQJfWSxwegd82AAKEG2sbEMmhS0HDKnNJyWFKAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBWWp0xJ-e4-13IirMvMSR06PBHibnAAJ0G2sbEMmhS9f8U6rzqb7ZAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBWmp0xJ8-iBNFpVc5WeqjGsYvp_lEAAJ1G2sbEMmhS9jFYWUZhHhfAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBW2p0xJ8Jb-SEh-p1CaMgaiI2_3AlAAJ2G2sbEMmhS7bkBIx9nF76AQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBSmp0xJyCnhtFzLXgkGAzP-4fB-rKAAJ3G2sbEMmhSzii6ou30dSDAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBS2p0xJwIEcApAoDgomiei9Bbxe4kAAJ4G2sbEMmhSyg7aut8CKOHAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBTGp0xJxquyE4WOWQ1NXNX62pMC5pAAJ5G2sbEMmhS-8-W5ewBo0CAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBTWp0xJxFmdBqVur_8rmlKqp_aKcEAAJ6G2sbEMmhSxCL2ni-zm9jAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBTmp0xJzX3xIknRj_eQTkba1uB2T-AAJ7G2sbEMmhS2YxRxh613OHAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBT2p0xJyzP646VB1fltnVIrtcuH6HAAJ8G2sbEMmhS-HSBbaufrtOAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBUGp0xJwYgCO0anE1vlOePFZkBzQbAAJ9G2sbEMmhSzpWO54nafYuAQADAgADeQADPQQ",
]

WORKS_PHOTOS_REVIEWS = [
    "AgACAgIAAxkBAAIBUWp0xJwmcaB7qPGxbA_4Cktlkkx0AAJ-G2sbEMmhS06RBDmC9Ww-AQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBU2p0xJzcdKqA2HNoZPUzpsJkpUQeAAJ_G2sbEMmhSyOghOsl3pdeAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBVGp0xJ9v8zZjOkq2pOF0kjVmO6ZCAAKAG2sbEMmhS8pXeY9QrTJUAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBVWp0xJ8AAURhARQ79pBQtoSYxiDiWQACgRtrGxDJoUsdgdOJB2VV_QEAAwIAA3kAAz0E",
    "AgACAgIAAxkBAAIBVmp0xJ9I2DUar44v5OSwWWVfF22oAAKCG2sbEMmhS4ztVZl_PiR9AQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBV2p0xJ8f-kZr1-oEAeQkBoStEggZAAKDG2sbEMmhS7jc8vPiFI6bAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBXGp0xJ8r07TSpQbHyk63PUU3pPxLAAKFG2sbEMmhS3y1Z1YQzdY-AQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBXWp0xJ_HtVFSOMQhQfmmnmnT8NwdAAKGG2sbEMmhSz2j23jX13xVAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBXmp0xKFoaC_Syh5qJ_SdWzqfepkzAAKHG2sbEMmhSzG8f6DNSvI1AQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBX2p0xKE2aEWyPBFrFXMmJa_fI9-2AAKIG2sbEMmhS97E38RzhAABlAEAAwIAA3kAAz0E",
    "AgACAgIAAxkBAAIBYGp0xKFOJhGXH5wdtlJWGbRcXPjzAAKJG2sbEMmhS6PS95g5Dj2wAQADAgADeQADPQQ",
]

WORKS_PHOTOS_CERTIFICATES = [
    "AgACAgIAAxkBAAIBYWp0xKHEr8TFnf6p3G0wht2zWTupAAKKG2sbEMmhS2ewhPRkZji2AQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBYmp0xKE1WemAOdBB895OkrUtpRaFAAKLG2sbEMmhSzOtrkekMzlxAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBY2p0xKH_k468nD9godZ3C1nGwMRVAAKMG2sbEMmhS8w9x3G2uhBeAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBZGp0xKHpDkfx8OyqFA2Isx4pVUHdAAKNG2sbEMmhSzOEhTEo8FkAAQEAAwIAA3kAAz0E",
    "AgACAgIAAxkBAAIBZWp0xKEGZuatU06J-8b7Cjt3qUGhAAKOG2sbEMmhS81JqOnk09oQAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBZmp0xKE2UgWhs5ZSEaaFQUHWwrr9AAKPG2sbEMmhSyM5llZ-EoPGAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBZ2p0xKHdRVO3rw9E6yo7F5Ji8W3oAAKQG2sbEMmhS7VdWd8hbftIAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBaGp0xKrAZ7fsCSlpmYZUkiVFdtxSAAKRG2sbEMmhS95--Y2efiMiAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBaWp0xKpXHPrOkskhEALWrGMKLnr3AAKSG2sbEMmhSxTziM73LOA4AQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBbWp0xKpPP_EfV_nHEr0Nio2pfJefAAKVG2sbEMmhS4bVN9HvXpHGAQADAgADeQADPQQ",
    "AgACAgIAAxkBAAIBbmp0xKpTm_KX4WLatk9WClHecbULAAKUG2sbEMmhS1Ver5IPCK_VAQADAgADeQADPQQ",
]

# Категории для меню "Работы учеников".
# key: код категории (используется в callback_data works:<key>:<offset>)
# type: "photo" или "video"
# items: список file_id
WORKS_CATEGORIES = {
    "before_after": {"type": "photo", "items": WORKS_PHOTOS_BEFORE_AFTER},
    "reviews": {"type": "photo", "items": WORKS_PHOTOS_REVIEWS},
    "certificates": {"type": "photo", "items": WORKS_PHOTOS_CERTIFICATES},
    "videos": {"type": "video", "items": WORKS_VIDEOS},
}

# ============================================================
# ЯЗЫКИ
# ============================================================
# Ключ - код языка, значение - подпись кнопки на экране выбора языка.
LANGUAGES = {
    "ru": "🇷🇺 Русский",
    "en": "🇬🇧 English",
    "it": "🇮🇹 Italiano",
    "fr": "🇫🇷 Français",
}

# Язык по умолчанию, если что-то пошло не так и user_data пуст.
DEFAULT_LANG = "ru"

# ============================================================
# ТЕКСТЫ ПО ЯЗЫКАМ
# ============================================================
TEXTS = {
    # ------------------------------------------------------------------
    # РУССКИЙ
    # ------------------------------------------------------------------
    "ru": {
        "brand_header": "Система обучения EmSystem by Yevgeniya Em",
        "welcome_text": (
            "Добро пожаловать!\n\n"
            "Выберите язык, на котором Вам будет удобно проходить обучение."
        ),
        "main_menu_header": "Главное меню:",

        # Кнопки
        "btn_about": "🎓 О курсе",
        "btn_free_lesson": "🎁 Бесплатный урок",
        "btn_works": "🏆 Работы учеников",
        "btn_faq": "❓ FAQ",
        "btn_buy": "💳 Купить курс",
        "btn_watch_free_lesson": "➡ Посмотреть бесплатный урок",
        "btn_main_menu": "⬅ Главное меню",
        "btn_to_buy": "💳 Перейти к покупке",
        "btn_back_to_faq": "⬅ К вопросам",
        "btn_home": "🏠 Главное меню",
        "btn_language": "🌐 Язык",
        "choose_language_text": "Выберите язык интерфейса:",

        # Экран "О курсе"
        "about_caption": (
            "Меня зовут Евгения Эм.\n\n"
            "Я — чемпион мира, международный судья и автор метода Emsystem.me.\n\n"
            "За годы практики я разработала систему, которая позволяет создавать "
            "естественные, чистые и предсказуемые результаты в технике микроблейдинга.\n\n"
            "Этот курс — не просто запись процедуры. Это пошаговая система, по "
            "которой уже обучились мастера из разных стран мира."
        ),

        # Экран "Бесплатный урок"
        "free_lesson_intro": "Один действительно полезный урок.",
        "free_lesson_after": (
            "Если этот урок оказался для Вас полезным, представьте, сколько "
            "практических знаний Вы получите в полном курсе."
        ),

        # Экран "Работы учеников"
        "student_works_text": (
            "🏆 Работы учеников\n\n"
            "Здесь собраны примеры до/после, отзывы, сертификаты выпускниц "
            "и видео с процессом работы.\n\n"
            "Выберите, что хотите посмотреть:"
        ),
        "btn_works_before_after": "🔄 До/после",
        "btn_works_reviews": "💬 Отзывы",
        "btn_works_certificates": "📜 Сертификаты",
        "btn_works_videos": "🎥 Видео",
        "btn_works_more": "➡ Показать ещё",
        "works_before_after_intro": "🔄 Примеры работ до/после:",
        "works_reviews_intro": "💬 Отзывы наших учениц:",
        "works_certificates_intro": "📜 Сертификаты выпускниц:",
        "works_videos_intro": "🎥 Несколько видео с процессом работы:",
        "works_photos_done": "Это все фото в этой категории 🙂",
        "works_continue_prompt": "Хотите посмотреть ещё?",

        # FAQ
        "faq_intro_text": "❓ Часто задаваемые вопросы\n\nВыберите интересующий Вас вопрос:",
        "faq_items": [
            (
                "1. Языки курса",
                "На каких языках доступен курс?",
                "Курс полностью переведен на 10 языков и озвучен профессиональными "
                "дикторами.\n\nВам не придется отвлекаться на чтение субтитров — Вы "
                "сможете полностью сосредоточиться на технике выполнения процедуры, "
                "деталях работы и качестве результата.\n\nТакой формат делает обучение "
                "максимально комфортным и помогает быстрее усваивать материал и сразу "
                "применять знания на практике.",
            ),
            (
                "2. Срок доступа",
                "На какой срок предоставляется доступ?",
                "После покупки Вы получаете доступ к курсу на 1 год.\n\nВы сможете "
                "проходить обучение в удобном для себя темпе, возвращаться к любому "
                "уроку перед работой с клиентом, повторять сложные техники и "
                "закреплять материал столько раз, сколько потребуется.",
            ),
            (
                "3. Сертификат",
                "Получу ли я сертификат?",
                "Да.\n\nПосле успешного завершения обучения Вы получите именной "
                "сертификат о прохождении системы обучения «EmSystem by Yevgeniya Em».\n\n"
                "Сертификат можно использовать для пополнения профессионального "
                "портфолио и подтверждения прохождения обучения.",
            ),
            (
                "4. Для опытных мастеров",
                "Я уже опытный мастер. Будет ли курс полезен?",
                "Да.\n\nEmSystem by Yevgeniya Em — это не базовый курс и не повторение "
                "общеизвестной информации.\n\nЭто авторская система, в которой собраны "
                "детали и техники, напрямую влияющие на скорость работы, чистоту "
                "исполнения, качество заживших результатов и уверенность мастера.\n\n"
                "Если Вы хотите не просто выполнять процедуру, а создавать работы, "
                "которые выделяются среди других, работать быстрее и получать "
                "стабильный предсказуемый результат, этот курс станет для Вас "
                "ценным профессиональным инструментом.",
            ),
            (
                "5. Для новичков",
                "А если я новичок?",
                "Да.\n\nЭто одно из главных преимуществ курса.\n\nОн разработан таким "
                "образом, чтобы обучение было понятным даже тем, кто только начинает "
                "свой путь в профессии.\n\nВсе уроки выстроены в последовательную "
                "систему — от простого к более сложному.\n\nШаг за шагом Вы освоите "
                "технику, научитесь уверенно выполнять процедуру, создавать красивые "
                "зажившие результаты и сможете значительно повысить стоимость своих "
                "услуг.\n\nГлавное — внимательно проходить обучение и применять "
                "полученные знания на практике.",
            ),
            (
                "6. Просмотр с телефона",
                "Смогу ли я смотреть курс с телефона?",
                "Да.\n\nКурс полностью адаптирован для просмотра как с телефона, "
                "так и с планшета или компьютера. Вы сможете обучаться в любом "
                "удобном месте.",
            ),
            (
                "7. Материалы для обучения",
                "Нужны ли специальные материалы для обучения?",
                "Для просмотра курса специальные материалы не требуются.\n\nЕсли Вы "
                "планируете сразу отрабатывать технику на практике, в каждом уроке "
                "Вы увидите используемые инструменты и сможете заранее подготовить "
                "необходимые материалы.",
            ),
        ],

        # Экран "Купить курс"
        "buy_text": "Отличный выбор! Нажмите кнопку ниже, чтобы перейти к покупке курса:",

        # Неизвестная команда
        "unknown_command": "Пожалуйста, пользуйтесь кнопками меню. Чтобы начать заново — /start",

        # Сообщения об ошибках видео
        "video_unavailable": (
            "⚠️ Видео временно недоступно. (Не задан VIDEO_..._FILE_ID / файл не "
            "найден по пути VIDEO_..._PATH — см. config.py)"
        ),
        "video_send_failed": (
            "⚠️ Не удалось загрузить видео. Проверьте file_id/путь и размер файла "
            "(лимит Bot API — 50 МБ)."
        ),
    },

    # ------------------------------------------------------------------
    # ИТАЛЬЯНСКИЙ
    # ------------------------------------------------------------------
    "it": {
        "brand_header": "Sistema di formazione EmSystem by Yevgeniya Em",
        "welcome_text": (
            "Benvenuto/a!\n\n"
            "Scegli la lingua in cui preferisci seguire la formazione."
        ),
        "main_menu_header": "Menu principale:",

        "btn_about": "🎓 Il corso",
        "btn_free_lesson": "🎁 Lezione gratuita",
        "btn_works": "🏆 Lavori delle allieve",
        "btn_faq": "❓ FAQ",
        "btn_buy": "💳 Acquista il corso",
        "btn_watch_free_lesson": "➡ Guarda la lezione gratuita",
        "btn_main_menu": "⬅ Menu principale",
        "btn_to_buy": "💳 Vai all'acquisto",
        "btn_back_to_faq": "⬅ Alle domande",
        "btn_home": "🏠 Menu principale",
        "btn_language": "🌐 Lingua",
        "choose_language_text": "Scegli la lingua dell'interfaccia:",

        "about_caption": (
            "Mi chiamo Yevgeniya Em.\n\n"
            "Sono campionessa del mondo, giudice internazionale e autrice del "
            "metodo Emsystem.me.\n\n"
            "In anni di pratica ho sviluppato un sistema che permette di ottenere "
            "risultati naturali, puliti e prevedibili nella tecnica del microblading.\n\n"
            "Questo corso non è semplicemente la registrazione di una procedura. "
            "È un sistema passo dopo passo, grazie al quale si sono già formate "
            "specialiste di tutto il mondo."
        ),

        "free_lesson_intro": "Una lezione davvero utile.",
        "free_lesson_after": (
            "Se questa lezione ti è stata utile, immagina quante conoscenze "
            "pratiche riceverai nel corso completo."
        ),

        "student_works_text": (
            "🏆 Lavori delle allieve\n\n"
            "Qui trovi esempi di prima/dopo, recensioni, certificati delle "
            "diplomate e video del processo di lavoro.\n\n"
            "Scegli cosa vuoi vedere:"
        ),
        "btn_works_before_after": "🔄 Prima/dopo",
        "btn_works_reviews": "💬 Recensioni",
        "btn_works_certificates": "📜 Certificati",
        "btn_works_videos": "🎥 Video",
        "btn_works_more": "➡ Mostra altro",
        "works_before_after_intro": "🔄 Esempi di lavori prima/dopo:",
        "works_reviews_intro": "💬 Recensioni delle nostre allieve:",
        "works_certificates_intro": "📜 Certificati delle diplomate:",
        "works_videos_intro": "🎥 Alcuni video del processo di lavoro:",
        "works_photos_done": "Sono tutte le foto di questa categoria 🙂",
        "works_continue_prompt": "Vuoi vederne altre?",

        "faq_intro_text": "❓ Domande frequenti\n\nScegli la domanda che ti interessa:",
        "faq_items": [
            (
                "1. Lingue del corso",
                "In quali lingue è disponibile il corso?",
                "Il corso è completamente tradotto in 10 lingue ed è doppiato da "
                "speaker professionisti.\n\nNon dovrai distrarti a leggere i "
                "sottotitoli — potrai concentrarti pienamente sulla tecnica di "
                "esecuzione della procedura, sui dettagli del lavoro e sulla "
                "qualità del risultato.\n\nQuesto formato rende l'apprendimento il "
                "più confortevole possibile e aiuta ad assimilare il materiale più "
                "velocemente, applicando subito le conoscenze nella pratica.",
            ),
            (
                "2. Durata dell'accesso",
                "Per quanto tempo viene fornito l'accesso?",
                "Dopo l'acquisto ricevi l'accesso al corso per 1 anno.\n\nPotrai "
                "seguire la formazione al tuo ritmo, tornare a qualsiasi lezione "
                "prima di lavorare con una cliente, ripetere le tecniche più "
                "complesse e consolidare il materiale tutte le volte che serve.",
            ),
            (
                "3. Certificato",
                "Riceverò un certificato?",
                "Sì.\n\nDopo aver completato con successo la formazione riceverai "
                "un certificato nominativo di completamento del sistema di "
                "formazione «EmSystem by Yevgeniya Em».\n\nIl certificato può "
                "essere utilizzato per arricchire il tuo portfolio professionale "
                "e per confermare la formazione seguita.",
            ),
            (
                "4. Per specialiste esperte",
                "Sono già una specialista esperta. Il corso mi sarà utile?",
                "Sì.\n\nEmSystem by Yevgeniya Em non è un corso base né una "
                "ripetizione di informazioni generiche.\n\nÈ un sistema originale "
                "che raccoglie dettagli e tecniche che influiscono direttamente "
                "sulla velocità di lavoro, sulla pulizia dell'esecuzione, sulla "
                "qualità dei risultati guariti e sulla sicurezza della "
                "specialista.\n\nSe vuoi non solo eseguire la procedura, ma creare "
                "lavori che si distinguono dagli altri, lavorare più velocemente e "
                "ottenere un risultato stabile e prevedibile, questo corso "
                "diventerà per te uno strumento professionale prezioso.",
            ),
            (
                "5. Per principianti",
                "E se sono una principiante?",
                "Sì, va bene anche per te.\n\nQuesto è uno dei principali vantaggi "
                "del corso.\n\nÈ stato progettato in modo che la formazione sia "
                "comprensibile anche per chi sta muovendo i primi passi nella "
                "professione.\n\nTutte le lezioni sono organizzate in un sistema "
                "sequenziale — dal semplice al più complesso.\n\nPasso dopo passo "
                "imparerai la tecnica, acquisirai sicurezza nell'eseguire la "
                "procedura, creerai bellissimi risultati guariti e potrai "
                "aumentare notevolmente il prezzo dei tuoi servizi.\n\nL'importante "
                "è seguire attentamente la formazione e applicare le conoscenze "
                "acquisite nella pratica.",
            ),
            (
                "6. Visione da smartphone",
                "Potrò seguire il corso dallo smartphone?",
                "Sì.\n\nIl corso è completamente adattato per essere visto sia da "
                "smartphone, sia da tablet o computer. Potrai studiare ovunque ti "
                "sia comodo.",
            ),
            (
                "7. Materiali per la formazione",
                "Servono materiali speciali per la formazione?",
                "Per seguire il corso non sono necessari materiali speciali.\n\n"
                "Se hai intenzione di esercitarti subito nella pratica, in ogni "
                "lezione vedrai gli strumenti utilizzati e potrai preparare in "
                "anticipo i materiali necessari.",
            ),
        ],

        "buy_text": (
            "Ottima scelta! Premi il pulsante qui sotto per procedere "
            "all'acquisto del corso:"
        ),

        "unknown_command": "Per favore, usa i pulsanti del menu. Per ricominciare — /start",

        "video_unavailable": (
            "⚠️ Il video non è al momento disponibile. (VIDEO_..._FILE_ID non "
            "impostato / file non trovato nel percorso VIDEO_..._PATH — vedi config.py)"
        ),
        "video_send_failed": (
            "⚠️ Impossibile caricare il video. Controlla file_id/percorso e la "
            "dimensione del file (limite Bot API — 50 MB)."
        ),
    },

    # ------------------------------------------------------------------
    # ФРАНЦУЗСКИЙ
    # ------------------------------------------------------------------
    "fr": {
        "brand_header": "Système de formation EmSystem by Yevgeniya Em",
        "welcome_text": (
            "Bienvenue !\n\n"
            "Choisissez la langue dans laquelle vous souhaitez suivre la formation."
        ),
        "main_menu_header": "Menu principal :",

        "btn_about": "🎓 À propos du cours",
        "btn_free_lesson": "🎁 Leçon gratuite",
        "btn_works": "🏆 Travaux des élèves",
        "btn_faq": "❓ FAQ",
        "btn_buy": "💳 Acheter le cours",
        "btn_watch_free_lesson": "➡ Voir la leçon gratuite",
        "btn_main_menu": "⬅ Menu principal",
        "btn_to_buy": "💳 Passer à l'achat",
        "btn_back_to_faq": "⬅ Retour aux questions",
        "btn_home": "🏠 Menu principal",
        "btn_language": "🌐 Langue",
        "choose_language_text": "Choisissez la langue de l'interface :",

        "about_caption": (
            "Je m'appelle Yevgeniya Em.\n\n"
            "Je suis championne du monde, juge internationale et auteure de la "
            "méthode Emsystem.me.\n\n"
            "Au fil de mes années de pratique, j'ai développé un système qui "
            "permet d'obtenir des résultats naturels, nets et prévisibles dans la "
            "technique du microblading.\n\n"
            "Ce cours n'est pas simplement l'enregistrement d'une procédure. "
            "C'est un système progressif, étape par étape, grâce auquel des "
            "spécialistes du monde entier se sont déjà formées."
        ),

        "free_lesson_intro": "Une leçon vraiment utile.",
        "free_lesson_after": (
            "Si cette leçon vous a été utile, imaginez la quantité de "
            "connaissances pratiques que vous obtiendrez dans le cours complet."
        ),

        "student_works_text": (
            "🏆 Travaux des élèves\n\n"
            "Vous trouverez ici des exemples avant/après, des avis, des "
            "certificats des diplômées et des vidéos du processus de "
            "travail.\n\n"
            "Choisissez ce que vous voulez voir :"
        ),
        "btn_works_before_after": "🔄 Avant/après",
        "btn_works_reviews": "💬 Avis",
        "btn_works_certificates": "📜 Certificats",
        "btn_works_videos": "🎥 Vidéos",
        "btn_works_more": "➡ Voir plus",
        "works_before_after_intro": "🔄 Exemples de travaux avant/après :",
        "works_reviews_intro": "💬 Avis de nos élèves :",
        "works_certificates_intro": "📜 Certificats des diplômées :",
        "works_videos_intro": "🎥 Quelques vidéos du processus de travail :",
        "works_photos_done": "Ce sont toutes les photos de cette catégorie 🙂",
        "works_continue_prompt": "Voulez-vous en voir plus ?",

        "faq_intro_text": "❓ Questions fréquentes\n\nChoisissez la question qui vous intéresse :",
        "faq_items": [
            (
                "1. Langues du cours",
                "Dans quelles langues le cours est-il disponible ?",
                "Le cours est entièrement traduit en 10 langues et doublé par des "
                "professionnels.\n\nVous n'aurez pas besoin de lire des "
                "sous-titres — vous pourrez vous concentrer entièrement sur la "
                "technique d'exécution de la procédure, les détails du travail et "
                "la qualité du résultat.\n\nCe format rend l'apprentissage le plus "
                "confortable possible et aide à assimiler la matière plus "
                "rapidement, tout en appliquant immédiatement les connaissances "
                "en pratique.",
            ),
            (
                "2. Durée d'accès",
                "Pour combien de temps l'accès est-il accordé ?",
                "Après l'achat, vous obtenez l'accès au cours pendant 1 an.\n\n"
                "Vous pourrez suivre la formation à votre rythme, revenir sur "
                "n'importe quelle leçon avant de travailler avec une cliente, "
                "répéter les techniques complexes et consolider la matière autant "
                "de fois que nécessaire.",
            ),
            (
                "3. Certificat",
                "Recevrai-je un certificat ?",
                "Oui.\n\nAprès avoir terminé la formation avec succès, vous "
                "recevrez un certificat nominatif attestant la réussite du "
                "système de formation « EmSystem by Yevgeniya Em ».\n\nCe "
                "certificat peut être utilisé pour enrichir votre portfolio "
                "professionnel et attester de votre formation.",
            ),
            (
                "4. Pour les spécialistes expérimentées",
                "Je suis déjà une spécialiste expérimentée. Le cours me sera-t-il utile ?",
                "Oui.\n\nEmSystem by Yevgeniya Em n'est pas un cours de base ni "
                "une répétition d'informations générales.\n\nC'est un système "
                "original qui rassemble des détails et des techniques ayant un "
                "impact direct sur la vitesse de travail, la précision "
                "d'exécution, la qualité des résultats cicatrisés et la "
                "confiance de la spécialiste.\n\nSi vous souhaitez non seulement "
                "exécuter la procédure, mais créer des réalisations qui se "
                "démarquent, travailler plus vite et obtenir un résultat stable "
                "et prévisible, ce cours deviendra pour vous un outil "
                "professionnel précieux.",
            ),
            (
                "5. Pour les débutantes",
                "Et si je suis débutante ?",
                "Oui, c'est fait pour vous aussi.\n\nC'est l'un des principaux "
                "avantages du cours.\n\nIl est conçu pour que la formation soit "
                "compréhensible même pour celles qui commencent tout juste dans "
                "la profession.\n\nToutes les leçons sont organisées de manière "
                "progressive — du plus simple au plus complexe.\n\nÉtape par "
                "étape, vous maîtriserez la technique, apprendrez à exécuter la "
                "procédure avec assurance, créerez de beaux résultats cicatrisés "
                "et pourrez augmenter significativement le prix de vos "
                "prestations.\n\nL'essentiel est de suivre attentivement la "
                "formation et d'appliquer les connaissances acquises en pratique.",
            ),
            (
                "6. Visionnage depuis un téléphone",
                "Pourrai-je regarder le cours depuis mon téléphone ?",
                "Oui.\n\nLe cours est entièrement adapté pour être visionné aussi "
                "bien depuis un téléphone que depuis une tablette ou un "
                "ordinateur. Vous pourrez vous former où que ce soit, en tout "
                "confort.",
            ),
            (
                "7. Matériel pour la formation",
                "Faut-il du matériel spécial pour la formation ?",
                "Aucun matériel spécial n'est nécessaire pour suivre le cours.\n\n"
                "Si vous prévoyez de pratiquer immédiatement la technique, "
                "chaque leçon vous montrera les outils utilisés et vous pourrez "
                "préparer à l'avance le matériel nécessaire.",
            ),
        ],

        "buy_text": (
            "Excellent choix ! Cliquez sur le bouton ci-dessous pour procéder à "
            "l'achat du cours :"
        ),

        "unknown_command": "Veuillez utiliser les boutons du menu. Pour recommencer — /start",

        "video_unavailable": (
            "⚠️ La vidéo est temporairement indisponible. (VIDEO_..._FILE_ID non "
            "défini / fichier introuvable au chemin VIDEO_..._PATH — voir config.py)"
        ),
        "video_send_failed": (
            "⚠️ Impossible de charger la vidéo. Vérifiez le file_id/chemin et la "
            "taille du fichier (limite Bot API — 50 Mo)."
        ),
    },

    # ------------------------------------------------------------------
    # АНГЛИЙСКИЙ
    # ------------------------------------------------------------------
    "en": {
        "brand_header": "EmSystem by Yevgeniya Em Training System",
        "welcome_text": (
            "Welcome!\n\n"
            "Please choose the language you'd like to use for the training."
        ),
        "main_menu_header": "Main menu:",

        # Buttons
        "btn_about": "🎓 About the course",
        "btn_free_lesson": "🎁 Free lesson",
        "btn_works": "🏆 Student works",
        "btn_faq": "❓ FAQ",
        "btn_buy": "💳 Buy the course",
        "btn_watch_free_lesson": "➡ Watch the free lesson",
        "btn_main_menu": "⬅ Main menu",
        "btn_to_buy": "💳 Proceed to purchase",
        "btn_back_to_faq": "⬅ Back to questions",
        "btn_home": "🏠 Main menu",
        "btn_language": "🌐 Language",
        "choose_language_text": "Choose your interface language:",

        # "About the course" screen
        "about_caption": (
            "My name is Yevgeniya Em.\n\n"
            "I'm a world champion, an international judge, and the author of "
            "the Emsystem.me method.\n\n"
            "Over years of practice I've developed a system that lets you "
            "create natural, clean, and predictable results in the "
            "microblading technique.\n\n"
            "This course isn't just a recording of a procedure. It's a "
            "step-by-step system that specialists from many countries around "
            "the world have already trained with."
        ),

        # "Free lesson" screen
        "free_lesson_intro": "One genuinely useful lesson.",
        "free_lesson_after": (
            "If this lesson was useful to you, imagine how much practical "
            "knowledge you'll get from the full course."
        ),

        # "Student works" screen
        "student_works_text": (
            "🏆 Student works\n\n"
            "Here you'll find before/after examples, reviews, graduate "
            "certificates, and videos of the work process.\n\n"
            "Choose what you'd like to see:"
        ),
        "btn_works_before_after": "🔄 Before/after",
        "btn_works_reviews": "💬 Reviews",
        "btn_works_certificates": "📜 Certificates",
        "btn_works_videos": "🎥 Videos",
        "btn_works_more": "➡ Show more",
        "works_before_after_intro": "🔄 Before/after examples:",
        "works_reviews_intro": "💬 Reviews from our students:",
        "works_certificates_intro": "📜 Graduate certificates:",
        "works_videos_intro": "🎥 A few videos of the work process:",
        "works_photos_done": "That's all the photos in this category 🙂",
        "works_continue_prompt": "Want to see more?",

        # FAQ
        "faq_intro_text": "❓ Frequently asked questions\n\nChoose a question you're interested in:",
        "faq_items": [
            (
                "1. Course languages",
                "What languages is the course available in?",
                "The course is fully translated into 10 languages and voiced "
                "by professional narrators.\n\nYou won't need to be "
                "distracted by reading subtitles — you'll be able to focus "
                "entirely on the procedure technique, work details, and "
                "quality of the result.\n\nThis format makes learning as "
                "comfortable as possible and helps you absorb the material "
                "faster while applying it in practice right away.",
            ),
            (
                "2. Access period",
                "How long is access provided for?",
                "After purchase you get access to the course for 1 year.\n\n"
                "You'll be able to go through the training at your own pace, "
                "return to any lesson before working with a client, repeat "
                "complex techniques, and reinforce the material as many "
                "times as you need.",
            ),
            (
                "3. Certificate",
                "Will I receive a certificate?",
                "Yes.\n\nAfter successfully completing the training you'll "
                "receive a personalized certificate confirming completion of "
                "the «EmSystem by Yevgeniya Em» training system.\n\nThe "
                "certificate can be used to build up your professional "
                "portfolio and confirm you've completed the training.",
            ),
            (
                "4. For experienced specialists",
                "I'm already an experienced specialist. Will the course be useful to me?",
                "Yes.\n\nEmSystem by Yevgeniya Em is not a basic course or a "
                "repeat of commonly known information.\n\nIt's an original "
                "system that brings together details and techniques that "
                "directly affect work speed, precision of execution, the "
                "quality of healed results, and the specialist's "
                "confidence.\n\nIf you want to not just perform the "
                "procedure but create work that stands out, work faster, and "
                "get stable, predictable results, this course will become a "
                "valuable professional tool for you.",
            ),
            (
                "5. For beginners",
                "What if I'm a beginner?",
                "Yes, it's for you too.\n\nThis is one of the course's main "
                "advantages.\n\nIt's designed so that the training is "
                "understandable even for those who are just starting out in "
                "the profession.\n\nAll lessons are structured sequentially "
                "— from simple to more complex.\n\nStep by step you'll "
                "master the technique, learn to perform the procedure with "
                "confidence, create beautiful healed results, and be able "
                "to significantly raise the price of your services.\n\nThe "
                "main thing is to go through the training attentively and "
                "apply the knowledge you gain in practice.",
            ),
            (
                "6. Watching from a phone",
                "Will I be able to watch the course from my phone?",
                "Yes.\n\nThe course is fully adapted for viewing from a "
                "phone, a tablet, or a computer. You'll be able to train "
                "wherever is convenient for you.",
            ),
            (
                "7. Materials needed for training",
                "Do I need any special materials for the training?",
                "No special materials are needed to watch the course.\n\n"
                "If you're planning to practice the technique right away, "
                "each lesson will show you the tools used so you can "
                "prepare the necessary materials in advance.",
            ),
        ],

        "buy_text": (
            "Great choice! Press the button below to proceed to purchasing "
            "the course:"
        ),

        "unknown_command": "Please use the menu buttons. To start over — /start",

        "video_unavailable": (
            "⚠️ The video is temporarily unavailable. (VIDEO_..._FILE_ID is not "
            "set / file not found at VIDEO_..._PATH — see config.py)"
        ),
        "video_send_failed": (
            "⚠️ Failed to upload the video. Check the file_id/path and file "
            "size (Bot API limit — 50 MB)."
        ),
    },
}
