# ============================================================
#  ДЕМО: Headroom сжимает контекст для LLM
#  Связь с прошлым уроком про токены!
# ============================================================

import json
import headroom  # библиотека, которую мы установили

# --- 1. Готовим "тяжёлый" вывод инструмента ---
# Представь: агент дёрнул API и получил большой JSON-ответ.
# Такое часто попадает в контекст LLM и стоит МНОГО токенов.
big_json = {
    "users": [
        {
            "id": i,
            "name": f"User {i}",
            "email": f"user{i}@example.com",
            "active": True,
            "roles": ["reader", "writer"],
            "metadata": {"created_at": "2026-07-01T10:00:00Z", "score": 0.0},
        }
        for i in range(40)  # 40 одинаковых по структуре записей
    ],
    "status": "ok",
    "total": 40,
}

# Превращаем словарь в текст (как он реально пришёл бы в модель)
raw_text = json.dumps(big_json, indent=2, ensure_ascii=False)

# --- 2. Оборачиваем в формат сообщений (как для Claude) ---
# compress() ждёт список сообщений с ролями user/assistant
messages = [
    {"role": "user", "content": "Вот ответ API, проанализируй пользователей:"},
    {"role": "assistant", "content": raw_text},
]

# --- 3. Настраиваем сжатие ---
# protect_recent=0 — не защищать последние сообщения (иначе наш JSON
#   считается "свежим" и не сжимается).
# min_tokens_to_compress — сжимать даже небольшие блоки.
config = headroom.CompressConfig(
    protect_recent=0,
    min_tokens_to_compress=100,
    compress_user_messages=True,
)

# Сжимаем! model_limit=1500 — говорим, что окно маленькое,
# значит наш контент (3100 токенов) его переполняет -> Headroom
# вынужден сжимать, чтобы влезть.
result = headroom.compress(messages, model_limit=1500, config=config)

# --- 4. Смотрим результат ---
print("=" * 50)
print("РЕЗУЛЬТАТ СЖАТИЯ HEADROOM")
print("=" * 50)
print(f"Токенов ДО:      {result.tokens_before}")
print(f"Токенов ПОСЛЕ:   {result.tokens_after}")
print(f"Сэкономлено:     {result.tokens_saved}")
# compression_ratio — доля оставшегося (например 0.35 = осталось 35%)
print(f"Коэффициент:     {result.compression_ratio:.2f}")

# Считаем экономию в процентах сами (повторяем математику)
if result.tokens_before > 0:
    percent = 100 * result.tokens_saved / result.tokens_before
    print(f"Экономия:        {percent:.1f}%")
print("=" * 50)
