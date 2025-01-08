import pandas as pd
import numpy as np

# CSV 파일 읽어오기
data = pd.read_csv('audi_faq_raw.csv')

# 데이터프레임 생성
df = pd.DataFrame(data, columns=['질문', '답변'])

# 답변 컬럼 값 위로 37 칸 이동 (shift 함수 사용)
df['답변'] = df['답변'].shift(-37)

# 답변 컬럼의 \n 제거
df['답변'] = df['답변'].str.replace('\n', '')

# 중복 제거 후 인덱스 재설정
df = df.drop_duplicates().reset_index(drop=True)

# 4번 간격으로 행 추출
df = df.iloc[::4]

# 인덱스 재설정
df = df.reset_index(drop=True)

# 결과 출력
print(df)

# 새로운 CSV 파일로 저장 (인덱스 없이 저장)
df.to_csv('AUDI_FAQ.csv', index=False)

print("데이터가 AUDI_FAQ.csv 파일로 저장되었습니다.")
