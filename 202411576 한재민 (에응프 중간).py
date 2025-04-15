import json
import os
import random
from datetime import datetime

# 데이터 저장 폴더 생성
if not os.path.exists("user_data"):
    os.makedirs("user_data")

# ========================== 데이터베이스 ==========================
DIET_PLANS = {
        "근육량 증가": [
        {
            "아침": {"메뉴": "오트밀 + 계란 3개", "칼로리": 450, "단백질": 35, "탄수화물": 40, "지방": 12},
            "점심": {"메뉴": "소고기 스테이크 + 고구마", "칼로리": 650, "단백질": 55, "탄수화물": 50, "지방": 20},
            "저녁": {"메뉴": "연어 구이 + 브로콜리", "칼로리": 550, "단백질": 45, "탄수화물": 15, "지방": 25}
        },
        {
            "아침": {"메뉴": "닭가슴살 + 바나나", "칼로리": 400, "단백질": 40, "탄수화물": 35, "지방": 8},
            "점심": {"메뉴": "돼지고기 불고기 + 현미밥", "칼로리": 700, "단백질": 50, "탄수화물": 60, "지방": 22},
            "저녁": {"메뉴": "계란찜 + 고등어 구이", "칼로리": 600, "단백질": 50, "탄수화물": 10, "지방": 30}
        },
        {
            "아침": {"메뉴": "단백질 쉐이크 + 토스트", "칼로리": 420, "단백질": 35, "탄수화물": 40, "지방": 10},
            "점심": {"메뉴": "치킨 가슴살 버거 + 감자", "칼로리": 680, "단백질": 50, "탄수화물": 55, "지방": 18},
            "저녁": {"메뉴": "돼지 등심 구이 + 나물", "칼로리": 560, "단백질": 40, "탄수화물": 20, "지방": 24}
        },
        {
            "아침": {"메뉴": "삶은 계란 4개 + 바나나", "칼로리": 410, "단백질": 30, "탄수화물": 25, "지방": 15},
            "점심": {"메뉴": "닭다리살 구이 + 감자", "칼로리": 650, "단백질": 45, "탄수화물": 40, "지방": 20},
            "저녁": {"메뉴": "연두부 + 나물 반찬", "칼로리": 500, "단백질": 35, "탄수화물": 15, "지방": 22}
        },
        {
            "아침": {"메뉴": "그릭요거트 + 그래놀라", "칼로리": 350, "단백질": 25, "탄수화물": 30, "지방": 10},
            "점심": {"메뉴": "스테이크 덮밥", "칼로리": 720, "단백질": 50, "탄수화물": 60, "지방": 25},
            "저녁": {"메뉴": "계란말이 + 두부", "칼로리": 550, "단백질": 40, "탄수화물": 20, "지방": 18}
        },
        {
            "아침": {"메뉴": "단백질바 + 우유", "칼로리": 370, "단백질": 30, "탄수화물": 25, "지방": 12},
            "점심": {"메뉴": "오리훈제 + 고구마", "칼로리": 680, "단백질": 55, "탄수화물": 50, "지방": 20},
            "저녁": {"메뉴": "연어샐러드", "칼로리": 530, "단백질": 40, "탄수화물": 15, "지방": 28}
        },
        {
            "아침": {"메뉴": "삶은 계란 3개 + 오트밀", "칼로리": 460, "단백질": 35, "탄수화물": 40, "지방": 12},
            "점심": {"메뉴": "닭가슴살 + 잡곡밥", "칼로리": 600, "단백질": 45, "탄수화물": 45, "지방": 15},
            "저녁": {"메뉴": "두부조림 + 나물", "칼로리": 480, "단백질": 35, "탄수화물": 20, "지방": 18}
        }
    ],
   "체지방 감소": [
       {
            "아침": {"메뉴": "그릭 요거트 + 아몬드", "칼로리": 300, "단백질": 20, "탄수화물": 15, "지방": 10},
            "점심": {"메뉴": "닭가슴살 샐러드", "칼로리": 400, "단백질": 35, "탄수화물": 20, "지방": 8},
            "저녁": {"메뉴": "두부 스팀 + 시금치", "칼로리": 350, "단백질": 25, "탄수화물": 10, "지방": 12}
        },
        {
            "아침": {"메뉴": "삶은 계란 2개 + 바나나", "칼로리": 250, "단백질": 15, "탄수화물": 20, "지방": 9},
            "점심": {"메뉴": "현미밥 + 생선구이 + 나물", "칼로리": 450, "단백질": 30, "탄수화물": 40, "지방": 10},
            "저녁": {"메뉴": "닭가슴살 + 방울토마토", "칼로리": 300, "단백질": 30, "탄수화물": 5, "지방": 7}
        },
        {
            "아침": {"메뉴": "귀리죽 + 견과류", "칼로리": 320, "단백질": 15, "탄수화물": 30, "지방": 10},
            "점심": {"메뉴": "닭가슴살 브리또", "칼로리": 430, "단백질": 35, "탄수화물": 30, "지방": 12},
            "저녁": {"메뉴": "야채볶음 + 삶은계란", "칼로리": 330, "단백질": 20, "탄수화물": 15, "지방": 10}
        },
        {
            "아침": {"메뉴": "단백질쉐이크 + 사과", "칼로리": 280, "단백질": 25, "탄수화물": 20, "지방": 5},
            "점심": {"메뉴": "두부 샐러드", "칼로리": 370, "단백질": 30, "탄수화물": 10, "지방": 15},
            "저녁": {"메뉴": "현미밥 + 계란찜 + 나물", "칼로리": 400, "단백질": 25, "탄수화물": 35, "지방": 10}
        },
        {
            "아침": {"메뉴": "삶은 달걀 + 오이", "칼로리": 220, "단백질": 18, "탄수화물": 5, "지방": 10},
            "점심": {"메뉴": "현미밥 + 닭가슴살구이 + 나물", "칼로리": 440, "단백질": 35, "탄수화물": 35, "지방": 10},
            "저녁": {"메뉴": "두부김치 (기름없이)", "칼로리": 300, "단백질": 25, "탄수화물": 10, "지방": 8}
        },
        {
            "아침": {"메뉴": "고구마 + 삶은 계란", "칼로리": 280, "단백질": 18, "탄수화물": 25, "지방": 6},
            "점심": {"메뉴": "닭가슴살 곤약 볶음밥", "칼로리": 400, "단백질": 35, "탄수화물": 25, "지방": 10},
            "저녁": {"메뉴": "샐러드 + 닭가슴살", "칼로리": 300, "단백질": 30, "탄수화물": 5, "지방": 6}
        },
        {
            "아침": {"메뉴": "오트밀 + 블루베리", "칼로리": 300, "단백질": 15, "탄수화물": 35, "지방": 7},
            "점심": {"메뉴": "삶은 닭가슴살 + 고구마", "칼로리": 420, "단백질": 35, "탄수화물": 30, "지방": 10},
            "저녁": {"메뉴": "두부구이 + 나물", "칼로리": 310, "단백질": 25, "탄수화물": 10, "지방": 9}
        }
    ],
    "기능성운동": [
        {
            "아침": {"메뉴": "그릭 요거트 + 아몬드", "칼로리": 300, "단백질": 20, "탄수화물": 15, "지방": 10},
            "점심": {"메뉴": "닭가슴살 샐러드", "칼로리": 400, "단백질": 35, "탄수화물": 20, "지방": 8},
            "저녁": {"메뉴": "두부 스팀 + 시금치", "칼로리": 350, "단백질": 25, "탄수화물": 10, "지방": 12}
        },
        {
            "아침": {"메뉴": "고구마 + 삶은 계란", "칼로리": 280, "단백질": 18, "탄수화물": 25, "지방": 6},
            "점심": {"메뉴": "닭가슴살 곤약 볶음밥", "칼로리": 400, "단백질": 35, "탄수화물": 25, "지방": 10},
            "저녁": {"메뉴": "샐러드 + 닭가슴살", "칼로리": 300, "단백질": 30, "탄수화물": 5, "지방": 6}
        },
        {
            "아침": {"메뉴": "귀리죽 + 견과류", "칼로리": 320, "단백질": 15, "탄수화물": 30, "지방": 10},
            "점심": {"메뉴": "닭가슴살 브리또", "칼로리": 430, "단백질": 35, "탄수화물": 30, "지방": 12},
            "저녁": {"메뉴": "야채볶음 + 삶은계란", "칼로리": 330, "단백질": 20, "탄수화물": 15, "지방": 10}
        },
        {
            "아침": {"메뉴": "단백질쉐이크 + 사과", "칼로리": 280, "단백질": 25, "탄수화물": 20, "지방": 5},
            "점심": {"메뉴": "두부 샐러드", "칼로리": 370, "단백질": 30, "탄수화물": 10, "지방": 15},
            "저녁": {"메뉴": "현미밥 + 계란찜 + 나물", "칼로리": 400, "단백질": 25, "탄수화물": 35, "지방": 10}
        },
        {
            "아침": {"메뉴": "삶은 달걀 + 오이", "칼로리": 220, "단백질": 18, "탄수화물": 5, "지방": 10},
            "점심": {"메뉴": "현미밥 + 닭가슴살구이 + 나물", "칼로리": 440, "단백질": 35, "탄수화물": 35, "지방": 10},
            "저녁": {"메뉴": "두부김치 (기름없이)", "칼로리": 300, "단백질": 25, "탄수화물": 10, "지방": 8}
        },
        {
            "아침": {"메뉴": "단백질 쉐이크 + 토스트", "칼로리": 420, "단백질": 35, "탄수화물": 40, "지방": 10},
            "점심": {"메뉴": "치킨 가슴살 버거 + 감자", "칼로리": 680, "단백질": 50, "탄수화물": 55, "지방": 18},
            "저녁": {"메뉴": "돼지 등심 구이 + 나물", "칼로리": 560, "단백질": 40, "탄수화물": 20, "지방": 24}
        },
        {
            "아침": {"메뉴": "오트밀 + 블루베리", "칼로리": 300, "단백질": 15, "탄수화물": 35, "지방": 7},
            "점심": {"메뉴": "삶은 닭가슴살 + 고구마", "칼로리": 420, "단백질": 35, "탄수화물": 30, "지방": 10},
            "저녁": {"메뉴": "두부구이 + 나물", "칼로리": 310, "단백질": 25, "탄수화물": 10, "지방": 9}
        }
    ]
}


MUSCLE_WORKOUTS = {
    "등운동": [
        {"이름": "랫 풀다운", "세트": "4x12", "가이드": "가슴을 열고 어깨 내리기"},
        {"이름": "바벨 로우", "세트": "3x10", "가이드": "등 중앙에 집중"},
        {"이름": "풀업", "세트": "3x8", "가이드": "완전한 수축 유지"},
        {"이름": "데드리프트", "세트": "4x6", "가이드": "허리 보호 필수"},
        {"이름": "케이블 로우", "세트": "3x12", "가이드": "등 근육 수축 유지"}
    ],
    "가슴운동": [
        {"이름": "벤치 프레스", "세트": "4x8", "가이드": "발바닥으로 지면 밀기"},
        {"이름": "인클라인 덤벨", "세트": "3x10", "가이드": "45도 각도 유지"},
        {"이름": "딥스", "세트": "3x12", "가이드": "상체 약간 기울이기"},
        {"이름": "체스트 플라이", "세트": "3x15", "가이드": "가슴 펴고 운동"},
        {"이름": "푸시업", "세트": "4x20", "가이드": "코어 긴장 상태 유지"}
    ],
    "하체운동": [
        {"이름": "스쿼트", "세트": "4x12", "가이드": "무릎이 발끝 넘지 않게"},
        {"이름": "레그 프레스", "세트": "3x10", "가이드": "허리 붙이고 무릎 90도"},
        {"이름": "런지", "세트": "3x8", "가이드": "앞무릎 90도 유지"},
        {"이름": "레그 컬", "세트": "3x15", "가이드": "햄스트링 수축에 집중"},
        {"이름": "카프 레이즈", "세트": "4x20", "가이드": "발목 높이 최대한 올리기"}
    ],
    "어깨운동": [
        {"이름": "오버헤드 프레스", "세트": "4x10", "가이드": "허리 보호를 위해 코어 강화"},
        {"이름": "레터럴 레이즈", "세트": "3x12", "가이드": "팔보다 어깨 높이까지만"},
        {"이름": "프론트 레이즈", "세트": "3x12", "가이드": "팔을 정면으로 천천히"},
        {"이름": "리어 델트 플라이", "세트": "3x15", "가이드": "등 뒤로 모으는 느낌"},
        {"이름": "업라이트 로우", "세트": "3x10", "가이드": "바벨을 턱까지 끌어올리기"}
    ],
    "팔운동": [
        {"이름": "바벨 컬", "세트": "3x12", "가이드": "팔꿈치 고정하고 이두근만"},
        {"이름": "트라이셉스 딥", "세트": "3x10", "가이드": "몸을 수직으로 내리기"},
        {"이름": "해머 컬", "세트": "3x10", "가이드": "중립 그립 유지"},
        {"이름": "오버헤드 트라이셉스", "세트": "3x12", "가이드": "팔꿈치 움직임 최소화"},
        {"이름": "리버스 컬", "세트": "3x15", "가이드": "전완근 강화에 효과적"}
    ],
    "복근운동": [
        {"이름": "크런치", "세트": "3x20", "가이드": "목 보호를 위해 턱 당기기"},
        {"이름": "레그 레이즈", "세트": "3x15", "가이드": "허리 떼지 않게 주의"},
        {"이름": "플랭크", "세트": "3x60초", "가이드": "엉덩이 높이 일정하게"},
        {"이름": "러시안 트위스트", "세트": "3x20", "가이드": "상체 회전만 수행"},
        {"이름": "행잉 레그 레이즈", "세트": "3x12", "가이드": "관성 없이 천천히"}
    ]
}

CARDIO_WORKOUTS = [
    {"이름": "등산", "시간": "60분", "강도": "중", "칼로리소모": "400-600kcal"},
    {"이름": "수영", "시간": "45분", "강도": "중상", "칼로리소모": "350-500kcal"},
    {"이름": "달리기", "시간": "30분", "강도": "고", "칼로리소모": "300-400kcal"},
    {"이름": "계단 오르기", "시간": "20분", "강도": "중고", "칼로리소모": "250-350kcal"},
    {"이름": "싸이클", "시간": "40분", "강도": "중", "칼로리소모": "300-450kcal"}
]

FUNCTIONAL_WORKOUTS = [
    {"이름": "슈퍼맨 자세", "시간": "3x30초", "효과": "척추 기립근 강화", "가이드": "팔다리 동시 들어올리기"},
    {"이름": "버드 독", "시간": "3x20초(각쪽)", "효과": "코어 안정화", "가이드": "반대쪽 팔/다리 사용"},
    {"이름": "플랭크", "시간": "3x60초", "효과": "전신 안정성", "가이드": "허리 곧게 유지"},
    {"이름": "사이드 플랭크", "시간": "3x30초(각쪽)", "효과": "측면 코어", "가이드": "골반 들어올리기"},
    {"이름": "글루트 브릿지", "시간": "3x15회", "효과": "둔근 강화", "가이드": "엉덩이 최대 수축"},
    {"이름": "박스 점프", "시간": "3x10회", "효과": "파워 발달", "가이드": "착지 시 무릎 유연하게"},
    {"이름": "TRX 로우", "시간": "3x12회", "효과": "상체 협응력", "가이드": "견갑골 조이기"}
]

# ========================== 시스템 클래스 ==========================
class FitnessProgram:
    def __init__(self):
        self.current_user = None
        self.body_parts = ["등운동", "가슴운동", "하체운동", "어깨운동", "팔운동", "복근운동"]

    def create_profile(self):
        print("\n" + "="*50)
        print(" " * 15 + "🆕 프로필 생성")
        print("="*50)
        
        profile = {
            "name": input("이름: "),
            "age": int(input("나이: ")),
            "height": float(input("키(cm): ")),
            "weight": float(input("몸무게(kg): ")),
            "body_fat": float(input("체지방률(%): ")),
            "muscle_mass": float(input("골격근량(kg): ")),
            "goal": self.select_goal(),
            "workout_place": self.select_workout_place(),
            "target_body_parts": []
        }
        
        if profile["goal"] == "근육량 증가":
            profile["target_body_parts"] = self.select_body_parts()
        
        self.save_profile(profile)
        self.current_user = profile
        print(f"\n✅ {profile['name']}님 프로필 생성 완료!")

    def select_goal(self):
        while True:
            print("\n운동 목표 선택:")
            print("1. 근육량 증가")
            print("2. 체지방 감소")
            print("3. 기능성운동 (균형/협응력)")
            choice = input(">> 선택: ").strip()
            
            if choice == "1": return "근육량 증가"
            elif choice == "2": return "체지방 감소"
            elif choice == "3": return "기능성운동"
            print("⚠ 올바른 번호를 입력하세요!")

    def select_workout_place(self):
        while True:
            print("\n운동 장소 선택:")
            print("1. 헬스장")
            print("2. 집")
            print("3. 야외")
            choice = input(">> 선택: ").strip()
            
            if choice == "1": return "헬스장"
            elif choice == "2": return "집"
            elif choice == "3": return "야외"
            print("⚠ 올바른 번호를 입력하세요!")

    def select_body_parts(self):
        selected = []
        print("\n운동 부위 선택 (복수 선택 가능):")
        for i, part in enumerate(self.body_parts, 1):
            print(f"{i}. {part}")
        
        while True:
            choices = input("선택할 번호(쉼표로 구분, 예: 1,3,5): ").split(',')
            try:
                selected = [self.body_parts[int(c)-1] for c in choices]
                if not selected:
                    raise ValueError
                return selected
            except:
                print("⚠ 올바른 번호 조합을 입력하세요!")

    def save_profile(self, profile):
        filename = f"user_data/{profile['name']}_profile.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(profile, f, indent=4, ensure_ascii=False)

    def load_profile(self):
        profiles = []
        for file in os.listdir("user_data"):
            if file.endswith(".json"):
                with open(f"user_data/{file}", 'r', encoding='utf-8') as f:
                    profiles.append(json.load(f))
        
        if not profiles:
            print("\n⚠ 저장된 프로필이 없습니다!")
            return False
            
        print("\n" + "="*50)
        print(" " * 15 + "📂 프로필 목록")
        print("="*50)
        for i, p in enumerate(profiles, 1):
            print(f"{i}. {p['name']} | 키: {p['height']}cm | 목표: {p['goal']}")
        
        while True:
            try:
                choice = int(input("\n프로필 번호 선택 (0:취소): "))
                if choice == 0: return False
                self.current_user = profiles[choice-1]
                print(f"\n✨ {self.current_user['name']}님 프로필 불러오기 완료!")
                return True
            except:
                print("⚠ 올바른 번호를 입력하세요!")

    def generate_weekly_plan(self):
        if not self.current_user:
            print("\n⚠ 먼저 프로필을 생성/선택하세요!")
            return

        print("\n" + "="*60)
        print(f"📅 [{self.current_user['name']}님의 7일 계획]")
        print("="*60)
        
        # 식단 계획 출력
        self.print_diet_plan()
        
        # 운동 계획 생성
        if self.current_user["goal"] == "근육량 증가":
            self.generate_muscle_plan()
        elif self.current_user["goal"] == "체지방 감소":
            self.generate_cardio_plan()
        else:
            self.generate_functional_plan()

    def print_diet_plan(self):
        print("\n🍽️ [일주일 식단 계획]")
        goal = self.current_user["goal"]
        for day in range(1, 8):
            daily_meals = DIET_PLANS[goal][day % len(DIET_PLANS[goal])]
            print(f"\nDay {day}:")
            for meal_type, meal in daily_meals.items():
                print(f"- {meal_type}: {meal['메뉴']}")
                print(f"  칼로리: {meal['칼로리']}kcal | 단백질: {meal['단백질']}g | 탄수화물: {meal['탄수화물']}g | 지방: {meal['지방']}g")

    def generate_muscle_plan(self):
        print("\n💪 [근육량 증가 운동 계획]")
        parts = self.current_user["target_body_parts"]
        for day in range(1, 8):
            if day in [3, 6]:  # 휴식일
                print(f"\nDay {day}: 🛌 휴식일 (가벼운 스트레칭 권장)")
                continue
                
            part = parts[day % len(parts)]
            workouts = random.sample(MUSCLE_WORKOUTS[part], 4)  # 4개 운동 추천
            print(f"\nDay {day}: {part} (총 4종목)")
            for i, ex in enumerate(workouts, 1):
                print(f"{i}. {ex['이름']} ({ex['세트']})")
                print(f"   → {ex['가이드']}")

    def generate_cardio_plan(self):
        print("\n🏃 [체지방 감소 운동 계획]")
        cardio = random.choice(CARDIO_WORKOUTS)
        for day in range(1, 8):
            if day in [2, 5]:  # 주 2회 유산소
                print(f"\nDay {day}: 유산소 운동")
                print(f"- {cardio['이름']} ({cardio['시간']})")
                print(f"  강도: {cardio['강도']} | 예상 칼로리 소모: {cardio['칼로리소모']}")
            else:
                print(f"\nDay {day}: 근력 운동")
                # 근력운동 추가 가능

    def generate_functional_plan(self):
        print("\n🧘 [기능성 운동 계획]")
        for day in range(1, 8):
            workout = random.choice(FUNCTIONAL_WORKOUTS)
            print(f"\nDay {day}: {workout['이름']}")
            print(f"- 시간/횟수: {workout['시간']}")
            print(f"- 주요 효과: {workout['효과']}")
            print(f"- 자세 요령: {workout['가이드']}")

# ========================== 메인 실행 ==========================
def show_title():
    print("\n" + "="*60)
    print(" " * 20 + "🏆 FIT HERO 🏆")
    print("="*60)
    print(" " * 15 + "맞춤형 피트니스 프로그램")
    print("="*60)

def main():
    show_title()
    program = FitnessProgram()
    
    while True:
        print("\n" + "="*50)
        print(" " * 15 + "🎮 메인 메뉴")
        print("="*50)
        print("1. 새 프로필 생성")
        print("2. 프로필 불러오기")
        print("3. 일주일 계획 생성")
        print("4. 종료")
        print("="*50)
        
        choice = input(">> 선택: ").strip()
        
        if choice == "1":
            program.create_profile()
        elif choice == "2":
            program.load_profile()
        elif choice == "3":
            program.generate_weekly_plan()
        elif choice == "4":
            print("\n🎯 프로그램을 종료합니다. 건강한 하루 되세요!")
            break
        else:
            print("\n⚠ 올바른 메뉴를 선택하세요!")
        
        input("\n🔴 계속하려면 엔터를 누르세요...")

if __name__ == "__main__":
    main()