# Speaking Pingu 🐧🤖

## Overview
A speaking penguin **AI chatbot** built with Flask and Vue.js, powered by **Deepseek AI API**. Basicly it's a self-hosted web interface for [Deepseek AI](https://www.deepseek.com/).

## Installation

### Prerequisites
- docker-compose

**Clone the repository**
```bash
git clone https://github.com/lytexdev/speaking-pingu.git
cd speaking-pingu
```

**Copy and rename `.env.example` to `.env`**
```bash
cp .env.example .env
```

**Insert a Flask secret key in `.env`**
```bash
FLASK_SECRET_KEY=your-secret-key
```

**Build the frontend**
```bash
./speaking-pingu build
```

**Build and run the Docker image**
```bash
# with docker-compose-v2
docker compose up -d

# with docker-compose-v1
docker-compose up -d
```
By default it runs on port 5000

## License
This project is licensed under the GNU General Public License v3 - see the [LICENSE](LICENSE) file for details.
