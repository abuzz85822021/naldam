from datetime import datetime
import math


# =========================================================
# 기본 천문 상수
# =========================================================

# 평균 삭망월
# 신월에서 다음 신월까지 약 29.53일
SYNODIC_MONTH = 29.53058867


# 기준 신월 시각
REFERENCE_NEW_MOON = datetime(
    2000,
    1,
    6,
    18,
    14
)


# =========================================================
# 달의 월령 계산
# =========================================================

def get_moon_age(year, month, day):

    target = datetime(
        year,
        month,
        day,
        12,
        0
    )

    diff_days = (
        target - REFERENCE_NEW_MOON
    ).total_seconds() / 86400

    moon_age = diff_days % SYNODIC_MONTH

    return moon_age


# =========================================================
# 달의 위상
# =========================================================

def get_moon_phase(year, month, day):

    age = get_moon_age(
        year,
        month,
        day
    )

    if age < 1.85:

        return {
            "icon": "🌑",
            "name": "삭 · 신월",
            "age": age,
            "description":
                "달이 태양과 거의 같은 방향에 있어 "
                "지구에서는 밝은 면이 거의 보이지 않는 시기입니다."
        }

    elif age < 5.54:

        return {
            "icon": "🌒",
            "name": "초승달",
            "age": age,
            "description":
                "신월이 지난 뒤 달의 밝은 부분이 "
                "조금씩 커지기 시작하는 시기입니다."
        }

    elif age < 9.23:

        return {
            "icon": "🌓",
            "name": "상현달",
            "age": age,
            "description":
                "달의 절반 정도가 밝게 보입니다. "
                "보름달을 향해 점점 차오르고 있습니다."
        }

    elif age < 12.92:

        return {
            "icon": "🌔",
            "name": "차오르는 달",
            "age": age,
            "description":
                "달의 절반 이상이 밝게 보이며 "
                "보름달에 가까워지고 있습니다."
        }

    elif age < 16.61:

        return {
            "icon": "🌕",
            "name": "보름달",
            "age": age,
            "description":
                "태양빛을 받는 달의 면이 지구에서 "
                "거의 원형으로 보이는 시기입니다."
        }

    elif age < 20.30:

        return {
            "icon": "🌖",
            "name": "기우는 달",
            "age": age,
            "description":
                "보름이 지난 뒤 달의 밝은 부분이 "
                "조금씩 줄어들고 있습니다."
        }

    elif age < 23.99:

        return {
            "icon": "🌗",
            "name": "하현달",
            "age": age,
            "description":
                "달의 절반 정도가 밝게 보이며 "
                "그믐을 향해 기울고 있습니다."
        }

    elif age < 27.68:

        return {
            "icon": "🌘",
            "name": "그믐달",
            "age": age,
            "description":
                "달의 밝은 부분이 매우 가늘어지며 "
                "다음 신월을 향해 가는 시기입니다."
        }

    else:

        return {
            "icon": "🌑",
            "name": "삭 직전",
            "age": age,
            "description":
                "달이 거의 보이지 않는 시기로 "
                "곧 새로운 달의 주기가 시작됩니다."
        }


# =========================================================
# 달 밝기 계산
# =========================================================

def get_moon_illumination(year, month, day):

    age = get_moon_age(
        year,
        month,
        day
    )

    phase_angle = (
        2
        * math.pi
        * age
        / SYNODIC_MONTH
    )

    illumination = (
        1
        - math.cos(phase_angle)
    ) / 2

    return illumination * 100


# =========================================================
# 다음 보름달까지 남은 날
# =========================================================

def days_until_full_moon(year, month, day):

    age = get_moon_age(
        year,
        month,
        day
    )

    full_moon_age = (
        SYNODIC_MONTH / 2
    )

    if age <= full_moon_age:

        remain = (
            full_moon_age
            - age
        )

    else:

        remain = (
            SYNODIC_MONTH
            - age
            + full_moon_age
        )

    return remain


# =========================================================
# 다음 신월까지 남은 날
# =========================================================

def days_until_new_moon(year, month, day):

    age = get_moon_age(
        year,
        month,
        day
    )

    if age < 0.5:
        return 0.0

    return SYNODIC_MONTH - age


# =========================================================
# 황도 12궁
# =========================================================

ZODIAC = [

    {
        "name": "염소자리",
        "symbol": "♑",
        "english": "Capricorn",
        "start": (12, 22),
        "end": (1, 19),
        "bright_star": "데네브 알게디",
        "description":
            "황도 12궁 가운데 하나로 "
            "남쪽 하늘에서 볼 수 있는 별자리입니다."
    },

    {
        "name": "물병자리",
        "symbol": "♒",
        "english": "Aquarius",
        "start": (1, 20),
        "end": (2, 18),
        "bright_star": "사달수드",
        "description":
            "물을 붓는 사람의 모습으로 표현되는 "
            "고대부터 알려진 황도 별자리입니다."
    },

    {
        "name": "물고기자리",
        "symbol": "♓",
        "english": "Pisces",
        "start": (2, 19),
        "end": (3, 20),
        "bright_star": "에타 피시움",
        "description":
            "두 마리의 물고기가 끈으로 연결된 모습으로 "
            "표현되는 황도 별자리입니다."
    },

    {
        "name": "양자리",
        "symbol": "♈",
        "english": "Aries",
        "start": (3, 21),
        "end": (4, 19),
        "bright_star": "하말",
        "description":
            "황도 12궁 가운데 하나로 "
            "고대 천문학에서 중요한 위치를 차지했던 별자리입니다."
    },

    {
        "name": "황소자리",
        "symbol": "♉",
        "english": "Taurus",
        "start": (4, 20),
        "end": (5, 20),
        "bright_star": "알데바란",
        "description":
            "붉게 빛나는 알데바란과 "
            "플레이아데스 성단으로 유명한 별자리입니다."
    },

    {
        "name": "쌍둥이자리",
        "symbol": "♊",
        "english": "Gemini",
        "start": (5, 21),
        "end": (6, 21),
        "bright_star": "폴룩스",
        "description":
            "카스토르와 폴룩스라는 두 밝은 별로 "
            "잘 알려진 황도 별자리입니다."
    },

    {
        "name": "게자리",
        "symbol": "♋",
        "english": "Cancer",
        "start": (6, 22),
        "end": (7, 22),
        "bright_star": "알 타르프",
        "description":
            "황도 12궁 가운데 비교적 어두운 별자리이며 "
            "프레세페 성단이 위치해 있습니다."
    },

    {
        "name": "사자자리",
        "symbol": "♌",
        "english": "Leo",
        "start": (7, 23),
        "end": (8, 22),
        "bright_star": "레굴루스",
        "description":
            "사자의 모습을 닮은 대표적인 황도 별자리로 "
            "밝은 별 레굴루스가 유명합니다."
    },

    {
        "name": "처녀자리",
        "symbol": "♍",
        "english": "Virgo",
        "start": (8, 23),
        "end": (9, 22),
        "bright_star": "스피카",
        "description":
            "황도 12궁 가운데 매우 큰 별자리이며 "
            "밝은 별 스피카가 유명합니다."
    },

    {
        "name": "천칭자리",
        "symbol": "♎",
        "english": "Libra",
        "start": (9, 23),
        "end": (10, 22),
        "bright_star": "주베넬게누비",
        "description":
            "저울의 모습을 나타내는 황도 별자리입니다."
    },

    {
        "name": "전갈자리",
        "symbol": "♏",
        "english": "Scorpius",
        "start": (10, 23),
        "end": (11, 21),
        "bright_star": "안타레스",
        "description":
            "여름철 남쪽 하늘에서 쉽게 볼 수 있으며 "
            "붉은 별 안타레스로 유명합니다."
    },

    {
        "name": "사수자리",
        "symbol": "♐",
        "english": "Sagittarius",
        "start": (11, 22),
        "end": (12, 21),
        "bright_star": "카우스 오스트랄리스",
        "description":
            "우리 은하 중심 방향에 위치해 "
            "별과 성운이 풍부한 황도 별자리입니다."
    },
]


# =========================================================
# 황도 12궁 찾기
# =========================================================

def get_zodiac(month, day):

    current = month * 100 + day

    for zodiac in ZODIAC:

        start_month, start_day = zodiac["start"]
        end_month, end_day = zodiac["end"]

        start_value = (
            start_month * 100
            + start_day
        )

        end_value = (
            end_month * 100
            + end_day
        )

        # 염소자리처럼 연말 → 연초
        if start_value > end_value:

            if (
                current >= start_value
                or current <= end_value
            ):
                return zodiac

        else:

            if (
                start_value
                <= current
                <= end_value
            ):
                return zodiac

    return None


# =========================================================
# 계절별 대표 별자리
# 한국 기준
# =========================================================

def get_season_constellation(month):

    if month in [3, 4, 5]:

        return {
            "season": "봄",
            "name": "사자자리",
            "symbol": "♌",
            "bright_star": "레굴루스",
            "description":
                "봄철 밤하늘을 대표하는 별자리입니다. "
                "사자의 머리 부분에 해당하는 별 배열을 이용하면 "
                "비교적 쉽게 찾을 수 있습니다."
        }

    elif month in [6, 7, 8]:

        return {
            "season": "여름",
            "name": "전갈자리",
            "symbol": "♏",
            "bright_star": "안타레스",
            "description":
                "여름철 남쪽 하늘을 대표하는 별자리입니다. "
                "붉게 빛나는 안타레스가 전갈의 심장에 해당합니다."
        }

    elif month in [9, 10, 11]:

        return {
            "season": "가을",
            "name": "페가수스자리",
            "symbol": "✨",
            "bright_star": "마르카브",
            "description":
                "가을철 밤하늘의 대표적인 별자리입니다. "
                "네 개의 별이 만드는 가을의 대사각형이 유명합니다."
        }

    else:

        return {
            "season": "겨울",
            "name": "오리온자리",
            "symbol": "✨",
            "bright_star": "베텔게우스",
            "description":
                "겨울 밤하늘을 대표하는 유명한 별자리입니다. "
                "가운데 나란히 늘어선 세 별로 쉽게 찾을 수 있습니다."
        }


# =========================================================
# 주요 유성우
#
# 여기서의 기간은 날담에서 보기 좋도록
# 극대일 전후의 '주요 관찰 기간'을 표시합니다.
# 실제 유성우의 전체 활동 기간은 더 길 수 있습니다.
# =========================================================

METEOR_SHOWERS = [

    {
        "name": "사분의자리 유성우",
        "start": (1, 1),
        "end": (1, 5),
        "peak": (1, 3),
        "description":
            "1월 초 밤하늘에서 만날 수 있는 "
            "대표적인 겨울철 유성우입니다."
    },

    {
        "name": "거문고자리 유성우",
        "start": (4, 19),
        "end": (4, 24),
        "peak": (4, 22),
        "description":
            "4월 하순에 볼 수 있으며 "
            "오랜 관측 기록을 가진 유성우입니다."
    },

    {
        "name": "페르세우스자리 유성우",
        "start": (8, 10),
        "end": (8, 14),
        "peak": (8, 12),
        "description":
            "여름철 가장 유명한 유성우 가운데 하나입니다. "
            "8월 중순 밤하늘의 대표적인 천문 현상입니다."
    },

    {
        "name": "오리온자리 유성우",
        "start": (10, 18),
        "end": (10, 23),
        "peak": (10, 21),
        "description":
            "핼리 혜성이 남긴 먼지와 관련된 "
            "대표적인 가을철 유성우입니다."
    },

    {
        "name": "쌍둥이자리 유성우",
        "start": (12, 11),
        "end": (12, 15),
        "peak": (12, 14),
        "description":
            "12월 밤하늘에서 만날 수 있는 "
            "매우 활발한 유성우 가운데 하나입니다."
    },
]


# =========================================================
# 날짜 범위 확인
# =========================================================

def date_in_range(
    month,
    day,
    start,
    end
):

    current = (
        month * 100
        + day
    )

    start_value = (
        start[0] * 100
        + start[1]
    )

    end_value = (
        end[0] * 100
        + end[1]
    )

    # 일반적인 기간
    if start_value <= end_value:

        return (
            start_value
            <= current
            <= end_value
        )

    # 연말 → 연초로 넘어가는 기간도 대응
    return (
        current >= start_value
        or current <= end_value
    )


# =========================================================
# 해당 날짜의 유성우 찾기
# =========================================================

def get_meteor_shower(month, day):

    for shower in METEOR_SHOWERS:

        if date_in_range(
            month,
            day,
            shower["start"],
            shower["end"]
        ):

            peak_month, peak_day = (
                shower["peak"]
            )

            result = shower.copy()

            result["is_peak"] = (
                month == peak_month
                and day == peak_day
            )

            return result

    return None


# =========================================================
# 오늘의 하늘 정보
#
# app.py에서는 이 함수 하나만 호출하면 됩니다.
# =========================================================

def get_sky_info(year, month, day):

    moon = get_moon_phase(
        year,
        month,
        day
    )

    illumination = get_moon_illumination(
        year,
        month,
        day
    )

    zodiac = get_zodiac(
        month,
        day
    )

    full_moon_days = days_until_full_moon(
        year,
        month,
        day
    )

    new_moon_days = days_until_new_moon(
        year,
        month,
        day
    )

    season_constellation = (
        get_season_constellation(
            month
        )
    )

    meteor_shower = (
        get_meteor_shower(
            month,
            day
        )
    )

    return {
        "moon": moon,
        "illumination": illumination,

        # ↓ 아까 KeyError가 났던 값
        "full_moon_days": full_moon_days,

        "new_moon_days": new_moon_days,

        "zodiac": zodiac,

        "season_constellation":
            season_constellation,

        "meteor_shower":
            meteor_shower,
    }