from datetime import date, datetime


# =========================================================
# 24절기 기본 정보
# =========================================================
#
# 24절기는 실제로는 태양의 황경을 기준으로 결정되기 때문에
# 해마다 정확한 시각과 날짜가 조금씩 달라질 수 있습니다.
#
# 날담에서는 '오늘이 어떤 계절의 흐름에 있는가'를 보여주는
# 용도로 사용하기 위해 대표 날짜를 기준으로 표시합니다.
# =========================================================

SOLAR_TERMS = [

    {
        "name": "소한",
        "month": 1,
        "day": 5,
        "emoji": "❄️",
        "description": "추위가 본격적으로 시작되는 때입니다.",
        "story": "이름은 '작은 추위'지만 우리나라에서는 오히려 대한보다 더 추운 경우가 많습니다.",
    },

    {
        "name": "대한",
        "month": 1,
        "day": 20,
        "emoji": "❄️",
        "description": "한 해의 추위가 절정에 이르는 때입니다.",
        "story": "24절기의 마지막 절기로, 대한이 지나면 다시 봄의 시작인 입춘을 맞이합니다.",
    },

    {
        "name": "입춘",
        "month": 2,
        "day": 4,
        "emoji": "🌱",
        "description": "봄의 시작을 알리는 절기입니다.",
        "story": "아직 날씨는 춥지만 절기상으로는 이날부터 새로운 봄이 시작됩니다.",
    },

    {
        "name": "우수",
        "month": 2,
        "day": 19,
        "emoji": "💧",
        "description": "눈이 녹아 비가 되고 얼음이 풀리기 시작하는 때입니다.",
        "story": "겨울의 추위가 조금씩 물러나고 봄기운이 느껴지기 시작합니다.",
    },

    {
        "name": "경칩",
        "month": 3,
        "day": 5,
        "emoji": "🐸",
        "description": "겨울잠을 자던 생명들이 깨어나는 때입니다.",
        "story": "땅속에서 겨울을 보내던 벌레와 동물들이 봄기운을 느끼고 움직이기 시작한다고 여겼습니다.",
    },

    {
        "name": "춘분",
        "month": 3,
        "day": 20,
        "emoji": "🌸",
        "description": "낮과 밤의 길이가 거의 같아지는 때입니다.",
        "story": "춘분을 지나면서 낮의 길이가 밤보다 점점 길어집니다.",
    },

    {
        "name": "청명",
        "month": 4,
        "day": 5,
        "emoji": "🌿",
        "description": "하늘이 맑아지고 봄빛이 짙어지는 때입니다.",
        "story": "이름 그대로 하늘이 맑고 밝아진다는 뜻을 가진 봄의 절기입니다.",
    },

    {
        "name": "곡우",
        "month": 4,
        "day": 20,
        "emoji": "🌧️",
        "description": "곡식을 자라게 하는 봄비가 내리는 때입니다.",
        "story": "농사에 필요한 비가 내려 곡식의 성장을 돕는다는 의미를 담고 있습니다.",
    },

    {
        "name": "입하",
        "month": 5,
        "day": 5,
        "emoji": "☀️",
        "description": "여름의 시작을 알리는 절기입니다.",
        "story": "봄이 지나고 자연의 초록빛이 더욱 짙어지는 시기입니다.",
    },

    {
        "name": "소만",
        "month": 5,
        "day": 21,
        "emoji": "🌿",
        "description": "햇빛이 풍부해지고 만물이 자라나는 때입니다.",
        "story": "'조금씩 가득 찬다'는 뜻처럼 자연이 생명력으로 채워지는 시기입니다.",
    },

    {
        "name": "망종",
        "month": 6,
        "day": 6,
        "emoji": "🌾",
        "description": "곡식의 씨를 뿌리기에 알맞은 때입니다.",
        "story": "벼와 보리처럼 까끄라기가 있는 곡식과 관련된 농사의 중요한 절기였습니다.",
    },

    {
        "name": "하지",
        "month": 6,
        "day": 21,
        "emoji": "☀️",
        "description": "일 년 중 낮의 길이가 가장 긴 무렵입니다.",
        "story": "태양이 가장 오래 머무는 시기로, 하지 이후부터 낮의 길이는 조금씩 짧아집니다.",
    },

    {
        "name": "소서",
        "month": 7,
        "day": 7,
        "emoji": "🌤️",
        "description": "본격적인 더위가 시작되는 때입니다.",
        "story": "'작은 더위'라는 뜻으로 여름의 뜨거운 기운이 본격적으로 느껴지기 시작합니다.",
    },

    {
        "name": "대서",
        "month": 7,
        "day": 23,
        "emoji": "🔥",
        "description": "일 년 중 더위가 가장 심한 무렵입니다.",
        "story": "'큰 더위'라는 이름처럼 한여름의 무더위가 절정에 이르는 시기입니다.",
    },

    {
        "name": "입추",
        "month": 8,
        "day": 7,
        "emoji": "🍃",
        "description": "가을의 시작을 알리는 절기입니다.",
        "story": "날씨는 여전히 덥지만 절기상으로는 이날부터 가을의 문턱에 들어섭니다.",
    },

    {
        "name": "처서",
        "month": 8,
        "day": 23,
        "emoji": "🍂",
        "description": "더위가 한풀 꺾이기 시작하는 때입니다.",
        "story": "'더위가 그친다'는 뜻을 가진 절기로 아침저녁으로 가을 기운이 느껴지기 시작합니다.",
    },

    {
        "name": "백로",
        "month": 9,
        "day": 7,
        "emoji": "💧",
        "description": "풀잎에 흰 이슬이 맺히기 시작하는 때입니다.",
        "story": "밤 기온이 내려가면서 풀과 나뭇잎에 이슬이 맺히고 가을의 기운이 더욱 뚜렷해집니다.",
    },

    {
        "name": "추분",
        "month": 9,
        "day": 23,
        "emoji": "🍁",
        "description": "낮과 밤의 길이가 다시 거의 같아지는 때입니다.",
        "story": "추분을 지나면서 밤의 길이가 낮보다 점점 길어집니다.",
    },

    {
        "name": "한로",
        "month": 10,
        "day": 8,
        "emoji": "🍂",
        "description": "찬 기운이 느껴지는 이슬이 맺히는 때입니다.",
        "story": "가을이 깊어지면서 아침저녁의 공기가 눈에 띄게 차가워지는 시기입니다.",
    },

    {
        "name": "상강",
        "month": 10,
        "day": 23,
        "emoji": "🍁",
        "description": "서리가 내리기 시작하는 무렵입니다.",
        "story": "가을의 끝자락으로 접어들며 겨울이 가까워졌음을 느낄 수 있는 절기입니다.",
    },

    {
        "name": "입동",
        "month": 11,
        "day": 7,
        "emoji": "🧣",
        "description": "겨울의 시작을 알리는 절기입니다.",
        "story": "전통적으로 겨울을 준비하고 김장과 월동 준비를 시작하던 시기입니다.",
    },

    {
        "name": "소설",
        "month": 11,
        "day": 22,
        "emoji": "🌨️",
        "description": "첫눈이 내릴 수 있는 겨울의 초입입니다.",
        "story": "'작은 눈'이라는 뜻으로 본격적인 겨울 추위가 오기 전의 시기입니다.",
    },

    {
        "name": "대설",
        "month": 12,
        "day": 7,
        "emoji": "❄️",
        "description": "큰 눈이 내릴 수 있는 한겨울로 접어드는 때입니다.",
        "story": "이름은 '큰 눈'이라는 뜻이지만 실제 날씨와 반드시 일치하는 것은 아닙니다.",
    },

    {
        "name": "동지",
        "month": 12,
        "day": 22,
        "emoji": "🌙",
        "description": "일 년 중 밤이 가장 길고 낮이 가장 짧은 무렵입니다.",
        "story": "동지를 지나면서 낮의 길이가 다시 조금씩 길어지기 시작합니다.",
    },
]


# =========================================================
# 특정 날짜가 절기인지 확인
# =========================================================

def get_solar_term(month, day):

    for term in SOLAR_TERMS:

        if (
            term["month"] == month
            and term["day"] == day
        ):
            return term

    return None


# =========================================================
# 가장 최근에 지난 절기 찾기
# =========================================================

def get_previous_solar_term(year, month, day):

    target = date(
        year,
        month,
        day
    )

    candidates = []

    # 현재 연도의 절기
    for term in SOLAR_TERMS:

        term_date = date(
            year,
            term["month"],
            term["day"]
        )

        if term_date <= target:

            candidates.append(
                (
                    term_date,
                    term
                )
            )

    # 1월 초에는 전년도 동지를 비교해야 함
    if not candidates:

        for term in SOLAR_TERMS:

            term_date = date(
                year - 1,
                term["month"],
                term["day"]
            )

            candidates.append(
                (
                    term_date,
                    term
                )
            )

    candidates.sort(
        key=lambda item: item[0],
        reverse=True
    )

    term_date, term = candidates[0]

    days_passed = (
        target - term_date
    ).days

    result = term.copy()

    result["date"] = term_date
    result["days_passed"] = days_passed

    return result


# =========================================================
# 다음 절기 찾기
# =========================================================

def get_next_solar_term(year, month, day):

    target = date(
        year,
        month,
        day
    )

    candidates = []

    # 현재 연도
    for term in SOLAR_TERMS:

        term_date = date(
            year,
            term["month"],
            term["day"]
        )

        if term_date > target:

            candidates.append(
                (
                    term_date,
                    term
                )
            )

    # 연말이면 다음 해 절기까지 확인
    if not candidates:

        for term in SOLAR_TERMS:

            term_date = date(
                year + 1,
                term["month"],
                term["day"]
            )

            candidates.append(
                (
                    term_date,
                    term
                )
            )

    candidates.sort(
        key=lambda item: item[0]
    )

    term_date, term = candidates[0]

    days_until = (
        term_date - target
    ).days

    result = term.copy()

    result["date"] = term_date
    result["days_until"] = days_until

    return result


# =========================================================
# 오늘의 절기 정보
# =========================================================

def get_solar_term_info(year, month, day):

    today_term = get_solar_term(
        month,
        day
    )

    previous_term = get_previous_solar_term(
        year,
        month,
        day
    )

    next_term = get_next_solar_term(
        year,
        month,
        day
    )

    return {
        "today": today_term,
        "previous": previous_term,
        "next": next_term,
    }


# =========================================================
# 올해의 몇 번째 날
# =========================================================

def get_year_progress(year, month, day):

    target = date(
        year,
        month,
        day
    )

    first_day = date(
        year,
        1,
        1
    )

    last_day = date(
        year,
        12,
        31
    )

    day_number = (
        target - first_day
    ).days + 1

    total_days = (
        last_day - first_day
    ).days + 1

    percentage = (
        day_number
        / total_days
        * 100
    )

    days_remaining = (
        last_day - target
    ).days

    return {
        "day_number": day_number,
        "total_days": total_days,
        "percentage": percentage,
        "days_remaining": days_remaining,
    }