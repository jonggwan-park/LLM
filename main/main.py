import openai
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

# API Key 설정

openai.api_key = os.getenv("OPENAI_API_KEY")

    # 프롬프트 명령
def chat_with_gpt():
    # 대화 내용 저장할 파일
    log_file = "conversation_log.txt"

    # 대화 기록 초기화
    messages = []
    
    prompt = "You are a very scary computer teacher."

    # 초기 대화 설정
    messages = [{"role":"system","content":prompt}]

    # exit가 입력되기 전까지 계속 대화

    while True:
        user_input = input("User: ")
        
        if user_input.lower() == "exit":
            print("대화 종료")
            break
        messages.append({"role":"system","content":user_input})

        try:
            response=openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
            )
            assistant_response = response['choices'][0]['message']['content']
            print(f"GPT: {assistant_response}")

            messages.append({"role":"assistant","content":assistant_response})
            # 대화 내용을 파일에 저장
            with open(log_file, "a", encoding="utf-8") as file:
                file.write(f"You: {user_input}\n")
                file.write(f"GPT: {assistant_response}\n\n")
        except Exception as e:
            print(f"오류발생:{e}")
if __name__ == "__main__":
    chat_with_gpt()