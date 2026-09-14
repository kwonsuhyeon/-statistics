# -*- coding: utf-8 -*-
"""
파이썬을 활용한 기초통계 분석 — 1차시
데이터 불러오기부터 describe()까지 (코드 5개)

실행 방법
  1) 이 파일과 hccp_worker_2023_selected.csv 를 같은 폴더에 둔다
  2) 터미널에서:  python stats_lesson1.py
     (VS Code에서는 오른쪽 위 ▷ 실행 버튼)

노트북(.ipynb)에서는 각 단계를 셀 하나씩 붙여 넣고 Shift+Enter 로 실행하면 됩니다.
노트북은 마지막 줄 값을 자동으로 보여 주지만, .py 파일은 print()로 감싸야 화면에 나옵니다.
"""

import pandas as pd

# 표가 한 화면에 잘 보이도록 출력 폭을 넓힌다 (통계와 무관한 표시 설정)
pd.set_option("display.width", 160)
pd.set_option("display.max_columns", 12)


# ── 코드 1. 불러오기 ─────────────────────────────────────────────
# CSV 파일을 읽어 df(데이터프레임)에 담는다. 결과가 없는 것이 정상.
df = pd.read_csv("hccp_worker_2023_selected.csv")
# 다른 폴더에 있다면 전체 경로를 쓴다. 앞의 r 을 잊지 말 것.
# df = pd.read_csv(r"C:\Users\사용자이름\Downloads\hccp_worker_2023_selected.csv")


# ── 코드 2. 생김새 — head() ──────────────────────────────────────
print("=" * 70)
print("코드 2. df.head()  — 처음 5행")
print("=" * 70)
print(df.head())          # 괄호 안에 10을 넣으면 10행


# ── 코드 3. 크기 — shape ─────────────────────────────────────────
print("\n" + "=" * 70)
print("코드 3. df.shape  — (행 수, 열 수)   ※ shape 뒤에는 괄호가 없다")
print("=" * 70)
print(df.shape)           # (10759, 47)

print("\n변수(열) 이름 목록 — df.columns")
print(list(df.columns))   # 변수 이름은 여기서 복사해서 쓰는 습관


# ── 코드 4. 구조 — info() ────────────────────────────────────────
print("\n" + "=" * 70)
print("코드 4. df.info()  — 변수별 결측 아닌 개수(Non-Null Count)와 자료형(Dtype)")
print("=" * 70)
df.info()                 # info()는 스스로 출력하므로 print() 불필요


# ── 코드 5. 기초통계량 — describe()  ← 오늘의 목표 ────────────────
print("\n" + "=" * 70)
print("코드 5. df.describe()  — 숫자형 변수 전체의 기초통계량 (8행 × 47열)")
print("=" * 70)
print(df.describe())

# 5-1. 보고 싶은 변수만 골라서 — 대괄호 두 겹 [[ ]]
print("\n" + "-" * 70)
print("5-1. 변수 세 개만 — 연소득 · 주당 정규 근로시간 · 전반적 직무만족 (.round(2))")
print("-" * 70)
print(
    df[["annual_income_10k_krw", "regular_work_hours", "overall_job_satisfaction"]]
    .describe()
    .round(2)
)

# 5-2. 변수 하나만 — 대괄호 한 겹 [ ]
print("\n" + "-" * 70)
print("5-2. 변수 하나만 — 연소득(만원)")
print("-" * 70)
print(df["annual_income_10k_krw"].describe().round(2))

# 5-3. 함정 — 명명척도 변수에 describe()를 쓰면?
print("\n" + "-" * 70)
print("5-3. 명명척도 변수(gender)에 describe()를 쓰면? → 평균 1.30은 의미 없음")
print("-" * 70)
print(df["gender"].describe())
# 1과 2는 크기가 아니라 이름표. 이런 변수는 다음 차시의 value_counts()로 '몇 명씩인지' 센다.
