from homeassistant.const import Platform

DOMAIN = "kiturami"
TITLE = "귀뚜라미"
MODEL = "NCTR"

PLATFORMS: list[Platform] = [Platform.CLIMATE]

KITURAMI_API_URL = 'https://igis.krb.co.kr/api'

MAX_TEMP = 45
MIN_TEMP = 10

# 온돌(난방수온) 모드 설정 범위
MAX_TEMP_WATER = 85
MIN_TEMP_WATER = 45
