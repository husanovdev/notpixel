from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    USE_REF: bool = True
    REF_ID: str = 'f810529190'
    GIVE_10_PERCENT_OF_REFERRALS_TO_CREATOR_OF_THE_SOFT: bool = False

    USE_RANDOM_DELAY_IN_RUN: bool = True
    RANDOM_DELAY_IN_RUN: list[int] = [5, 60]

    SLEEP_TIME_IN_MINUTES: list[int] = [30, 60]

    ENABLE_AUTO_TASKS: bool = False
    ENABLE_AUTO_DRAW: bool = True
    ENABLE_JOIN_TG_CHANNELS: bool = False
    ENABLE_CLAIM_REWARD: bool = True
    ENABLE_AUTO_UPGRADE: bool = True

    DRAW_RANDOM_X_DIAPOSON: list[int] = [0, 900]
    DRAW_RANDOM_Y_DIAPOSON: list[int] = [0, 900]
    DRAW_RANDOM_COLORS: list[str] = ["#000000"]

    ENABLE_DRAW_ART: bool = False
    DRAW_ART_COORDS: list[dict] = [
        {
            'color': "#6A5CFF",
            'x': { 'type': 'diaposon', 'value': [995, 999] },
            'y': { 'type': 'random', 'value': [995, 999] }
        }
    ]

    ENABLE_SSL: bool = False

    BOOSTS_BLACK_LIST: list[str] = ['INVITE_FRIENDS', 'TON_TRANSACTION', 'BOOST_CHANNEL', 'ACTIVITY_CHALLENGE', 'CONNECT_WALLET']
    TASKS_TODO_LIST: list[str] = ["x:notcoin", "x:notpixel", "paint20pixels", "leagueBonusSilver", "invite3frens", "leagueBonusGold", "channel:notpixel_channel", "channel:notcoin", "premium"]

    USE_PROXY_FROM_FILE: bool = True


settings = Settings()


