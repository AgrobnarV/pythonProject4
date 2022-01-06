import json
import pytest
import requests


class TestUserAgentHeader:
    headers = {
        (
            "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
            "Mobile", "No", "Android"
        ),
        (
            "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
            "Mobile", "Chrome", "iOS"
        ),
        (
            "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", "Googlebot", "Unknown", "Unknown"
        ),
        (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
            "Web", "Chrome", "No"
        ),
        (
            "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
            "Mobile", "No", "iPhone"
        ),
        (
            "Unknown", "Unknown", "Unknown", "Unknown"
        )
    }

    @pytest.mark.parametrize("agent, platform, browser, device", headers)
    def test_check_correct_header(self, agent, platform, browser, device):
        data = {"User_agent": agent}
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers=data)
        assert response.status_code == 200, f"Неверный статус код"

        # распарсили ответ в json
        obj = json.loads(response.text)

        actual_platform = obj.get("platform")
        actual_browser = obj.get("browser")
        actual_device = obj.get("device")

        assert actual_platform == platform, f"Платформа {platform} в заголовках ответа не соответстует нужной для агента {agent}"
        assert actual_browser == browser, f"Браузер {browser} в заголовках ответа не соответстует нужному для агента {agent}"
        assert actual_device == device, f"Девайс {device} в заголовках ответа не соответстует нужному для агента {agent}"
