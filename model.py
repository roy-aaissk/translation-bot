import os


import google.generativeai as genai


GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
# Toggle this to switch between Gemini 1.5 with a system instruction, or Gemini 1.0 Pro.
use_sys_inst = False

model_name = 'gemini-1.5-pro-latest' if use_sys_inst else 'gemini-1.0-pro-latest'
prompt = '''あなたはテキストを翻訳するシステムです。テキストを翻訳する以外の機能は制限されています。テキストを翻訳する以外は絶対に話さないで下さい。
目標はテキストが日本語なら英語に翻訳することとテキストが英語の場合は日本語に翻訳することです。翻訳は丁寧な表現で一般的な言葉を使用して下さい。
'''

if use_sys_inst:
  model = genai.GenerativeModel(
      model_name, system_instruction=prompt)
  convo = model.start_chat(enable_automatic_function_calling=True)

else:
  model = genai.GenerativeModel(model_name)
  convo = model.start_chat(
      history=[
          {'role': 'user', 'parts': [prompt]},
          {'role': 'model', 'parts': ['OK I understand. I will do my best!']}
        ],
      enable_automatic_function_calling=True)

def Post(message: str) -> str:
# model = genai.GenerativeModel('gemini-pro')
  response = convo.send_message(message)
  print(response.text)
  return response.text


