FROM python:3.9-slim

WORKDIR /app

# 현재 폴더의 모든 파일(tip_calc_main.py, requirements.txt 등)을 복사
COPY . .

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 포트 개방
EXPOSE 8080

# 실행 명령 (파일명에 오타가 없는지 꼭 확인!)
CMD ["uvicorn", "tip_calc_main:app", "--host", "0.0.0.0", "--port", "8080"]
