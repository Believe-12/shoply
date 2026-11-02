Учебный проект для модуля 2: «Интернет-магазин»

Состав:
- app.py — простое веб-приложение Flask;
- requirements.txt — зависимости Python;
- Dockerfile — инструкция сборки образа;
- docker-compose.yml — веб-приложение и MySQL, общая сеть и том;
- k8s/deployment.yaml — Deployment Kubernetes;
- k8s/service.yaml — Service типа NodePort.

Важно:
1. Перед публикацией образа замените DOCKERHUB_USERNAME на свой логин Docker Hub.
2. Для Kubernetes замените DOCKERHUB_USERNAME в deployment.yaml на свой логин.
3. В этом учебном примере Kubernetes разворачивает веб-приложение; база данных
   в Kubernetes-манифесты не включена, поскольку задание №6 требует Deployment
   приложения и Service для доступа к нему.
4. Пароли в примере учебные. Для реального проекта их следует хранить в Secrets
   или переменных окружения, а не публиковать в открытом виде.
