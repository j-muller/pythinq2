import logging

import requests

from pythinq2.utils import random_string
from pythinq2.constants import (
    GATEWAY_URL,
    API_KEY,
    SERVICE_CODE,
    API_CLIENT_ID,
)

LOGGER = logging.getLogger(__name__)


class Gateway:
    def __init__(self, country_code, language, load=True):
        """Create a new Gateway object."""
        self._session = requests.Session()
        self._session.headers = {
            "x-api-key": API_KEY,
            "x-thinq-app-ver": "3.6.1200",
            "x-thinq-app-type": "NUTS",
            "x-thinq-app-level": "PRD",
            "x-thinq-app-os": "ANDROID",
            "x-thinq-app-logintype": "LGE",
            "x-service-code": SERVICE_CODE,
            "x-country-code": country_code,
            "x-language-code": language,
            "x-service-phase": "OP",
            "x-origin": "app-native",
            "x-model-name": "samsung/SM-G930L",
            "x-os-version": "AOS/7.1.2",
            "x-app-version": "LG ThinQ/3.6.12110",
            "x-message-id": random_string(22),
            "user-agent": "okhttp/3.14.9",
            "x-client-id": API_CLIENT_ID,
        }

        self._data = None

        if load:
            self.load()

    @property
    def login_base_url(self):
        return self._data["empSpxUri"]

    @property
    def country_code(self):
        return self._data["countryCode"]

    @property
    def language_code(self):
        return self._data["languageCode"]

    @property
    def emp_base_url(self):
        return self._data["empTermsUri"]

    def load(self):
        """Load data from remote gateway."""
        LOGGER.debug("Loading data from gateway: %s", GATEWAY_URL)

        # response = self._session.get(GATEWAY_URL)
        # response.raise_for_status()
        # self._data = response.json()["result"]

        gateway = {
            "resultCode": "0000",
            "result": {
                "countryCode": "HK",
                "languageCode": "en-HK",
                "thinq1Uri": "https://kic.lgthinq.com:46030/api",
                "thinq2Uri": "https://kic-service.lgthinq.com:46030/v1",
                "empUri": "https://hk.m.lgaccount.com",
                "empSpxUri": "https://hk.m.lgaccount.com/spx",
                "rtiUri": "kic.lgthinq.com:47878",
                "mediaUri": "media.lgthinq.com:47800",
                "appLatestVer": "4.1.46041",
                "appUpdateYn": "N",
                "appLink": "market://details?id=com.lgeha.nuts",
                "nestSupportAppVer": "",
                "uuidLoginYn": "N",
                "lineLoginYn": "N",
                "lineChannelId": "",
                "cicTel": "852-3543-7777",
                "cicUri": "",
                "isSupportVideoYn": "N",
                "countryLangDescription": "Hong Kong/English",
                "empTermsUri": "https://hk.emp.lgsmartplatform.com",
                "googleAssistantUri": "https://assistant.google.com/services/invoke/uid/000000d26892b8a3",
                "smartWorldUri": "",
                "racUri": "hk.rac.lgeapi.com",
                "cssUri": "https://kic-common.lgthinq.com",
                "cssWebUri": "http://s3-an2-op-t20-css-web-resource.s3-website.ap-northeast-2.amazonaws.com",
                "iotssUri": "https://kic-iotservice.lgthinq.com",
                "chatBotUri": "",
                "autoOrderSetUri": "",
                "autoOrderManageUri": "",
                "aiShoppingUri": "",
                "onestopCall": "",
                "onestopEngineerUri": "",
                "hdssUri": "",
                "amazonDrsYn": "N",
                "features": {
                    "supportTvIoTServerYn": "Y",
                    "tvCastYn": "Y",
                    "nonProductThemes": "GIF,FOM",
                    "bleConfirmYn": "Y",
                    "nonWifiQrSupportYn": "Y",
                    "awhpWidgetYn": "N",
                    "qnaSatisYn": "Y",
                    "shortcutPromotionYn": "Y",
                    "searchYn": "Y",
                    "groupControlYn": "Y",
                    "thinqQuickguide": "N",
                    "supportQRPlaceGuideYn": "Y",
                    "multiProfile": "Y",
                    "eventAutoScrollYn": "Y",
                    "wifiInfoFeature": "Y",
                    "supportBleYn": "Y",
                    "takeATourSupport": "Y",
                    "empFrontProfileYn": "Y",
                    "checkWhiteListYn": "N",
                    "disableWeatherCard": "N",
                    "thinqCss": "Y",
                    "tvRcmdContentYn": "Y",
                    "supportProductManualYn": "N",
                    "awhpWidgetFeatureYn": "Y",
                    "clientDbYn": "Y",
                    "tvFeatureYn": "Y",
                    "thinqNotice": "Y",
                    "dmpCollectingYn": "N",
                    "smartScanWineHelpYn": "Y",
                    "inAppReviewYn": "Y",
                    "cicSupport": "Y",
                    "qrRegisterYn": "Y",
                    "closeAppDelayTimeSec": "1",
                },
                "serviceCards": [],
                "uris": {
                    "ItssUri": "https://kic-it-service.lgthinq.com",
                    "serviceDownloadUri": "https://service-download.lgthinq.com",
                    "takeATourUri": "https://s3-an2-op-t20-css-contents.s3.ap-northeast-2.amazonaws.com/workexperience-new/ios/no-version/index.html",
                    "gscsUri": "https://gscs.lge.com",
                    "empFrontBaseUri2": "https://hk.lgemembers.com/lgacc/service/v1/",
                    "careSdsUri": "https://kic-hcss.lgthinq.com:47040",
                    "onboardUri": "https://thinq-onboard-dashboard.lgthinq.com",
                    "empFrontBaseUri": "",
                    "amazonDartUri": "https://shs.lgthinq.com",
                },
            },
        }
        self._data = gateway["result"]
