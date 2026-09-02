from datetime import date, timedelta

from korean_calendar import solar_to_lunar


# =========================================================
# 날담 - 대한민국 기념일 / 공휴일
# =========================================================

ANNIVERSARIES = []


def add_anniversary(
    name,
    month=None,
    day=None,
    category="memorial_day",
    description="",
    emoji="🎗️",
    movable=None,
):
    ANNIVERSARIES.append(
        {
            "name": name,
            "month": month,
            "day": day,
            "category": category,
            "description": description,
            "emoji": emoji,
            "movable": movable,
        }
    )


# =========================================================
# 국경일
# =========================================================

add_anniversary(
    "3·1절",
    3,
    1,
    "national_holiday",
    "1919년 3·1운동의 독립정신을 기리는 국경일입니다.",
    "🇰🇷",
)

add_anniversary(
    "제헌절",
    7,
    17,
    "national_holiday",
    "대한민국 헌법의 제정과 공포를 기념하는 국경일입니다.",
    "📜",
)

add_anniversary(
    "광복절",
    8,
    15,
    "national_holiday",
    "우리나라의 광복을 기념하는 국경일입니다.",
    "🇰🇷",
)

add_anniversary(
    "개천절",
    10,
    3,
    "national_holiday",
    "우리 민족의 건국 이념을 되새기는 국경일입니다.",
    "🌄",
)

add_anniversary(
    "한글날",
    10,
    9,
    "national_holiday",
    "한글의 창제와 반포를 기념하는 국경일입니다.",
    "🔤",
)


# =========================================================
# 대한민국 주요 기념일
# =========================================================

FIXED_ANNIVERSARIES = [
    (
        "2·28민주운동 기념일",
        2,
        28,
        "🕊️",
        "2·28민주운동의 민주주의 정신을 기리는 날입니다.",
    ),
    (
        "납세자의 날",
        3,
        3,
        "🧾",
        "성실한 납세와 세금의 중요성을 되새기는 날입니다.",
    ),
    (
        "3·8민주의거 기념일",
        3,
        8,
        "🕊️",
        "3·8민주의거의 민주주의 정신을 기리는 날입니다.",
    ),
    (
        "3·15의거 기념일",
        3,
        15,
        "🕊️",
        "3·15의거의 역사적 의미를 되새기는 날입니다.",
    ),
    (
        "4·3희생자 추념일",
        4,
        3,
        "🕯️",
        "제주4·3 희생자를 추모하는 날입니다.",
    ),
    (
        "보건의 날",
        4,
        7,
        "⚕️",
        "국민 보건과 건강의 중요성을 되새기는 날입니다.",
    ),
    (
        "대한민국 임시정부 수립 기념일",
        4,
        11,
        "🇰🇷",
        "대한민국 임시정부 수립을 기념하는 날입니다.",
    ),
    (
        "4·19혁명 기념일",
        4,
        19,
        "🕊️",
        "4·19혁명의 민주주의 정신을 기리는 날입니다.",
    ),
    (
        "과학의 날",
        4,
        21,
        "🔬",
        "과학기술의 중요성을 되새기는 날입니다.",
    ),
    (
        "법의 날",
        4,
        25,
        "⚖️",
        "법치주의의 중요성을 되새기는 날입니다.",
    ),
    (
        "근로자의 날",
        5,
        1,
        "🛠️",
        "근로자의 노고와 권익을 기리는 날입니다.",
    ),
    (
        "어린이날",
        5,
        5,
        "🧒",
        "어린이의 행복과 건강한 성장을 바라는 날입니다.",
    ),
    (
        "어버이날",
        5,
        8,
        "💐",
        "부모의 사랑과 은혜에 감사하는 날입니다.",
    ),
    (
        "동학농민혁명 기념일",
        5,
        11,
        "🌾",
        "동학농민혁명의 역사적 의미를 되새기는 날입니다.",
    ),
    (
        "스승의 날",
        5,
        15,
        "📚",
        "스승의 은혜와 교육의 가치를 되새기는 날입니다.",
    ),
    (
        "5·18민주화운동 기념일",
        5,
        18,
        "🕊️",
        "5·18민주화운동의 민주주의 정신을 기리는 날입니다.",
    ),
    (
        "부부의 날",
        5,
        21,
        "💑",
        "부부와 가족의 소중함을 되새기는 날입니다.",
    ),
    (
        "바다의 날",
        5,
        31,
        "🌊",
        "바다와 해양산업의 중요성을 되새기는 날입니다.",
    ),
    (
        "현충일",
        6,
        6,
        "🕯️",
        "순국선열과 호국영령을 추모하는 날입니다.",
    ),
    (
        "6·10민주항쟁 기념일",
        6,
        10,
        "🕊️",
        "6월 민주항쟁의 민주주의 정신을 되새기는 날입니다.",
    ),
    (
        "6·10만세운동 기념일",
        6,
        10,
        "🇰🇷",
        "6·10만세운동의 독립정신을 기리는 날입니다.",
    ),
    (
        "6·25전쟁일",
        6,
        25,
        "🕯️",
        "6·25전쟁을 기억하고 평화의 소중함을 되새기는 날입니다.",
    ),
    (
        "정보보호의 날",
        7,
        8,
        "🔐",
        "정보보호의 중요성을 되새기는 날입니다.",
    ),
    (
        "북한이탈주민의 날",
        7,
        14,
        "🤝",
        "북한이탈주민의 정착과 사회통합을 생각하는 날입니다.",
    ),
    (
        "국군의 날",
        10,
        1,
        "🪖",
        "대한민국 국군의 역할과 국가수호의 의미를 되새기는 날입니다.",
    ),
    (
        "노인의 날",
        10,
        2,
        "👵",
        "노인에 대한 존경과 복지의 중요성을 되새기는 날입니다.",
    ),
    (
        "부마민주항쟁 기념일",
        10,
        16,
        "🕊️",
        "부마민주항쟁의 민주주의 정신을 기리는 날입니다.",
    ),
    (
        "문화의 날",
        10,
        17,
        "🎨",
        "문화예술의 중요성을 되새기는 날입니다.",
    ),
    (
        "경찰의 날",
        10,
        21,
        "👮",
        "경찰의 역할과 국민 안전의 중요성을 되새기는 날입니다.",
    ),
    (
        "국제연합일",
        10,
        24,
        "🌐",
        "국제평화와 국제연합의 의미를 되새기는 날입니다.",
    ),
    (
        "교정의 날",
        10,
        28,
        "⚖️",
        "교정행정과 재사회화의 의미를 되새기는 날입니다.",
    ),
    (
        "농업인의 날",
        11,
        11,
        "🌾",
        "농업과 농업인의 소중함을 되새기는 날입니다.",
    ),
    (
        "무역의 날",
        12,
        5,
        "🚢",
        "무역과 수출 산업의 중요성을 되새기는 날입니다.",
    ),
]


for (
    name,
    month,
    day,
    emoji,
    description,
) in FIXED_ANNIVERSARIES:

    add_anniversary(
        name,
        month,
        day,
        "memorial_day",
        description,
        emoji,
    )


# =========================================================
# 날짜가 매년 바뀌는 기념일
# =========================================================

add_anniversary(
    "상공의 날",
    category="memorial_day",
    emoji="🏭",
    description="상공업의 발전과 산업 진흥의 의미를 되새기는 날입니다.",
    movable={
        "month": 3,
        "weekday": 2,
        "nth": 3,
    },
)


add_anniversary(
    "서해수호의 날",
    category="memorial_day",
    emoji="⚓",
    description="서해수호를 위해 희생한 이들을 기리는 날입니다.",
    movable={
        "month": 3,
        "weekday": 4,
        "nth": 4,
    },
)


# =========================================================
# 변동 기념일 계산
# =========================================================

def get_nth_weekday(
    year,
    month,
    weekday,
    nth,
):

    first_day = date(
        year,
        month,
        1,
    )

    offset = (
        weekday
        - first_day.weekday()
    ) % 7

    target_day = (
        1
        + offset
        + (nth - 1) * 7
    )

    return date(
        year,
        month,
        target_day,
    )


# =========================================================
# 음력 정보
# =========================================================

def get_lunar_info(
    year,
    month,
    day,
):

    return solar_to_lunar(
        year,
        month,
        day,
    )


def is_seollal_eve(
    year,
    month,
    day,
):

    today = date(
        year,
        month,
        day,
    )

    tomorrow = (
        today
        + timedelta(days=1)
    )

    lunar_today = get_lunar_info(
        today.year,
        today.month,
        today.day,
    )

    lunar_tomorrow = get_lunar_info(
        tomorrow.year,
        tomorrow.month,
        tomorrow.day,
    )

    return (
        lunar_today["month"] == 12
        and
        lunar_tomorrow["month"] == 1
        and
        lunar_tomorrow["day"] == 1
        and
        not lunar_today.get(
            "is_leap",
            False,
        )
        and
        not lunar_tomorrow.get(
            "is_leap",
            False,
        )
    )


# =========================================================
# 기본 공휴일
# 대체공휴일은 여기서 제외
# =========================================================

def get_base_public_holiday_info(
    year,
    month,
    day,
):

    target = date(
        year,
        month,
        day,
    )


    # -----------------------------------------------------
    # 양력 고정 공휴일
    # -----------------------------------------------------

    if (month, day) == (1, 1):

        return {
            "name": "신정",
            "emoji": "🎉",
            "kind": "new_year",
            "description": "새해의 첫날입니다.",
            "show_as_anniversary": True,
        }


    if (month, day) == (3, 1):

        return {
            "name": "3·1절",
            "emoji": "🇰🇷",
            "kind": "national",
            "description": (
                "3·1운동의 독립정신을 "
                "기리는 국경일이자 공휴일입니다."
            ),
        }


    if (month, day) == (5, 5):

        return {
            "name": "어린이날",
            "emoji": "🧒",
            "kind": "children",
            "description": (
                "어린이의 행복과 건강한 "
                "성장을 바라는 공휴일입니다."
            ),
        }


    if (month, day) == (6, 6):

        return {
            "name": "현충일",
            "emoji": "🕯️",
            "kind": "memorial",
            "description": (
                "순국선열과 호국영령을 "
                "추모하는 공휴일입니다."
            ),
        }


    # -----------------------------------------------------
    # 제헌절
    #
    # 2007년까지 공휴일
    # 2008~2025년 비공휴일
    # 2026년부터 다시 공휴일
    # -----------------------------------------------------

    if (month, day) == (7, 17):

        if (
            year <= 2007
            or year >= 2026
        ):

            return {
                "name": "제헌절",
                "emoji": "📜",
                "kind": "national",
                "description": (
                    "대한민국 헌법의 제정과 공포를 "
                    "기념하는 국경일이자 공휴일입니다."
                ),
            }


    if (month, day) == (8, 15):

        return {
            "name": "광복절",
            "emoji": "🇰🇷",
            "kind": "national",
            "description": (
                "광복을 기념하는 "
                "국경일이자 공휴일입니다."
            ),
        }


    if (month, day) == (10, 3):

        return {
            "name": "개천절",
            "emoji": "🌄",
            "kind": "national",
            "description": (
                "우리 민족의 건국 이념을 "
                "되새기는 국경일이자 공휴일입니다."
            ),
        }


    if (month, day) == (10, 9):

        return {
            "name": "한글날",
            "emoji": "🔤",
            "kind": "national",
            "description": (
                "한글의 창제와 반포를 "
                "기념하는 국경일이자 공휴일입니다."
            ),
        }


    if (month, day) == (12, 25):

        return {
            "name": "성탄절",
            "emoji": "🎄",
            "kind": "christmas",
            "description": (
                "기독탄신일로 지정된 "
                "공휴일입니다."
            ),
            "show_as_anniversary": True,
        }


    # -----------------------------------------------------
    # 근로자의 날
    # -----------------------------------------------------

    if (
        (month, day) == (5, 1)
        and
        year >= 2027
    ):

        return {
            "name": "노동절",
            "emoji": "🛠️",
            "kind": "labor",
            "description": (
                "근로자의 노고와 권익을 "
                "기리는 공휴일입니다."
            ),
            "show_as_anniversary": True,
        }


    # -----------------------------------------------------
    # 2026년 전국동시지방선거
    # -----------------------------------------------------

    if target == date(
        2026,
        6,
        3,
    ):

        return {
            "name": "제9회 전국동시지방선거",
            "emoji": "🗳️",
            "kind": "election",
            "description": (
                "공직선거법에 따른 "
                "임기만료 선거일로 공휴일입니다."
            ),
            "show_as_anniversary": True,
        }


    # -----------------------------------------------------
    # 음력 공휴일
    # -----------------------------------------------------

    lunar = get_lunar_info(
        year,
        month,
        day,
    )

    is_leap = lunar.get(
        "is_leap",
        False,
    )


    if not is_leap:

        # 설날 전날

        if is_seollal_eve(
            year,
            month,
            day,
        ):

            return {
                "name": "설날 연휴",
                "emoji": "🧧",
                "kind": "seollal",
                "description": (
                    "설날 전날로 지정된 "
                    "공휴일입니다."
                ),
                "show_as_anniversary": True,
            }


        # 설날

        if (
            lunar["month"] == 1
            and
            lunar["day"] == 1
        ):

            return {
                "name": "설날",
                "emoji": "🧧",
                "kind": "seollal",
                "description": (
                    "음력 정월 초하루로 "
                    "우리나라의 대표적인 명절입니다."
                ),
                "show_as_anniversary": True,
            }


        # 설날 다음날

        if (
            lunar["month"] == 1
            and
            lunar["day"] == 2
        ):

            return {
                "name": "설날 연휴",
                "emoji": "🧧",
                "kind": "seollal",
                "description": (
                    "설날 다음 날로 지정된 "
                    "공휴일입니다."
                ),
                "show_as_anniversary": True,
            }


        # 부처님오신날

        if (
            lunar["month"] == 4
            and
            lunar["day"] == 8
        ):

            return {
                "name": "부처님오신날",
                "emoji": "🪷",
                "kind": "buddha",
                "description": (
                    "음력 4월 8일, "
                    "부처님의 탄생을 기념하는 공휴일입니다."
                ),
                "show_as_anniversary": True,
            }


        # 추석 전날

        if (
            lunar["month"] == 8
            and
            lunar["day"] == 14
        ):

            return {
                "name": "추석 연휴",
                "emoji": "🌕",
                "kind": "chuseok",
                "description": (
                    "추석 전날로 지정된 "
                    "공휴일입니다."
                ),
                "show_as_anniversary": True,
            }


        # 추석

        if (
            lunar["month"] == 8
            and
            lunar["day"] == 15
        ):

            return {
                "name": "추석",
                "emoji": "🌕",
                "kind": "chuseok",
                "description": (
                    "음력 8월 15일, "
                    "한 해의 수확에 감사하고 "
                    "가족과 함께하는 대표적인 명절입니다."
                ),
                "show_as_anniversary": True,
            }


        # 추석 다음날

        if (
            lunar["month"] == 8
            and
            lunar["day"] == 16
        ):

            return {
                "name": "추석 연휴",
                "emoji": "🌕",
                "kind": "chuseok",
                "description": (
                    "추석 다음 날로 지정된 "
                    "공휴일입니다."
                ),
                "show_as_anniversary": True,
            }


    return None


# =========================================================
# 해당 연도의 기본 공휴일
# =========================================================

def get_base_public_holidays_for_year(
    year,
):

    holidays = {}

    current = date(
        year,
        1,
        1,
    )

    end = date(
        year,
        12,
        31,
    )


    while current <= end:

        info = get_base_public_holiday_info(
            current.year,
            current.month,
            current.day,
        )

        if info:

            holidays[current] = info


        current += timedelta(
            days=1
        )


    return holidays


# =========================================================
# 대체공휴일 대상 판정
# =========================================================

def needs_substitute_holiday(
    target,
    info,
):

    weekday = target.weekday()

    kind = info.get(
        "kind"
    )


    # 토요일 또는 일요일과 겹치면 대체공휴일

    if kind in {
        "national",
        "children",
        "buddha",
        "christmas",
        "labor",
    }:

        return weekday in {
            5,
            6,
        }


    # 설날 / 추석 연휴는 일요일과 겹치는 경우

    if kind in {
        "seollal",
        "chuseok",
    }:

        return weekday == 6


    return False


# =========================================================
# 대체공휴일 계산
# =========================================================

def get_substitute_holidays_for_year(
    year,
):

    base_holidays = (
        get_base_public_holidays_for_year(
            year
        )
    )

    substitute_holidays = {}


    for (
        original_date,
        info,
    ) in sorted(
        base_holidays.items()
    ):

        if not needs_substitute_holiday(
            original_date,
            info,
        ):

            continue


        candidate = (
            original_date
            + timedelta(days=1)
        )


        while (
            candidate.weekday()
            in {5, 6}
            or
            candidate
            in base_holidays
            or
            candidate
            in substitute_holidays
        ):

            candidate += timedelta(
                days=1
            )


        substitute_holidays[
            candidate
        ] = {
            "name": (
                f'{info["name"]} '
                f'대체공휴일'
            ),
            "emoji": "🔴",
            "kind": "substitute",
            "description": (
                f'{info["name"]}에 따른 '
                f'대체공휴일입니다.'
            ),
            "show_as_anniversary": True,
        }


    return substitute_holidays


# =========================================================
# 공휴일 캐시
# =========================================================

PUBLIC_HOLIDAY_CACHE = {}


def get_public_holidays_for_year(
    year,
):

    if year in PUBLIC_HOLIDAY_CACHE:

        return PUBLIC_HOLIDAY_CACHE[
            year
        ]


    holidays = (
        get_base_public_holidays_for_year(
            year
        )
    )


    substitute_holidays = (
        get_substitute_holidays_for_year(
            year
        )
    )


    holidays.update(
        substitute_holidays
    )


    PUBLIC_HOLIDAY_CACHE[
        year
    ] = holidays


    return holidays


# =========================================================
# 특정 날짜 공휴일 정보
# =========================================================

def get_public_holiday_info(
    year,
    month,
    day,
):

    target = date(
        year,
        month,
        day,
    )


    holidays = (
        get_public_holidays_for_year(
            year
        )
    )


    return holidays.get(
        target
    )


# =========================================================
# 공휴일 여부
# =========================================================

def is_public_holiday(
    year,
    month,
    day,
):

    return (
        get_public_holiday_info(
            year,
            month,
            day,
        )
        is not None
    )


# =========================================================
# 달력에서 빨간색으로 표시할 날짜
# =========================================================

def is_red_calendar_day(
    year,
    month,
    day,
):

    target = date(
        year,
        month,
        day,
    )


    # 일요일

    if target.weekday() == 6:

        return True


    # 공휴일

    if is_public_holiday(
        year,
        month,
        day,
    ):

        return True


    return False


# =========================================================
# 특정 날짜의 기념일
# =========================================================

def get_anniversaries(
    year,
    month,
    day,
):

    target = date(
        year,
        month,
        day,
    )

    results = []


    # -----------------------------------------------------
    # 일반 기념일
    # -----------------------------------------------------

    for item in ANNIVERSARIES:

        # 고정 날짜

        if (
            item["month"] == month
            and
            item["day"] == day
        ):

            results.append(
                item
            )

            continue


        # 변동 날짜

        movable = item.get(
            "movable"
        )


        if movable:

            movable_date = (
                get_nth_weekday(
                    year,
                    movable["month"],
                    movable["weekday"],
                    movable["nth"],
                )
            )


            if target == movable_date:

                results.append(
                    item
                )


    # -----------------------------------------------------
    # 설날 / 추석 / 성탄절 등도 기념일 카드에 표시
    # -----------------------------------------------------

    holiday = (
        get_public_holiday_info(
            year,
            month,
            day,
        )
    )


    if (
        holiday
        and
        holiday.get(
            "show_as_anniversary",
            False,
        )
    ):

        already_exists = any(
            item["name"]
            == holiday["name"]
            for item in results
        )


        if not already_exists:

            results.append(
                {
                    "name":
                        holiday["name"],

                    "month":
                        month,

                    "day":
                        day,

                    "category":
                        "public_holiday",

                    "description":
                        holiday.get(
                            "description",
                            "",
                        ),

                    "emoji":
                        holiday.get(
                            "emoji",
                            "🔴",
                        ),

                    "movable":
                        None,
                }
            )


    return results