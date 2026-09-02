import streamlit as st
import calendar
import base64

from pathlib import Path
from datetime import datetime

from korean_calendar import (
    solar_to_lunar,
    is_sonnal,
)

from history.korea_history import (
    get_korea_history,
)

from history.world_history import (
    get_world_history,
)

from astronomy import (
    get_sky_info,
)

from solar_terms import (
    get_solar_term_info,
    get_year_progress,
)

from anniversaries import (
    get_anniversaries,
    get_public_holiday_info,
    is_red_calendar_day,
)

from nature_calendar import (
    get_nature_info,
)

from memo_db import (
    create_table,
    get_memo,
    save_memo,
    delete_memo,
    has_memo,
)


# =========================================================
# 기본 설정
# =========================================================

st.set_page_config(
    page_title="날담",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed",
)

create_table()

today = datetime.now()


# =========================================================
# 태극기 이미지
# =========================================================

KOREA_FLAG_PATH = Path(
    "assets/korea_flag.jpg"
)


def get_flag_data_uri():

    if not KOREA_FLAG_PATH.exists():
        return ""

    with open(
        KOREA_FLAG_PATH,
        "rb"
    ) as image_file:

        encoded = base64.b64encode(
            image_file.read()
        ).decode()

    return (
        f"data:image/jpeg;base64,"
        f"{encoded}"
    )


KOREA_FLAG_DATA = (
    get_flag_data_uri()
)

def subject_particle(word):

    last_char = word[-1]

    if "가" <= last_char <= "힣":

        code = ord(last_char) - ord("가")

        jong = code % 28

        if jong == 0:
            return "가"
        else:
            return "이"

    return "이"


# =========================================================
# 날짜 클릭
# =========================================================

query_date = st.query_params.get(
    "date"
)

if query_date:

    try:

        clicked = datetime.strptime(
            query_date,
            "%Y-%m-%d",
        )

        st.session_state.selected_date = {
            "year": clicked.year,
            "month": clicked.month,
            "day": clicked.day,
        }

        st.session_state.year = (
            clicked.year
        )

        st.session_state.month = (
            clicked.month
        )

    except ValueError:
        pass


# =========================================================
# 현재 연 / 월
# =========================================================

if "year" not in st.session_state:
    st.session_state.year = (
        today.year
    )

if "month" not in st.session_state:
    st.session_state.month = (
        today.month
    )


# 모바일 월 이동 링크 처리
query_view = st.query_params.get("view")

if query_view:
    try:
        view_date = datetime.strptime(query_view, "%Y-%m")
        st.session_state.year = view_date.year
        st.session_state.month = view_date.month
    except ValueError:
        pass

year = st.session_state.year
month = st.session_state.month


# =========================================================
# 오늘 기본 정보
# =========================================================

today_lunar = solar_to_lunar(
    today.year,
    today.month,
    today.day,
)


today_sky = get_sky_info(
    today.year,
    today.month,
    today.day,
)


today_moon = (
    today_sky["moon"]
)

today_zodiac = (
    today_sky["zodiac"]
)


today_term_info = (
    get_solar_term_info(
        today.year,
        today.month,
        today.day,
    )
)


today_progress = (
    get_year_progress(
        today.year,
        today.month,
        today.day,
    )
)


# =========================================================
# CSS
# =========================================================

st.markdown(
    """
<style>

:root{
    --ink:#1e2530;
    --muted:#7a7f89;
    --line:#e7e8eb;

    --gold:#d9931f;
    --red:#c83b3b;
    --blue:#304fc8;

    --sky:#526d94;
    --green:#688651;
}


/* 전체 */

html,
body,
[data-testid="stAppViewContainer"]{
    background:#ffffff;
}


.block-container{
    max-width:1220px;

    margin:0 auto;

    padding-top:1.35rem;
    padding-bottom:3.5rem;

    padding-left:1.2rem;
    padding-right:1.2rem;
}


[data-testid="stHorizontalBlock"]{
    gap:12px;
}


[data-testid="column"]{
    min-width:0 !important;
}


/* 브랜드 */

.brand{
    display:flex;
    align-items:center;
    gap:10px;
    margin-bottom:2px;
    padding-top:12px;
    padding-bottom:4px;
    overflow:visible;
}

.brand-mark{
    font-size:34px;
    line-height:1.25;
    display:flex;
    align-items:center;
    overflow:visible;
}

.brand-title{
    font-size:40px;
    font-weight:900;
    letter-spacing:-2.5px;
    color:var(--ink);
    line-height:1.5;
    padding-top:6px;
    padding-bottom:6px;
    overflow:visible;
}


.brand-sub{
    font-size:15px;

    color:var(--muted);

    margin:
        5px 0 16px 0;
}


/* 오늘의 한 장 */

.hero{
    border:
        1px solid #efd4aa;

    border-radius:18px;

    background:
        linear-gradient(
            135deg,
            #fffdf9 0%,
            #fff7ea 100%
        );

    padding:
        24px 28px;

    box-shadow:
        0 5px 16px
        rgba(95,70,35,.06);

    display:grid;

    grid-template-columns:
        1fr 250px;

    gap:24px;

    align-items:center;

    margin-bottom:20px;
}


.hero-kicker{
    color:#a85713;

    font-weight:850;

    font-size:15px;

    margin-bottom:6px;
}


.hero-date{
    font-size:36px;

    font-weight:900;

    letter-spacing:-1.7px;

    color:var(--ink);

    margin-bottom:4px;
}


.hero-lunar{
    color:#6f747c;

    font-size:14px;

    margin-bottom:10px;
}


.hero-info{
    display:flex;

    flex-wrap:wrap;

    gap:7px;

    margin-bottom:14px;
}


.hero-chip{
    display:inline-block;

    background:
        rgba(
            255,
            255,
            255,
            .7
        );

    border:
        1px solid #ead9bd;

    border-radius:9px;

    padding:
        6px 9px;

    font-size:12px;

    color:#685b49;
}


.hero-story{
    font-size:15px;

    color:#31353b;

    line-height:1.8;
}


.hero-quote{
    margin-top:16px;

    border-top:
        1px dashed #e5c18e;

    padding-top:14px;

    color:#a15d20;

    font-size:16px;

    text-align:center;
}


.hero-sky{
    text-align:center;

    padding:
        15px 10px;

    border-radius:16px;

    background:
        rgba(
            255,
            255,
            255,
            .54
        );
}


.hero-moon{
    font-size:82px;

    line-height:1.1;

    margin-bottom:5px;
}


.hero-moon-name{
    font-size:15px;

    font-weight:850;

    color:#48576e;
}


.hero-zodiac{
    margin-top:7px;

    font-size:13px;

    color:#737b88;
}


/* 버튼 */

.stButton > button{
    border-radius:11px;

    border:
        1px solid #d9dadd;

    background:#ffffff;

    min-height:44px;

    font-size:16px;
}


.stButton > button:hover{
    border-color:#c7a66e;

    color:#9b5d13;
}


/* 월 제목 */

.month-title{
    text-align:center;

    font-size:30px;

    font-weight:900;

    letter-spacing:-1.2px;

    color:var(--ink);

    margin:
        15px 0 7px;
}


.legend{
    text-align:center;

    font-size:12px;

    color:#747a83;

    line-height:1.8;

    margin-bottom:13px;
}


/* 요일 */

.week-title{
    text-align:center;

    font-size:13px;

    font-weight:800;

    color:#4d535b;

    padding:
        4px 0 7px;
}


.week-sat{
    color:#2458c7;
}


.week-sun{
    color:#d62929;
}


/* 달력 */

.calendar-card{
    height:90px;

    border:
        1px solid #e8e9ec;

    border-radius:11px;

    padding:
        9px 10px;

    background:#ffffff;

    display:flex;

    flex-direction:column;

    justify-content:
        space-between;

    box-sizing:
        border-box;

    text-decoration:
        none !important;

    color:
        var(--ink) !important;

    transition:
        .12s ease;
}


.calendar-card:hover{
    transform:
        translateY(-1px);

    border-color:#d4d7dc;

    box-shadow:
        0 4px 12px
        rgba(0,0,0,.05);
}


.calendar-card.today{
    border:
        1.5px solid
        #e3a12c;

    background:#fff9ed;
}


.calendar-card.selected{
    border-color:#efb0a6;

    background:#fff7f4;
}


.calendar-card.term-day{
    box-shadow:
        inset 0 3px 0
        #a5bb82;
}


.calendar-card.empty{
    border-color:
        transparent;

    background:
        transparent;

    box-shadow:none;
}


.day-top{
    display:flex;

    align-items:center;

    justify-content:
        space-between;
}


.day-number{
    font-size:18px;

    font-weight:850;
}


.day-number.sat{
    color:#2855c0;
}


.day-number.sun{
    color:#d62929;
}

.day-number.holiday {
    color: red !important;
    font-weight: 900 !important;
}

.holiday-name{
    margin-top:3px;
    font-size:10px;
    line-height:1.25;
    font-weight:800;
    color:#d62929;
    white-space:nowrap;
    overflow:hidden;
    text-overflow:ellipsis;
}

.public-holiday-badge{
    display:inline-flex;
    align-items:center;
    gap:6px;
    margin-top:8px;
    margin-right:6px;
    padding:6px 10px;
    border-radius:999px;
    background:#fff0f0;
    border:1px solid #ffd1d1;
    color:#c92525;
    font-size:13px;
    font-weight:850;
}


.day-icons{
    display:flex;

    align-items:center;

    gap:3px;

    font-size:12px;

    white-space:nowrap;
}


.korea-flag{
    width:18px;

    height:12px;

    object-fit:cover;

    border-radius:2px;
}


.calendar-moon{
    font-size:18px;

    line-height:1;

    margin-top:1px;
}


.lunar{
    font-size:10px;

    color:#777d86;
}


/* 상세 날짜 */

.detail-shell{
    border:
        1px solid var(--line);

    border-radius:18px;

    padding:22px 24px;

    margin-top:26px;

    background:#ffffff;
}


.detail-head{
    display:flex;

    align-items:flex-start;

    justify-content:
        space-between;

    gap:12px;

    margin-bottom:12px;
}


.detail-date{
    font-size:34px;

    font-weight:900;

    letter-spacing:-1.4px;

    color:var(--ink);
}


.detail-sub{
    font-size:14px;

    color:var(--muted);

    margin-top:2px;
}


.good-badge{
    display:inline-block;

    background:#fff6e9;

    border:
        1px solid #f1dfbf;

    color:#a86219;

    border-radius:10px;

    padding:
        10px 14px;

    font-size:13px;

    font-weight:700;
}


/* 날짜 의미 카드 */

.day-meaning{
    border:
        1px solid #e0e8d9;

    background:
        linear-gradient(
            135deg,
            #fbfdf8,
            #f5faef
        );

    border-radius:14px;

    padding:
        14px 16px;

    margin-bottom:15px;

    display:flex;

    flex-wrap:wrap;

    gap:10px;
}


.meaning-item{
    background:#ffffff;

    border:
        1px solid #e5eadf;

    border-radius:10px;

    padding:
        8px 11px;

    font-size:13px;

    color:#526046;
}


/* 스토리 카드 */

.story-card{
    border-radius:16px;

    padding:
        18px 18px 16px;

    min-height:270px;

    box-sizing:border-box;
}


.story-card.korea{
    border:
        1px solid #f0cccc;

    background:
        linear-gradient(
            145deg,
            #fffafa,
            #fff5f4
        );
}


.story-card.world{
    border:
        1px solid #d9ddf4;

    background:
        linear-gradient(
            145deg,
            #fbfbff,
            #f4f6ff
        );
}


.story-card.sky{
    border:
        1px solid #d9e2f0;

    background:
        linear-gradient(
            145deg,
            #fcfdff,
            #f1f6fd
        );
}


.card-title{
    font-size:17px;

    font-weight:850;

    margin-bottom:16px;
}


.card-title.korea{
    color:#bd2f2f;
}


.card-title.world{
    color:#3046b2;
}


.card-title.sky{
    color:#506e99;
}


.card-year{
    color:#666c74;

    font-size:12px;

    margin-bottom:4px;
}


.card-event{
    font-size:21px;

    font-weight:900;

    color:var(--ink);

    margin-bottom:6px;
}


.card-meta{
    color:#71767e;

    font-size:12px;

    margin-bottom:12px;
}


.card-desc{
    color:#373c43;

    font-size:14px;

    line-height:1.65;
}


.card-why{
    margin-top:14px;

    border-radius:11px;

    padding:
        11px 12px;

    background:
        rgba(
            255,
            255,
            255,
            .62
        );

    font-size:13px;

    color:#4b5056;
}


.empty-note{
    color:#858a92;

    font-size:14px;

    padding-top:34px;
}


/* 하늘 카드 */

.sky-moon-big{
    font-size:58px;

    line-height:1;

    margin-bottom:9px;
}


.sky-moon-name{
    font-size:21px;

    font-weight:900;

    color:#26354a;

    margin-bottom:7px;
}


.sky-stat{
    display:inline-block;

    padding:
        5px 9px;

    margin-right:4px;

    margin-bottom:8px;

    border-radius:8px;

    background:#ffffff;

    border:
        1px solid #dce5f0;

    font-size:12px;

    color:#556377;
}


.sky-divider{
    border-top:
        1px solid #dce5ef;

    margin:
        14px 0;
}


.zodiac-symbol{
    font-size:30px;

    margin-bottom:4px;
}


.zodiac-title{
    font-size:18px;

    font-weight:850;

    color:#415776;

    margin-bottom:4px;
}


.zodiac-star{
    font-size:13px;

    color:#6e7887;

    margin-bottom:9px;
}


.sky-box{
    margin-top:12px;

    padding:
        10px 11px;

    border-radius:10px;

    background:#ffffff;

    border:
        1px solid #dce5f0;

    font-size:12px;

    line-height:1.7;

    color:#526174;
}


.meteor-box{
    border:
        1px solid #d7e7ff;

    background:#f7fbff;

    border-radius:11px;

    padding:
        11px 12px;
}


.meteor-kicker{
    font-size:13px;

    font-weight:850;

    color:#4f6890;

    margin-bottom:4px;
}


.meteor-title{
    font-size:16px;

    font-weight:850;

    margin-bottom:5px;
}


/* 메모 */

.memo-head{
    font-size:18px;

    font-weight:850;

    color:#26314a;

    margin-top:18px;

    margin-bottom:8px;
}


/* 모바일 */

@media (max-width:800px){

    .block-container{
        padding-left:.7rem;
        padding-right:.7rem;
    }

    .hero{
        grid-template-columns:1fr;
        padding:20px;
    }

    .hero-sky{
        display:none;
    }

    .hero-date{
        font-size:28px;
    }

    .calendar-card{
        height:78px;
        padding:6px;
    }

    .day-number{
        font-size:16px;
    }

    .day-icons{
        font-size:10px;
        gap:2px;
    }

    .korea-flag{
        width:15px;
        height:10px;
    }

    .calendar-moon{
        font-size:15px;
    }

    .lunar{
        font-size:8px;
    }
}


a{
    text-decoration:none !important;
}

/* 달력 링크의 기본 파란색이 날짜 숫자를 덮지 않도록 차단 */
a:link,
a:visited,
a:hover,
a:active{
    text-decoration:none !important;
}

a .calendar-card{
    color:var(--ink) !important;
}

a .day-number{
    color:#1e2530 !important;
}

a .day-number.sat{
    color:#2855c0 !important;
}

a .day-number.sun,
a .day-number.holiday{
    color:#d62929 !important;
    font-weight:900 !important;
}

/* 클릭 링크는 카드 위에 투명 오버레이로만 둔다.
   날짜 텍스트를 <a> 안에 넣지 않아 링크 파란색 상속을 완전히 차단한다. */
.calendar-card{
    position:relative;
}

.calendar-card-link{
    position:absolute;
    inset:0;
    z-index:20;
    display:block;
    text-decoration:none !important;
    color:transparent !important;
    background:transparent !important;
    border-radius:11px;
}

.calendar-card .day-top,
.calendar-card .calendar-moon,
.calendar-card .lunar,
.calendar-card .holiday-name{
    position:relative;
    z-index:1;
    pointer-events:none;
}

/* 날짜 숫자 색상 - 카드 링크와 완전히 분리된 최종 규칙 */
.calendar-card .day-number.weekday-day{
    color:#1e2530 !important;
}

.calendar-card .day-number.saturday-day{
    color:#2855c0 !important;
}

.calendar-card .day-number.red-day{
    color:#d62929 !important;
}


/* =========================================================
   날담 v1.0 · 최종 화면 정리
   ========================================================= */
.hero{overflow:hidden;}
.hero-story{max-width:760px;}
.stButton > button{font-weight:700;box-shadow:none;}
.month-title{line-height:1.25;}
.legend{letter-spacing:-0.1px;}
.week-title{padding-top:6px;padding-bottom:8px;}
.calendar-card{box-shadow:0 1px 2px rgba(20,28,38,.015);}
.calendar-card.today{box-shadow:0 2px 8px rgba(217,147,31,.08);}
.calendar-card.selected{box-shadow:0 2px 8px rgba(200,59,59,.06);}
.day-top{min-height:22px;}
.day-icons{min-height:14px;}
.lunar{line-height:1.2;}
.detail-shell{box-shadow:0 4px 18px rgba(20,28,38,.035);}
.day-meaning{margin-top:2px;}
.story-card{box-shadow:0 2px 10px rgba(20,28,38,.025);}
.memo-head{padding-top:2px;}

/* 달력은 Streamlit columns 대신 순수 CSS 7열 그리드로 유지 */
.weekday-grid,
.calendar-grid{
    display:grid;
    grid-template-columns:repeat(7, minmax(0, 1fr));
    gap:12px;
}

.weekday-grid{
    margin-top:2px;
}

.st-key-month_nav [data-testid="stHorizontalBlock"]{
    flex-wrap:nowrap !important;
}

.st-key-month_nav [data-testid="column"]{
    width:33.333% !important;
    flex:1 1 0 !important;
    min-width:0 !important;
}

.mobile-month-nav{
    display:none;
}

@media (max-width:800px){
    /* 모바일에서는 좌우 스크롤을 완전히 막고 세로 스크롤만 사용 */
    html,
    body,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    .stMain,
    .block-container{
        width:100% !important;
        max-width:100vw !important;
        min-width:0 !important;
        box-sizing:border-box !important;
        overflow-x:hidden !important;
    }

    html, body{
        overscroll-behavior-x:none;
        touch-action:pan-y;
    }

    /* 설치형 화면에서 상단 Streamlit 툴바가 날담을 가리는 문제 방지 */
    [data-testid="stHeader"],
    header[data-testid="stHeader"]{
        display:none !important;
    }

    .block-container{
        padding-top:1.15rem !important;
        padding-bottom:2.5rem;
        padding-left:.7rem !important;
        padding-right:.7rem !important;
    }

    /* 일반 컬럼은 화면 폭을 넘기지 않게 한다 */
    [data-testid="stHorizontalBlock"]{
        max-width:100% !important;
        min-width:0 !important;
    }
    [data-testid="column"]{
        min-width:0 !important;
        max-width:100% !important;
    }

    /* 모바일 브랜드: 툴바 아래로 숨지 않고 온전히 표시 */
    .brand{
        min-height:50px;
        width:100%;
        max-width:100%;
        box-sizing:border-box;
        padding-top:7px;
        padding-bottom:5px;
        gap:8px;
        align-items:center;
        overflow:visible;
    }
    .brand-title{
        font-size:34px;
        letter-spacing:-2px;
        line-height:1.28;
        padding:2px 0 4px;
        white-space:nowrap;
        overflow:visible;
        font-family:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans KR",sans-serif;
    }
    .brand-mark{
        font-size:29px;
        line-height:1.15;
        flex:0 0 auto;
    }
    .brand-sub{font-size:13px;margin-bottom:13px;}

    .hero{margin-bottom:16px;}

    .hero,
    .detail-shell,
    .day-meaning,
    .story-card,
    .legend,
    .month-title{
        width:100%;
        max-width:100%;
        min-width:0;
        box-sizing:border-box;
        overflow-wrap:anywhere;
    }

    .legend{
        white-space:normal;
        overflow:hidden;
    }
    .month-title{font-size:26px;margin-top:12px;}
    .legend{font-size:10px;line-height:1.9;margin-bottom:9px;}

    /* 모바일 월 이동은 Streamlit 컬럼 대신 3등분 링크로 고정 */
    .st-key-month_nav{
        display:none !important;
    }
    .mobile-month-nav{
        display:grid !important;
        grid-template-columns:repeat(3, minmax(0, 1fr));
        gap:6px;
        width:100%;
        max-width:100%;
        margin:0 0 8px 0;
        box-sizing:border-box;
    }
    .mobile-month-nav a{
        display:flex;
        align-items:center;
        justify-content:center;
        min-width:0;
        min-height:40px;
        padding:7px 4px;
        border:1px solid #d9dadd;
        border-radius:10px;
        background:#ffffff;
        color:#30343a !important;
        font-size:14px;
        font-weight:700;
        line-height:1;
        text-decoration:none !important;
        box-sizing:border-box;
        touch-action:manipulation;
        -webkit-tap-highlight-color:transparent;
    }
    .mobile-month-nav a:active{
        background:#f7f4ee;
        border-color:#c7a66e;
    }

    /* 모바일 달력: 7열을 유지하면서 한 달을 한눈에 */
    .weekday-grid,
    .calendar-grid{
        width:100% !important;
        max-width:100% !important;
        min-width:0 !important;
        box-sizing:border-box;
        grid-template-columns:repeat(7, minmax(0, 1fr)) !important;
        gap:3px;
        overflow:hidden;
    }
    .week-title{
        font-size:12px;
        padding-top:4px;
        padding-bottom:6px;
    }
    .calendar-card{
        width:100% !important;
        max-width:100% !important;
        height:64px;
        min-width:0 !important;
        box-sizing:border-box;
        border-radius:8px;
        padding:4px;
        overflow:hidden;
    }
    .day-top{
        min-height:16px;
        gap:1px;
    }
    .day-number{
        font-size:14px;
        line-height:1;
    }
    .day-icons{
        min-height:10px;
        max-width:26px;
        overflow:hidden;
        font-size:8px;
        line-height:1;
        gap:1px;
        justify-content:flex-end;
    }
    .korea-flag{
        width:11px;
        height:7px;
    }
    .calendar-moon{
        font-size:13px;
        line-height:1;
        margin-top:0;
    }
    .lunar{
        font-size:7px;
        line-height:1;
        white-space:nowrap;
        overflow:hidden;
        text-overflow:clip;
    }
    .holiday-name{display:none;}

    .detail-shell{padding:18px 15px;border-radius:14px;}
    .detail-date{font-size:28px;}
    .day-meaning{gap:7px;padding:11px;}
    .meaning-item{font-size:12px;padding:7px 9px;}
}


</style>
""",
    unsafe_allow_html=True,
)


# =========================================================
# 브랜드
# =========================================================

st.markdown(
    (
        '<div class="brand">'
        '<div class="brand-mark">🌙</div>'
        '<div class="brand-title">날담</div>'
        '</div>'
    ),
    unsafe_allow_html=True,
)


st.markdown(
    (
        '<div class="brand-sub">'
        '오늘이라는 날에 담긴 이야기를 만나다'
        '</div>'
    ),
    unsafe_allow_html=True,
)


# =========================================================
# 오늘의 한 장
# =========================================================

today_korea = get_korea_history(
    today.month,
    today.day,
)


today_world = get_world_history(
    today.month,
    today.day,
)


today_anniversaries = get_anniversaries(
    today.year,
    today.month,
    today.day,
)


today_nature = get_nature_info(
    today.month,
    today.day,
)


preview = []


if today_korea:

    e = today_korea[0]

    preview.append(
        f"🇰🇷 {e['year']}년 · "
        f"{e['title']}"
    )


if today_world:

    e = today_world[0]

    preview.append(
        f"🌍 {e['year']}년 · "
        f"{e['title']}"
    )


if today_anniversaries:

    a = today_anniversaries[0]

    preview.append(
        f"🎗️ {a['name']}"
    )


if today_nature:

    preview.append(
        f"🌿 {today_nature['title']}"
    )


preview.append(
    f"{today_moon['icon']} "
    f"{today_moon['name']}"
)


# =========================================================
# 오늘 절기 문구
# =========================================================

today_term = (
    today_term_info["today"]
)

previous_term = (
    today_term_info["previous"]
)


if today_term:

    term_chip = (
        f'{today_term["emoji"]} '
        f'오늘은 {today_term["name"]}'
    )

else:

    days_passed = (
        previous_term["days_passed"]
    )

    if days_passed == 1:

        term_chip = (
            f'{previous_term["emoji"]} '
            f'{previous_term["name"]}{subject_particle(previous_term["name"])} '
            f'지난 지 1일'
        )

    else:

        term_chip = (
            f'{previous_term["emoji"]} '
            f'{previous_term["name"]}{subject_particle(previous_term["name"])} '
            f'지난 지 {days_passed}일'
        )


progress_chip = (
    f'⏳ 올해의 '
    f'{today_progress["day_number"]}번째 날 · '
    f'{today_progress["percentage"]:.1f}%'
)


today_zodiac_html = ""


if today_zodiac:

    today_zodiac_html = (
        f'{today_zodiac["symbol"]} '
        f'{today_zodiac["name"]}'
    )


hero_html = (
    '<div class="hero">'

    '<div>'

    '<div class="hero-kicker">'
    'TODAY · 오늘의 한 장'
    '</div>'

    f'<div class="hero-date">'
    f'{today.year}년 '
    f'{today.month}월 '
    f'{today.day}일'
    f'</div>'

    f'<div class="hero-lunar">'
    f'🌙 음력 '
    f'{today_lunar["month"]}월 '
    f'{today_lunar["day"]}일'
    f'</div>'

    '<div class="hero-info">'

    f'<div class="hero-chip">'
    f'{term_chip}'
    f'</div>'

    f'<div class="hero-chip">'
    f'{progress_chip}'
    f'</div>'

    '</div>'

    f'<div class="hero-story">'
    f'{"<br>".join(preview)}'
    f'</div>'

    '<div class="hero-quote">'
    '“우리가 살아가는 오늘도 '
    '언젠가는 역사가 됩니다.”'
    '</div>'

    '</div>'

    '<div class="hero-sky">'

    f'<div class="hero-moon">'
    f'{today_moon["icon"]}'
    f'</div>'

    f'<div class="hero-moon-name">'
    f'{today_moon["name"]}'
    f'</div>'

    f'<div class="hero-zodiac">'
    f'{today_zodiac_html}'
    f'</div>'

    '</div>'

    '</div>'
)


st.markdown(
    hero_html,
    unsafe_allow_html=True,
)


# =========================================================
# 월 이동
# =========================================================

with st.container(key="month_nav"):

    n1, n2, n3 = st.columns(3)

    with n1:

        if st.button(
            "‹ 이전",
            use_container_width=True,
        ):

            month -= 1

            if month == 0:

                month = 12
                year -= 1

            st.session_state.year = year
            st.session_state.month = month

            st.query_params.clear()

            st.rerun()

    with n2:

        if st.button(
            "오늘",
            use_container_width=True,
        ):

            st.session_state.year = (
                today.year
            )

            st.session_state.month = (
                today.month
            )

            st.session_state.selected_date = {
                "year": today.year,
                "month": today.month,
                "day": today.day,
            }

            st.query_params.clear()

            st.rerun()

    with n3:

        if st.button(
            "다음 ›",
            use_container_width=True,
        ):

            month += 1

            if month == 13:

                month = 1
                year += 1

            st.session_state.year = year
            st.session_state.month = month

            st.query_params.clear()

            st.rerun()


# 모바일 전용 월 이동 링크
prev_year = year
prev_month = month - 1
if prev_month == 0:
    prev_month = 12
    prev_year -= 1

next_year = year
next_month = month + 1
if next_month == 13:
    next_month = 1
    next_year += 1

mobile_nav_html = (
    '<div class="mobile-month-nav">'
    f'<a href="?view={prev_year:04d}-{prev_month:02d}" target="_self">‹ 이전</a>'
    f'<a href="?date={today.year:04d}-{today.month:02d}-{today.day:02d}" target="_self">오늘</a>'
    f'<a href="?view={next_year:04d}-{next_month:02d}" target="_self">다음 ›</a>'
    '</div>'
)

st.markdown(mobile_nav_html, unsafe_allow_html=True)


# =========================================================
# 월 제목
# =========================================================

st.markdown(
    (
        f'<div class="month-title">'
        f'{year}년 {month}월'
        f'</div>'
    ),
    unsafe_allow_html=True,
)


# =========================================================
# 범례
# =========================================================

if KOREA_FLAG_DATA:

    flag_legend = (
        f'<img '
        f'src="{KOREA_FLAG_DATA}" '
        f'style="'
        f'width:18px;'
        f'height:12px;'
        f'object-fit:cover;'
        f'border-radius:2px;'
        f'vertical-align:middle;">'
    )

else:

    flag_legend = "🇰🇷"


st.markdown(
    (
        '<div class="legend">'

        f'{flag_legend} 한국사'
        '&nbsp;&nbsp; '

        '🌍 세계사'
        '&nbsp;&nbsp; '

        '🌙 달'
        '&nbsp;&nbsp; '

        '🌿 24절기'
        '&nbsp;&nbsp; '

        '🎗️ 기념일'
        '&nbsp;&nbsp; '

        '🔴 공휴일'
        '&nbsp;&nbsp; '

        '🍃 자연의 달력'
        '&nbsp;&nbsp; '

        '⭐ 손 없는 날'
        '&nbsp;&nbsp; '

        '📝 메모'

        '</div>'
    ),
    unsafe_allow_html=True,
)


# =========================================================
# 요일
# =========================================================

weekdays = [
    "월",
    "화",
    "수",
    "목",
    "금",
    "토",
    "일",
]

weekday_html = []

for i, name in enumerate(weekdays):

    cls = ""

    if i == 5:
        cls = "week-sat"

    elif i == 6:
        cls = "week-sun"

    weekday_html.append(
        f'<div class="week-title {cls}">{name}</div>'
    )

st.markdown(
    '<div class="weekday-grid">'
    + "".join(weekday_html)
    + '</div>',
    unsafe_allow_html=True,
)


# =========================================================
# 달력
# =========================================================

cal = calendar.Calendar(
    firstweekday=0,
)

weeks = (
    cal.monthdayscalendar(
        year,
        month,
    )
)

selected_date = (
    st.session_state.get(
        "selected_date"
    )
)

calendar_cells = []

for week in weeks:

    for weekday_index, day in enumerate(week):

        if day == 0:

            calendar_cells.append(
                '<div class="calendar-card empty"></div>'
            )

            continue

        # 음력
        lunar = solar_to_lunar(
            year,
            month,
            day,
        )

        lunar_text = (
            f"음 "
            f"{lunar['month']}."
            f"{lunar['day']}"
        )

        if lunar["is_leap"]:
            lunar_text += " 윤"

        # 손 없는 날
        good_day = is_sonnal(
            lunar["day"]
        )

        # 오늘
        is_today = (
            year == today.year
            and month == today.month
            and day == today.day
        )

        # 역사
        korea = get_korea_history(
            month,
            day,
        )

        world = get_world_history(
            month,
            day,
        )

        # 하늘
        sky = get_sky_info(
            year,
            month,
            day,
        )

        moon = sky["moon"]

        # 절기
        solar_term = (
            get_solar_term_info(
                year,
                month,
                day,
            )["today"]
        )

        # 기념일
        anniversaries = get_anniversaries(
            year,
            month,
            day,
        )

        # 공휴일
        public_holiday = get_public_holiday_info(
            year,
            month,
            day,
        )

        # 메모
        date_key = (
            f"{year:04d}-"
            f"{month:02d}-"
            f"{day:02d}"
        )

        memo_exists = (
            has_memo(
                date_key
            )
        )

        # 아이콘
        icons = []

        if (
            korea
            and KOREA_FLAG_DATA
        ):
            icons.append(
                (
                    f'<img '
                    f'src="{KOREA_FLAG_DATA}" '
                    f'class="korea-flag">'
                )
            )

        if world:
            icons.append("🌍")

        if solar_term:
            icons.append("🌿")

        if anniversaries:
            icons.append("🎗️")

        if public_holiday:
            icons.append("🔴")

        if good_day:
            icons.append("⭐")

        if memo_exists:
            icons.append("📝")

        # 날짜 숫자 색상
        # 공휴일 정보가 있거나 일요일이면 빨강 / 토요일 파랑 / 평일 검정
        if public_holiday or weekday_index == 6:
            number_class = "red-day"
        elif weekday_index == 5:
            number_class = "saturday-day"
        else:
            number_class = "weekday-day"

        # 카드 클래스
        card_class = "calendar-card"

        if is_today:
            card_class += " today"

        if solar_term:
            card_class += " term-day"

        if selected_date:
            if (
                selected_date["year"] == year
                and selected_date["month"] == month
                and selected_date["day"] == day
            ):
                card_class += " selected"

        click_url = (
            f"?date="
            f"{year:04d}-"
            f"{month:02d}-"
            f"{day:02d}"
        )

        card_html = (
            f'<div class="{card_class}">'
            f'<a class="calendar-card-link" '
            f'href="{click_url}" target="_self" '
            f'aria-label="{year}년 {month}월 {day}일"></a>'
            '<div class="day-top">'
            f'<div class="day-number {number_class}">{day}</div>'
            f'<div class="day-icons">{"".join(icons)}</div>'
            '</div>'
            f'<div class="calendar-moon">{moon["icon"]}</div>'
            f'<div class="lunar">{lunar_text}</div>'
            f'{(
                "<div class=\"holiday-name\">"
                + public_holiday.get("emoji", "🔴")
                + " "
                + public_holiday.get("name", "")
                + "</div>"
            ) if public_holiday else ""}'
            '</div>'
        )

        calendar_cells.append(card_html)

st.markdown(
    '<div class="calendar-grid">'
    + "".join(calendar_cells)
    + '</div>',
    unsafe_allow_html=True,
)


# =========================================================
# 상세정보
# =========================================================

if "selected_date" in st.session_state:

    selected = (
        st.session_state.selected_date
    )


    sy = selected["year"]
    sm = selected["month"]
    sd = selected["day"]


    slunar = solar_to_lunar(
        sy,
        sm,
        sd,
    )


    selected_good_day = (
        is_sonnal(
            slunar["day"]
        )
    )


    korea_history = (
        get_korea_history(
            sm,
            sd,
        )
    )


    world_history = (
        get_world_history(
            sm,
            sd,
        )
    )


    selected_anniversaries = (
        get_anniversaries(
            sy,
            sm,
            sd,
        )
    )


    selected_public_holiday = (
        get_public_holiday_info(
            sy,
            sm,
            sd,
        )
    )


    selected_nature = (
        get_nature_info(
            sm,
            sd,
        )
    )


    selected_sky = (
        get_sky_info(
            sy,
            sm,
            sd,
        )
    )


    selected_moon = (
        selected_sky["moon"]
    )


    selected_illumination = (
        selected_sky[
            "illumination"
        ]
    )


    selected_zodiac = (
        selected_sky["zodiac"]
    )


    selected_term_info = (
        get_solar_term_info(
            sy,
            sm,
            sd,
        )
    )


    selected_progress = (
        get_year_progress(
            sy,
            sm,
            sd,
        )
    )


    # 손 없는 날 배지

    badge_parts = []

    if selected_public_holiday:

        badge_parts.append(
            '<div class="public-holiday-badge">'
            f'{selected_public_holiday.get("emoji", "🔴")} '
            f'{selected_public_holiday.get("name", "공휴일")} · 공휴일'
            '</div>'
        )

    if selected_good_day:

        badge_parts.append(
            '<div class="good-badge">'
            '⭐ 오늘은 손 없는 날입니다'
            '</div>'
        )

    badge = "".join(badge_parts)


    st.markdown(
        (
            '<div '
            'class="detail-shell">'

            '<div '
            'class="detail-head">'

            '<div>'

            f'<div '
            f'class="detail-date">'
            f'{sm}월 {sd}일'
            f'</div>'

            f'<div '
            f'class="detail-sub">'
            f'{sy}년 · '
            f'음력 '
            f'{slunar["month"]}월 '
            f'{slunar["day"]}일'
            f'</div>'

            '</div>'

            f'{badge}'

            '</div>'

            '</div>'
        ),
        unsafe_allow_html=True,
    )


    # =====================================================
    # 선택 날짜의 의미
    # =====================================================

    selected_today_term = (
        selected_term_info[
            "today"
        ]
    )


    selected_previous_term = (
        selected_term_info[
            "previous"
        ]
    )


    selected_next_term = (
        selected_term_info[
            "next"
        ]
    )


    if selected_today_term:

        term_text = (
            f'{selected_today_term["emoji"]} '
            f'오늘은 '
            f'{selected_today_term["name"]} · '
            f'{selected_today_term["description"]}'
        )

    else:

        term_text = (
            f'{selected_previous_term["emoji"]} '
            f'{selected_previous_term["name"]}{subject_particle(selected_previous_term["name"])} '
            f'지난 지 '
            f'{selected_previous_term["days_passed"]}일'
        )


    next_term_text = (
        f'다음 절기 '
        f'{selected_next_term["name"]}까지 '
        f'{selected_next_term["days_until"]}일'
    )


    progress_text = (
        f'⏳ {sy}년의 '
        f'{selected_progress["day_number"]}번째 날 · '
        f'{selected_progress["percentage"]:.1f}%'
    )


    st.markdown(
        (
            '<div class="day-meaning">'

            f'<div '
            f'class="meaning-item">'
            f'{term_text}'
            f'</div>'

            f'<div '
            f'class="meaning-item">'
            f'🌿 {next_term_text}'
            f'</div>'

            f'<div '
            f'class="meaning-item">'
            f'{progress_text}'
            f'</div>'

            '</div>'
        ),
        unsafe_allow_html=True,
    )


    # =====================================================
    # 기념일 + 자연의 달력
    # =====================================================

    extra1, extra2 = st.columns(2)


    with extra1:

        if selected_anniversaries:

            anniversary_blocks = []

            for item in selected_anniversaries:

                if item.get("category") == "national_holiday":
                    category_name = "국경일"
                elif item.get("category") == "public_holiday":
                    category_name = "공휴일"
                else:
                    category_name = "기념일"

                anniversary_blocks.append(
                    '<div style="margin-bottom:14px;">'
                    f'<div class="card-year">{category_name}</div>'
                    f'<div class="card-event">{item.get("emoji", "🎗️")} {item["name"]}</div>'
                    f'<div class="card-desc">{item.get("description", "")}</div>'
                    '</div>'
                )

            anniversary_html = (
                '<div class="story-card korea">'
                '<div class="card-title korea">🎗️ 오늘의 기념일</div>'
                f'{"".join(anniversary_blocks)}'
                '</div>'
            )

        else:

            anniversary_html = (
                '<div class="story-card korea">'
                '<div class="card-title korea">🎗️ 오늘의 기념일</div>'
                '<div class="empty-note">등록된 대한민국 기념일이 없습니다.</div>'
                '</div>'
            )

        st.markdown(
            anniversary_html,
            unsafe_allow_html=True,
        )


    with extra2:

        if selected_nature:

            flowers_text = " · ".join(selected_nature.get("flowers", []))
            fruits_text = " · ".join(selected_nature.get("fruits", []))
            fields_text = " · ".join(selected_nature.get("fields", []))
            animals_text = " · ".join(selected_nature.get("animals", []))

            nature_rows = []

            if flowers_text:
                nature_rows.append(f'<div class="card-desc">🌸 <b>꽃</b> — {flowers_text}</div>')

            if fruits_text:
                nature_rows.append(f'<div class="card-desc">🍎 <b>과일</b> — {fruits_text}</div>')

            if fields_text:
                nature_rows.append(f'<div class="card-desc">🌾 <b>들판</b> — {fields_text}</div>')

            if animals_text:
                nature_rows.append(f'<div class="card-desc">🦋 <b>자연</b> — {animals_text}</div>')

            nature_html = (
                '<div class="story-card sky">'
                '<div class="card-title sky">🍃 자연의 달력</div>'
                f'<div class="card-year">{selected_nature.get("season", "")}</div>'
                f'<div class="card-event">{selected_nature.get("title", "")}</div>'
                f'{"".join(nature_rows)}'
                f'<div class="card-why"><b>이 무렵의 풍경</b><br>{selected_nature.get("landscape", "")}</div>'
                '</div>'
            )

        else:

            nature_html = (
                '<div class="story-card sky">'
                '<div class="card-title sky">🍃 자연의 달력</div>'
                '<div class="empty-note">등록된 자연 이야기가 없습니다.</div>'
                '</div>'
            )

        st.markdown(
            nature_html,
            unsafe_allow_html=True,
        )


    # =====================================================
    # 3개 카드
    # =====================================================

    c1, c2, c3 = st.columns(3)


    # =====================================================
    # 한국사
    # =====================================================

    with c1:

        if korea_history:

            h = korea_history[0]


            imp = (
                "★"
                * h.get(
                    "importance",
                    1,
                )
            )


            why = h.get(
                "why",
                "",
            )


            why_html = ""


            if why:

                why_html = (
                    '<div '
                    'class="card-why">'
                    '<b>왜 기억할까?</b><br>'
                    f'{why}'
                    '</div>'
                )


            if KOREA_FLAG_DATA:

                title_icon = (
                    f'<img '
                    f'src="{KOREA_FLAG_DATA}" '
                    f'class="korea-flag" '
                    f'style="'
                    f'margin-right:6px;">'
                )

            else:

                title_icon = "🇰🇷 "


            html = (
                '<div '
                'class="story-card korea">'

                f'<div '
                f'class="card-title korea">'
                f'{title_icon}'
                f'한국의 역사'
                f'</div>'

                f'<div '
                f'class="card-year">'
                f'{h["year"]}년'
                f'</div>'

                f'<div '
                f'class="card-event">'
                f'{h["title"]}'
                f'</div>'

                f'<div '
                f'class="card-meta">'
                f'{imp}'
                f'</div>'

                f'<div '
                f'class="card-desc">'
                f'{h["description"]}'
                f'</div>'

                f'{why_html}'

                '</div>'
            )

        else:

            html = (
                '<div '
                'class="story-card korea">'

                '<div '
                'class="card-title korea">'
                '🇰🇷 한국의 역사'
                '</div>'

                '<div '
                'class="empty-note">'
                '등록된 핵심 한국사 기록이 없습니다.'
                '</div>'

                '</div>'
            )


        st.markdown(
            html,
            unsafe_allow_html=True,
        )


    # =====================================================
    # 세계사
    # =====================================================

    with c2:

        if world_history:

            h = world_history[0]


            imp = (
                "★"
                * h.get(
                    "importance",
                    1,
                )
            )


            why = h.get(
                "why",
                "",
            )


            why_html = ""


            if why:

                why_html = (
                    '<div '
                    'class="card-why">'
                    '<b>왜 기억할까?</b><br>'
                    f'{why}'
                    '</div>'
                )


            html = (
                '<div '
                'class="story-card world">'

                '<div '
                'class="card-title world">'
                '🌍 세계의 역사'
                '</div>'

                f'<div '
                f'class="card-year">'
                f'{h["year"]}년 · '
                f'{h.get("country","세계")}'
                f'</div>'

                f'<div '
                f'class="card-event">'
                f'{h["title"]}'
                f'</div>'

                f'<div '
                f'class="card-meta">'
                f'{imp}'
                f'</div>'

                f'<div '
                f'class="card-desc">'
                f'{h["description"]}'
                f'</div>'

                f'{why_html}'

                '</div>'
            )

        else:

            html = (
                '<div '
                'class="story-card world">'

                '<div '
                'class="card-title world">'
                '🌍 세계의 역사'
                '</div>'

                '<div '
                'class="empty-note">'
                '등록된 핵심 세계사 기록이 없습니다.'
                '</div>'

                '</div>'
            )


        st.markdown(
            html,
            unsafe_allow_html=True,
        )


    # =====================================================
    # 오늘의 하늘
    # =====================================================

    with c3:

        moon_age = (
            selected_moon["age"]
        )


        moon_description = (
            selected_moon[
                "description"
            ]
        )


        full_moon_days = (
            selected_sky.get(
                "full_moon_days",
                0.0,
            )
        )


        new_moon_days = (
            selected_sky.get(
                "new_moon_days",
                0.0,
            )
        )


        season_constellation = (
            selected_sky.get(
                "season_constellation"
            )
        )


        meteor_shower = (
            selected_sky.get(
                "meteor_shower"
            )
        )


        # 황도 12궁

        zodiac_html = ""


        if selected_zodiac:

            zodiac_html = (
                '<div '
                'class="sky-divider">'
                '</div>'

                '<div style="'
                'font-size:12px;'
                'color:#7c8798;'
                'margin-bottom:4px;">'
                '오늘의 황도 12궁'
                '</div>'

                f'<div '
                f'class="zodiac-symbol">'
                f'{selected_zodiac["symbol"]}'
                f'</div>'

                f'<div '
                f'class="zodiac-title">'
                f'{selected_zodiac["name"]} · '
                f'{selected_zodiac["english"]}'
                f'</div>'

                f'<div '
                f'class="zodiac-star">'
                f'✨ 대표 별 · '
                f'{selected_zodiac["bright_star"]}'
                f'</div>'

                f'<div '
                f'class="card-desc">'
                f'{selected_zodiac["description"]}'
                f'</div>'
            )


        # 계절 별자리

        season_html = ""


        if season_constellation:

            season_html = (
                '<div '
                'class="sky-divider">'
                '</div>'

                '<div style="'
                'font-size:12px;'
                'color:#7c8798;'
                'margin-bottom:5px;">'

                f'{season_constellation["season"]}'
                f'철 밤하늘'

                '</div>'

                '<div style="'
                'font-size:18px;'
                'font-weight:850;'
                'color:#415776;'
                'margin-bottom:4px;">'

                f'{season_constellation["symbol"]} '
                f'{season_constellation["name"]}'

                '</div>'

                f'<div '
                f'class="zodiac-star">'
                f'✨ 대표 별 · '
                f'{season_constellation["bright_star"]}'
                f'</div>'

                f'<div '
                f'class="card-desc">'
                f'{season_constellation["description"]}'
                f'</div>'
            )


        # 유성우

        meteor_html = ""


        if meteor_shower:

            if meteor_shower.get(
                "is_peak"
            ):

                meteor_title = (
                    f'🌠 '
                    f'{meteor_shower["name"]} '
                    f'극대'
                )

            else:

                meteor_title = (
                    f'🌠 '
                    f'{meteor_shower["name"]} '
                    f'활동 기간'
                )


            meteor_html = (
                '<div '
                'class="sky-divider">'
                '</div>'

                '<div '
                'class="meteor-box">'

                '<div '
                'class="meteor-kicker">'
                '오늘의 천문 이벤트'
                '</div>'

                f'<div '
                f'class="meteor-title">'
                f'{meteor_title}'
                f'</div>'

                f'<div '
                f'class="card-desc">'
                f'{meteor_shower["description"]}'
                f'</div>'

                '</div>'
            )


        # 보름 / 신월

        if full_moon_days < 0.5:

            full_moon_text = (
                "오늘은 보름달 무렵"
            )

        else:

            full_moon_text = (
                f"다음 보름달까지 "
                f"약 "
                f"{full_moon_days:.1f}일"
            )


        if new_moon_days < 0.5:

            new_moon_text = (
                "오늘은 신월 무렵"
            )

        else:

            new_moon_text = (
                f"다음 신월까지 "
                f"약 "
                f"{new_moon_days:.1f}일"
            )


        sky_html = (
            '<div '
            'class="story-card sky">'

            '<div '
            'class="card-title sky">'
            '🌙 오늘의 하늘'
            '</div>'

            f'<div '
            f'class="sky-moon-big">'
            f'{selected_moon["icon"]}'
            f'</div>'

            f'<div '
            f'class="sky-moon-name">'
            f'{selected_moon["name"]}'
            f'</div>'

            f'<span '
            f'class="sky-stat">'
            f'월령 '
            f'{moon_age:.1f}일'
            f'</span>'

            f'<span '
            f'class="sky-stat">'
            f'달 밝기 '
            f'{selected_illumination:.0f}%'
            f'</span>'

            '<div '
            'class="card-desc" '
            'style="margin-top:7px;">'

            f'{moon_description}'

            '</div>'

            '<div '
            'class="sky-box">'

            f'🌕 {full_moon_text}'
            f'<br>'

            f'🌑 {new_moon_text}'

            '</div>'

            f'{zodiac_html}'

            f'{season_html}'

            f'{meteor_html}'

            '</div>'
        )


        st.markdown(
            sky_html,
            unsafe_allow_html=True,
        )


    # =====================================================
    # 절기 상세 설명
    # 절기 당일에만 표시
    # =====================================================

    if selected_today_term:

        st.markdown(
            (
                '<div style="'
                'margin-top:16px;'
                'padding:16px 18px;'
                'border:1px solid #e1e9d8;'
                'border-radius:14px;'
                'background:#f9fcf6;">'

                f'<div style="'
                f'font-size:17px;'
                f'font-weight:850;'
                f'color:#587044;'
                f'margin-bottom:5px;">'

                f'{selected_today_term["emoji"]} '
                f'오늘은 '
                f'{selected_today_term["name"]}입니다'

                '</div>'

                f'<div style="'
                f'font-size:14px;'
                f'line-height:1.7;'
                f'color:#485342;">'

                f'{selected_today_term["story"]}'

                '</div>'

                '</div>'
            ),
            unsafe_allow_html=True,
        )


    # =====================================================
    # 메모
    # =====================================================

    st.markdown(
        (
            '<div '
            'class="memo-head">'
            '✎ 나의 기록'
            '</div>'
        ),
        unsafe_allow_html=True,
    )


    selected_date_key = (
        f"{sy:04d}-"
        f"{sm:02d}-"
        f"{sd:02d}"
    )


    saved_memo = get_memo(
        selected_date_key
    )


    memo = st.text_area(
        "메모",

        value=saved_memo,

        height=100,

        key=(
            f"memo_"
            f"{selected_date_key}"
        ),

        label_visibility="collapsed",

        placeholder=(
            "이 날 기억하고 싶은 일을 "
            "적어보세요..."
        ),
    )


    m1, m2 = st.columns(
        [4, 1]
    )


    with m1:

        if st.button(
            "💾 기록 저장",

            use_container_width=True,

            key=(
                f"save_"
                f"{selected_date_key}"
            ),
        ):

            save_memo(
                selected_date_key,
                memo,
            )

            st.success(
                "기록을 저장했습니다."
            )

            st.rerun()


    with m2:

        if st.button(
            "🗑️ 삭제",

            use_container_width=True,

            key=(
                f"delete_"
                f"{selected_date_key}"
            ),
        ):

            delete_memo(
                selected_date_key
            )

            st.rerun()