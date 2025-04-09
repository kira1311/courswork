import json
from datetime import datetime
from src.utils import parse_datetime, fetch_data_from_api, analyze_data, load_operations_data


def home_page_function(datetime_str: str) -> str:
    """Основная функция для страницы «Главная»"""
    try:
        dt = parse_datetime(datetime_str)

        api_data = fetch_data_from_api(dt)

        processed_data = analyze_data(api_data, dt)

        response = load_operations_data(datetime_str, api_data, processed_data)

        return json.dumps(response, ensure_ascii=False, indent=2)

    except Exception as e:
        error_response = {
            'status': 'error',
            'message': str(e),
            'timestamp': datetime.now().isoformat()
        }
        return json.dumps(error_response, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    test_datetime = "2025-04-09 14:30:00"
    result = home_page_function(test_datetime)
    print(result)
