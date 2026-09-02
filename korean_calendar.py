from korean_lunar_calendar import KoreanLunarCalendar


def solar_to_lunar(year, month, day):
    """
    양력 날짜를 음력 날짜로 변환
    """

    calendar = KoreanLunarCalendar()

    # 양력 날짜 입력
    calendar.setSolarDate(year, month, day)

    return {
        "year": calendar.lunarYear,
        "month": calendar.lunarMonth,
        "day": calendar.lunarDay,
        "is_leap": calendar.isIntercalation,
    }


def is_sonnal(lunar_day):
    """
    손 없는 날인지 확인

    음력 날짜의 끝자리가
    9 또는 0이면 손 없는 날
    """

    return lunar_day % 10 in [9, 0]