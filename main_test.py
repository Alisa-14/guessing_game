import pytest
import datetime

from main import check_num
from main import num_log_add



def test_check_num(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: '1')
    assert check_num("Текст") == 1



def test_num_log_add():
    num_log_record = []
    num2 = 10
    text = "Some information"
    num_log_add(num2, text, num_log_record,5)
    now = datetime.datetime.now()
    expected_log_record = [f'[{now}] [User] [Попытка "6"] : Введено число - {num2}',
        f'[{now}] [System] [INFO] : {text}']
    assert num_log_record == expected_log_record


if __name__ == '__main__':
    pytest.main(['-vv'])