-- День 01 — SQL основы: SELECT, ROUND, FLOOR, CEILING, DISTINCT, LIMIT

-- 1. Название фильма + рейтинг, округлённый до 1 знака
SELECT title,
    ROUND(rating, 1) AS rounded_rating
FROM movies;

-- 2. Название фильма + жанр заглавными буквами
SELECT title,
    UPPER(genre) AS upper_genre
FROM movies;

-- 3. Название фильма + рейтинг, округлённый вверх до целого
SELECT title,
    CEILING(rating) AS ceiling_rating
FROM movies;

-- 4. Уникальные годы выпуска
SELECT DISTINCT year
FROM movies;

-- 5. Первые 5 фильмов
SELECT title
FROM movies
LIMIT 5;
