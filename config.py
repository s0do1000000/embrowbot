# -*- coding: utf-8 -*-
"""
Конфигурация бота EmSystem by Yevgeniya Em.

Бот поддерживает 4 языка интерфейса: русский, английский, итальянский, французский.
Все тексты, кнопки и FAQ переведены на каждый язык и лежат в словаре TEXTS.
"""

import os

# ============================================================
# ТОКЕН БОТА
# ============================================================
BOT_TOKEN = os.getenv("BOT_TOKEN", "8582789594:AAEQBRo3D6DvWNF_bMLIpn7zOUmmwzAPszw")

# ============================================================
# ССЫЛКА НА ПОКУПКУ КУРСА
# ============================================================
BUY_URL = "http://emsystem.me/"

# ============================================================
# ВИДЕО (СВОЁ ДЛЯ КАЖДОГО ЯЗЫКА)
# ============================================================
# Для каждого языка — свой file_id (или свой путь к файлу как запасной
# вариант). Если для какого-то языка file_id ещё не готов, оставьте
# пустую строку "" — тогда бот покажет видео языка по умолчанию (ru)
# вместо пустого экрана.
VIDEO_ABOUT_FILE_ID_BY_LANG = {
    "ru": os.getenv("VIDEO_ABOUT_FILE_ID_RU", "BAACAgIAAxkBAAPIanSS4GULisUdJIhMrhf2l0kLcGkAAnOpAAIBCKhLBKjMThbFhmI9BA"),
    "en": os.getenv("VIDEO_ABOUT_FILE_ID_EN", "BAACAgIAAxkBAAIGfWp6H1djsaKxytETxyNm403BUEEUAALGoQACnU_QS5zhNnI0eAT9PQQ"),
    "it": os.getenv("VIDEO_ABOUT_FILE_ID_IT", "BAACAgIAAxkBAAIGe2p6HxkBNqLXrBfZcKZ2GgvjJTQCAALDoQACnU_QS3Rg5DL8YVAVPQQ"),
    "fr": os.getenv("VIDEO_ABOUT_FILE_ID_FR", "BAACAgIAAxkBAAIGeWp6HsAkjO7nNvWf6qb9UK5kIkL0AALCoQACnU_QS8FkEC8NirTGPQQ"),
}
VIDEO_ABOUT_PATH_BY_LANG = {
    "ru": os.getenv("VIDEO_ABOUT_PATH_RU", "assets/welcome_ru.mp4"),
    "en": os.getenv("VIDEO_ABOUT_PATH_EN", "assets/welcome_en.mp4"),
    "it": os.getenv("VIDEO_ABOUT_PATH_IT", "assets/welcome_it.mp4"),
    "fr": os.getenv("VIDEO_ABOUT_PATH_FR", "assets/welcome_fr.mp4"),
}

VIDEO_LESSON_FILE_ID_BY_LANG = {
    "ru": os.getenv("VIDEO_LESSON_FILE_ID_RU", "BAACAgIAAxkBAAPKanSS8DlSBVt1zl6F0ync7DOvh50AAnWpAAIBCKhLduBuY83Dy0o9BA"),
    "en": os.getenv("VIDEO_LESSON_FILE_ID_EN", "BAACAgIAAxkBAAIGf2p6H6ovwOoQAAH1q3jKiqJKY86NwwACyaEAAp1P0Esr05_-7xEcUj0E"),
    "it": os.getenv("VIDEO_LESSON_FILE_ID_IT", "BAACAgIAAxkBAAIGg2p6IB6kkRwej5M6G6o65AKOfoqxAALLoQACnU_QS7suKp66LH_1PQQ"),
    "fr": os.getenv("VIDEO_LESSON_FILE_ID_FR", "BAACAgIAAxkBAAIGgWp6H-mG2ZJUhJDKagMAAalybaKEnAACyqEAAp1P0EsoHhJO7NX_eT0E"),
}
VIDEO_LESSON_PATH_BY_LANG = {
    "ru": os.getenv("VIDEO_LESSON_PATH_RU", "assets/welcome2_ru.mp4"),
    "en": os.getenv("VIDEO_LESSON_PATH_EN", "assets/welcome2_en.mp4"),
    "it": os.getenv("VIDEO_LESSON_PATH_IT", "assets/welcome2_it.mp4"),
    "fr": os.getenv("VIDEO_LESSON_PATH_FR", "assets/welcome2_fr.mp4"),
}

# ============================================================
# МЕДИА ДЛЯ РАЗДЕЛА "РАБОТЫ УЧЕНИКОВ"
# ============================================================
WORKS_PHOTOS_PAGE_SIZE = 10

WORKS_VIDEOS = [
    "BAACAgIAAxkBAAIBamp0xKppSI1rZxFZYSvHO44ic4aOAALtqwACAQioS8f37phu3na7PQQ",
    "BAACAgIAAxkBAAIBa2p0xKpudDQiB5g4WmE2k4wIvRwQAALuqwACAQioS116B1VdD_FXPQQ",
    "BAACAgIAAxkBAAIBbGp0xKqQo_TNgLYxzHVuD-dnln8RAALvqwACAQioS28Zo_BoTZKlPQQ",
]

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

WORKS_CATEGORIES = {
    "before_after": {"type": "photo", "items": WORKS_PHOTOS_BEFORE_AFTER},
    "reviews": {"type": "photo", "items": WORKS_PHOTOS_REVIEWS},
    "certificates": {"type": "photo", "items": WORKS_PHOTOS_CERTIFICATES},
    "videos": {"type": "video", "items": WORKS_VIDEOS},
}

# ============================================================
# ЯЗЫКИ
# ============================================================
LANGUAGES = {
    "ru": "🇷🇺 Русский",
    "en": "🇬🇧 English",
    "it": "🇮🇹 Italiano",
    "fr": "🇫🇷 Français",
}

DEFAULT_LANG = "ru"

# ============================================================
# ТЕКСТЫ ПО ЯЗЫКАМ
# ============================================================
TEXTS = {
    "ru": {
        "brand_header": "Система обучения EmSystem by Yevgeniya Em",
        "welcome_text": (
            "Добро пожаловать!\n\n"
            "Выберите язык, на котором Вам будет удобно проходить обучение."
        ),
        "main_menu_header": "Главное меню:",

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

        "about_caption": (
            "Меня зовут Евгения Эм.\n\n"
            "Я — чемпион мира, международный судья и автор метода Emsystem.me.\n\n"
            "За годы практики я разработала систему, которая позволяет создавать "
            "естественные, чистые и предсказуемые результаты в технике микроблейдинга.\n\n"
            "Этот курс — не просто запись процедуры. Это пошаговая система, по "
            "которой уже обучились мастера из разных стран мира."
        ),

        "free_lesson_intro": "Один действительно полезный урок.",
        "free_lesson_after": (
            "Если этот урок оказался для Вас полезным, представьте, сколько "
            "практических знаний Вы получите в полном курсе."
        ),

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

        "faq_intro_text": "❓ Часто задаваемые вопросы\n\nВыберите интересующий Вас вопрос:",
        "faq_items": [
            (
                "1. Языки курса",
                "На каких языках доступен курс?",
                "Курс полностью переведен на 10 языков и озвучен профессиональными дикторами.\n\nВам не придется отвлекаться на чтение субтитров — Вы сможете полностью сосредоточиться на технике выполнения процедуры, деталях работы и качестве результата.\n\nТакой формат делает обучение максимально комфортным и помогает быстрее усваивать материал и сразу применять знания на практике.",
            ),
            (
                "2. Срок доступа",
                "На какой срок предоставляется доступ?",
                "После покупки Вы получаете доступ к курсу на 1 год.\n\nВы сможете проходить обучение в удобном для себя темпе, возвращаться к любому уроку перед работой с клиентом, повторять сложные техники и закреплять материал столько раз, сколько потребуется.",
            ),
            (
                "3. Сертификат",
                "Получу ли я сертификат?",
                "Да.\n\nПосле успешного завершения обучения Вы получите именной сертификат о прохождении системы обучения «EmSystem by Yevgeniya Em».\n\nСертификат можно использовать для пополнения профессионального портфолио и подтверждения прохождения обучения.",
            ),
            (
                "4. Для опытных мастеров",
                "Я уже опытный мастер. Будет ли курс полезен?",
                "Да.\n\nEmSystem by Yevgeniya Em — это не базовый курс и не повторение общеизвестной информации.\n\nЭто авторская система, в которой собраны детали и техники, напрямую влияющие на скорость работы, чистоту исполнения, качество заживших результатов и уверенность мастера.\n\nЕсли Вы хотите не просто выполнять процедуру, а создавать работы, которые выделяются среди других, работать быстрее и получать стабильный предсказуемый результат, этот курс станет для Вас ценным профессиональным инструментом.",
            ),
            (
                "5. Для новичков",
                "А если я новичок?",
                "Да.\n\nЭто одно из главных преимуществ курса.\n\nОн разработан таким образом, чтобы обучение было понятным даже тем, кто только начинает свой путь в профессии.\n\nВсе уроки выстроены в последовательную систему — от простого к более сложному.\n\nШаг за шагом Вы освоите технику, научитесь уверенно выполнять процедуру, создавать красивые зажившие результаты и сможете значительно повысить стоимость своих услуг.\n\nГлавное — внимательно проходить обучение и применять полученные знания на практике.",
            ),
            (
                "6. Просмотр с телефона",
                "Смогу ли я смотреть курс с телефона?",
                "Да.\n\nКурс полностью адаптирован для просмотра как с телефона, так и с планшета или компьютера. Вы сможете обучаться в любом удобном месте.",
            ),
            (
                "7. Материалы для обучения",
                "Нужны ли специальные материалы для обучения?",
                "Для просмотра курса специальные материалы не требуются.\n\nЕсли Вы планируете сразу отрабатывать технику на практике, в каждом уроке Вы увидите используемые инструменты и сможете заранее подготовить необходимые материалы.",
            ),
        ],

        "buy_text": "Отличный выбор! Нажмите кнопку ниже, чтобы перейти к покупке курса:",
        "unknown_command": "Пожалуйста, пользуйтесь кнопками меню. Чтобы начать заново — /start",
        "video_unavailable": "⚠️ Видео временно недоступно.",
        "video_send_failed": "⚠️ Не удалось загрузить видео. Проверьте лимит размера (до 50 МБ).",
    },
    "it": {
        "brand_header": "Sistema di formazione EmSystem by Yevgeniya Em",
        "welcome_text": "Benvenuto/a!\n\nScegli la lingua in cui preferisci seguire la formazione.",
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
            "Sono campionessa del mondo, giudice internazionale e autrice del metodo Emsystem.me.\n\n"
            "In anni di pratica ho sviluppato un sistema che permette di ottenere risultati naturali, puliti e prevedibili nella tecnica del microblading.\n\n"
            "Questo corso non è semplicemente la registrazione di una procedura. È un sistema passo dopo passo, grazie al quale si sono già formate specialiste di tutto il mondo."
        ),
        "free_lesson_intro": "Una lezione davvero utile.",
        "free_lesson_after": "Se questa lezione ti è stata utile, immagina quante conoscenze pratiche riceverai nel corso completo.",
        "student_works_text": "🏆 Lavori delle allieve\n\nQui trovi esempi di prima/dopo, recensioni, certificati delle diplomate e video del processo di lavoro.\n\nScegli cosa vuoi vedere:",
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
            ("1. Lingue del corso", "In quali lingue è disponibile il corso?", "Il corso è completamente tradotto in 10 lingue ed è doppiato da speaker professionisti."),
            ("2. Durata dell'accesso", "Per quanto tempo viene fornito l'accesso?", "Dopo l'acquisto ricevi l'accesso al corso per 1 anno."),
            ("3. Certificato", "Riceverò un certificato?", "Sì. Riceverai un certificato nominativo."),
            ("4. Per specialiste esperte", "Sono già una specialista esperta. Il corso mi sarà utile?", "Sì, è un sistema originale con tecniche avanzate."),
            ("5. Per principianti", "E se sono una principiante?", "Sì, è strutturato dal semplice al complesso."),
            ("6. Visione da smartphone", "Potrò seguire il corso dallo smartphone?", "Sì, è completamente adattato."),
            ("7. Materiali per la formazione", "Servono materiali speciali per la formazione?", "No, nessun materiale speciale richiesto per la visione."),
        ],
        "buy_text": "Ottima scelta! Premi il pulsante qui sotto per procedere all'acquisto del corso:",
        "unknown_command": "Per favore, usa i pulsanti del menu. Per ricominciare — /start",
        "video_unavailable": "⚠️ Il video non è al momento disponibile.",
        "video_send_failed": "⚠️ Impossibile caricare il video.",
    },
    "fr": {
        "brand_header": "Système de formation EmSystem by Yevgeniya Em",
        "welcome_text": "Bienvenue !\n\nChoisissez la langue dans laquelle vous souhaitez suivre la formation.",
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
            "Je suis championne du monde, juge internationale et auteure de la méthode Emsystem.me.\n\n"
            "Au fil de mes années de pratique, j'ai développé un système qui permet d'obtenir des résultats naturels, nets et prévisibles dans la technique du microblading."
        ),
        "free_lesson_intro": "Une leçon vraiment utile.",
        "free_lesson_after": "Si cette leçon vous a été utile, imaginez la quantité de connaissances pratiques que vous obtiendrez dans le cours complet.",
        "student_works_text": "🏆 Travaux des élèves\n\nVous trouverez ici des exemples avant/après, des avis, des certificats des diplômées et des vidéos du processus de travail.\n\nChoisissez ce que vous voulez voir :",
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
            ("1. Langues du cours", "Dans quelles langues le cours est-il disponible ?", "Le cours est entièrement traduit en 10 langues."),
            ("2. Durée d'accès", "Pour combien de temps l'accès est-il accordé ?", "Accès pendant 1 an."),
            ("3. Certificat", "Recevrai-je un certificat ?", "Oui, un certificat nominatif."),
            ("4. Pour les spécialistes expérimentées", "Le cours me sera-t-il utile ?", "Oui, il rassemble des détails и техники avancées."),
            ("5. Pour les débutantes", "Et si je suis débutante ?", "Oui, le cours est très détaillé."),
            ("6. Visionnage depuis un téléphone", "Pourrai-je regarder depuis mon téléphone ?", "Oui, totalement adapté."),
            ("7. Matériel pour la formation", "Faut-il du matériel spécial ?", "Aucun matériel spécial n'est nécessaire pour visionner."),
        ],
        "buy_text": "Excellent choix ! Cliquez sur le bouton ci-dessous pour procéder à l'achat du cours :",
        "unknown_command": "Veuillez utiliser les boutons du menu. Pour recommencer — /start",
        "video_unavailable": "⚠️ La vidéo est temporairement indisponible.",
        "video_send_failed": "⚠️ Impossible de charger la vidéo.",
    },
    "en": {
        "brand_header": "EmSystem by Yevgeniya Em Training System",
        "welcome_text": "Welcome!\n\nPlease choose the language you'd like to use for the training.",
        "main_menu_header": "Main menu:",
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
        "about_caption": (
            "My name is Yevgeniya Em.\n\n"
            "I'm a world champion, an international judge, and the author of the Emsystem.me method.\n\n"
            "Over years of practice I've developed a system that lets you create natural, clean, and predictable results in the microblading technique."
        ),
        "free_lesson_intro": "One genuinely useful lesson.",
        "free_lesson_after": "If this lesson was useful to you, imagine how much practical knowledge you'll get from the full course.",
        "student_works_text": "🏆 Student works\n\nHere you'll find before/after examples, reviews, graduate certificates, and videos of the work process.\n\nChoose what you'd like to see:",
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
        "faq_intro_text": "❓ Frequently asked questions\n\nChoose a question you're interested in:",
        "faq_items": [
            ("1. Course languages", "What languages is the course available in?", "Fully translated into 10 languages."),
            ("2. Access period", "How long is access provided for?", "Access for 1 year."),
            ("3. Certificate", "Will I receive a certificate?", "Yes, a personalized certificate."),
            ("4. For experienced specialists", "Will the course be useful to me?", "Yes, it contains specialized techniques."),
            ("5. For beginners", "What if I'm a beginner?", "Yes, structured step-by-step."),
            ("6. Watching from a phone", "Will I be able to watch from my phone?", "Yes, fully responsive."),
            ("7. Materials needed for training", "Do I need any special materials?", "No special materials required for watching."),
        ],
        "buy_text": "Great choice! Press the button below to proceed to purchasing the course:",
        "unknown_command": "Please use the menu buttons. To start over — /start",
        "video_unavailable": "⚠️ The video is temporarily unavailable.",
        "video_send_failed": "⚠️ Failed to upload the video.",
    },
}