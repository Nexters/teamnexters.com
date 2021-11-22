# teamnexters.com

## 작업 내용

[웹 개편 프로젝트 리포트](https://classy-bottle-ba6.notion.site/8982faf68ce146e9b5613799f8c5f4f0) 참고

### 실행 방법

#### 프로젝트 실행

1. `.env` 파일 수정

   ```
   PROJECT_ID=
   PRIVATE_KEY_ID=
   PRIVATE_KEY=
   CLIENT_EMAIL=
   CLIENT_ID=
   ```

2. docker-compose 빌드 및 실행
   ```bash
   # .env 확인 필수
   docker-compose up --build -d
   ```

#### google sheet 동기화

```bash
# .env 확인 필수
docker-compose up content-updater
```

### 기술스택

- vue(+nuxt)
- Google Drive API (콘텐츠 관리)

### 주의사항

content generator을 이용하여 google sheet 동기화 시 읽기 요청 분당 300회 제한으로 429 Too many request가 발생할 수 있으니 배포 시 주의

- [Google Drive API 할당량](https://support.google.com/a/answer/6301355)
- [Usages limits](https://developers.google.com/docs/api/limits)
  - 읽기 요청 분당 300회 제한
  - 프로젝트당 분당 3000회 제한

### 팀 구성

- 14기 진성곤(디자인/PM)
- 6기 김대경(디자인)
- 15기 김민철(개발)
- 14기 김헌진(개발)
