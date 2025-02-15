# File Server

파일을 업로드, 다운로드할 수 있는 파일서버입니다.

## 기능

- 서버에 파일을 업로드 할 수 있습니다.
- 서버에서 파일을 다운로드 받을 수 있습니다.
- 서버에서 파일을 삭제할 수 있습니다.
- 서버에 업로드된 파일을 유저 친화적인 화면으로 제공하고, 파일 사이즈를 사람이 읽을 수 있는 형태로 출력합니다.
- 저장 공간 사용량을 추적하고, 사용한계에 도달하면 이메일 경고를 보냅니다.

## 설치 방법

**1. Clone repository**

```bash
git clone https://github.com/AlpacaMale/file-server
```

**2. Write email setup**

> You can create a google app password [here][1]

```bash
FLASK_ENV=development

MAIL_SERVER="smtp.gmail.com"
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME="example@email.com"
MAIL_PASSWORD="your password here"
MAIL_DEFAULT_SENDER='example@email.com'
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Run flask app**

```bash
flask run
```

## 패키지 구조

```
├── 📁 static / Directory for static files
├── 📁 uploads / Directory for storage files
├── 📁 templates / Directory for HTML templates
│   └── index.html / Web entry point
├── app.py / Main entry point for Flask application
├── config.py / Configurations settings
├── requirements.txt / List of package dependencies
└── README.md / Project documentation
```

[1]: https://myaccount.google.com/apppasswords
