
import os
import time
from flask import Flask
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)


def get_db_status():
    host = os.getenv("DB_HOST", "db")
    user = os.getenv("DB_USER", "shopuser")
    password = os.getenv("DB_PASSWORD", "shoppass")
    database = os.getenv("DB_NAME", "shopdb")

    for attempt in range(10):
        try:
            connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                connection_timeout=3
            )
            if connection.is_connected():
                connection.close()
                return "База данных подключена"
        except Error:
            time.sleep(2)

    return "База данных временно недоступна"


@app.route("/")
def index():
    db_status = get_db_status()

    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Shoply — интернет-магазин</title>

        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: Arial, sans-serif;
                background: #f5f6fa;
                color: #20243a;
            }

            header {
                background: white;
                padding: 20px 8%;
                display: flex;
                align-items: center;
                justify-content: space-between;
                box-shadow: 0 2px 12px rgba(0,0,0,0.05);
            }

            .logo {
                font-size: 28px;
                font-weight: bold;
                color: #6254d9;
            }

            nav {
                display: flex;
                gap: 30px;
            }

            nav a {
                text-decoration: none;
                color: #555;
                font-size: 15px;
            }

            nav a:hover {
                color: #6254d9;
            }

            .cart {
                background: #6254d9;
                color: white;
                padding: 12px 20px;
                border-radius: 12px;
                font-weight: bold;
            }

            .hero {
                margin: 35px 8%;
                padding: 55px;
                border-radius: 24px;
                background: linear-gradient(120deg, #6254d9, #9288f5);
                color: white;
                display: flex;
                align-items: center;
                justify-content: space-between;
                min-height: 260px;
            }

            .hero h1 {
                font-size: 40px;
                margin-bottom: 15px;
            }

            .hero p {
                font-size: 17px;
                opacity: 0.9;
                margin-bottom: 25px;
            }

            .hero-button {
                display: inline-block;
                background: white;
                color: #6254d9;
                padding: 14px 24px;
                border-radius: 10px;
                text-decoration: none;
                font-weight: bold;
            }

            .hero-icon {
                font-size: 110px;
                margin-right: 30px;
            }

            .container {
                margin: 45px 8%;
            }

            .section-title {
                font-size: 27px;
                margin-bottom: 25px;
            }

            .categories {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 18px;
                margin-bottom: 50px;
            }

            .category {
                background: white;
                padding: 25px;
                border-radius: 16px;
                text-align: center;
                font-weight: bold;
                box-shadow: 0 4px 15px rgba(0,0,0,0.03);
            }

            .category span {
                display: block;
                font-size: 35px;
                margin-bottom: 12px;
            }

            .products {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 22px;
            }

            .product {
                background: white;
                border-radius: 18px;
                padding: 18px;
                box-shadow: 0 4px 18px rgba(0,0,0,0.04);
                transition: transform 0.2s;
            }

            .product:hover {
                transform: translateY(-5px);
            }

            .product-image {
                height: 160px;
                background: #f1f0ff;
                border-radius: 14px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 75px;
                margin-bottom: 18px;
            }

            .product h3 {
                font-size: 17px;
                margin-bottom: 9px;
            }

            .description {
                color: #888;
                font-size: 13px;
                margin-bottom: 15px;
            }

            .price {
                font-size: 21px;
                font-weight: bold;
                margin-bottom: 15px;
            }

            .old-price {
                color: #aaa;
                text-decoration: line-through;
                font-size: 14px;
                margin-left: 7px;
                font-weight: normal;
            }

            .buy-button {
                width: 100%;
                border: none;
                background: #6254d9;
                color: white;
                padding: 13px;
                border-radius: 10px;
                font-size: 14px;
                font-weight: bold;
                cursor: pointer;
            }

            .buy-button:hover {
                background: #5042c4;
            }

            .status {
                margin: 40px 8%;
                padding: 18px 22px;
                background: white;
                border-radius: 12px;
                color: #555;
                font-size: 14px;
            }

            footer {
                margin-top: 60px;
                padding: 30px;
                text-align: center;
                background: #20243a;
                color: #ccc;
                font-size: 14px;
            }

            @media (max-width: 850px) {
                .products {
                    grid-template-columns: repeat(2, 1fr);
                }

                .categories {
                    grid-template-columns: repeat(2, 1fr);
                }

                nav {
                    display: none;
                }

                .hero-icon {
                    display: none;
                }
            }

            @media (max-width: 500px) {
                .hero {
                    padding: 30px;
                }

                .hero h1 {
                    font-size: 29px;
                }

                .products {
                    grid-template-columns: 1fr;
                }
            }
        </style>
    </head>

    <body>

        <header>
            <div class="logo">shoply.</div>

            <nav>
                <a href="#">Главная</a>
                <a href="#categories">Категории</a>
                <a href="#products">Товары</a>
                <a href="#contacts">Контакты</a>
            </nav>

            <div class="cart">
                🛒 Корзина: <span id="cart-count">0</span>
            </div>
        </header>

        <section class="hero">
            <div>
                <h1>Покупки с удовольствием</h1>
                <p>Стильные товары, выгодные цены и удобная доставка.</p>
                <a href="#products" class="hero-button">Перейти к покупкам →</a>
            </div>
            <div class="hero-icon">🛍️</div>
        </section>

        <main class="container">

            <h2 class="section-title" id="categories">Категории товаров</h2>

            <div class="categories">
                <div class="category"><span>💻</span>Электроника</div>
                <div class="category"><span>👕</span>Одежда</div>
                <div class="category"><span>🏠</span>Для дома</div>
                <div class="category"><span>🎧</span>Аксессуары</div>
            </div>

            <h2 class="section-title" id="products">Популярные товары</h2>

            <div class="products">

                <div class="product">
                    <div class="product-image">🎧</div>
                    <h3>Беспроводные наушники</h3>
                    <p class="description">Чистый звук и удобная посадка</p>
                    <div class="price">12 990 ₸
                        <span class="old-price">16 990 ₸</span>
                    </div>
                    <button class="buy-button" onclick="addToCart()">
                        🛒 В корзину
                    </button>
                </div>

                <div class="product">
                    <div class="product-image">⌚</div>
                    <h3>Умные часы</h3>
                    <p class="description">Современный дизайн и функции</p>
                    <div class="price">24 990 ₸</div>
                    <button class="buy-button" onclick="addToCart()">
                        🛒 В корзину
                    </button>
                </div>

                <div class="product">
                    <div class="product-image">🎒</div>
                    <h3>Городской рюкзак</h3>
                    <p class="description">Практичный аксессуар на каждый день</p>
                    <div class="price">8 490 ₸
                        <span class="old-price">10 990 ₸</span>
                    </div>
                    <button class="buy-button" onclick="addToCart()">
                        🛒 В корзину
                    </button>
                </div>

                <div class="product">
                    <div class="product-image">📷</div>
                    <h3>Цифровая камера</h3>
                    <p class="description">Яркие фотографии и видео</p>
                    <div class="price">39 990 ₸</div>
                    <button class="buy-button" onclick="addToCart()">
                        🛒 В корзину
                    </button>
                </div>

            </div>
        </main>

        <div class="status">
            <strong>Статус системы:</strong>
            <span id="db-status">""" + db_status + """</span>
            <br><br>
            <strong>Состояние веб-приложения:</strong> Работает
        </div>

        <footer id="contacts">
            <p>© 2026 Shoply — учебный интернет-магазин</p>
            <p style="margin-top: 8px;">Покупать удобно. Покупать выгодно.</p>
        </footer>

        <script>
            let cartCount = 0;

            function addToCart() {
                cartCount++;
                document.getElementById("cart-count").textContent = cartCount;
            }
        </script>

    </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
