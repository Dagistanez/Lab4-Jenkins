# 1. Беремо офіційний LTS-образ Jenkins
FROM jenkins/jenkins:lts

# 2. Перемикаємося на root, щоб встановити системні пакети Linux
USER root

# 3. Встановлюємо Python 3, pip та інструменти для venv
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv python3-full && \
    rm -rf /var/lib/apt/lists/*

# 4. Повертаємося до безпечного користувача jenkins
USER jenkins