

1. через ngrok робимо тунелювання в https:// (https://429f1e33.ngrok.io/)
   ngrok http 5000 (5000 - порт для фласка)

2. робимо Webhooks (setWebhook):
   https://api.telegram.org/bot<token>/setWebhook?url=https://429f1e33.ngrok.io
   {"ok":true,"result":true,"description":"Webhook was set"}
   
   Щоб телеграм бот слав пост запити

3. додаємо в декоратор @app.route('/', message=['POST', 'GET'])



