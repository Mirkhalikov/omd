<h4>Для запуска каждого теста необоходимо находиться в папке репозитория, не в папке /tests</h4>
<h2>Issue 1</h2>
<p>Шаг 1: иcполнить код $ python -m doctest -o NORMALIZE_WHITESPACE -v tests/test_issue1.py </p> 
<h2>Issue 2</h2>
<p>Шаг 1: иcполнить код $ python -m pytest tests/test_issue2.py </p> 
<h2>Issue 3</h2>
<p>Шаг 1: иcполнить код $ python -m unittest -v tests/test_issue3.py </p> 
<h2>Issue 4</h2>
<p>Шаг 1: иcполнить код $  python -m pytest -v tests/test_issue4.py </p> 
<h2>Issue 5</h2>
<p>Шаг 1: иcполнить код $ python -m pytest -v tests/test_issue5.py </p> 
<p>Шаг 2: Для просмотра coverage для Issuе5 воспользоваться командой $ python -m pytest -q tests/test_issue5.py --cov=what_is_year_now.py </p> 
<p>Шаг 3: Можно посмотреть существующий html-отчет по сoverage в папке htmlcov, там выбрать либо файл index для отчета по всем файлам, либо файл what_is_year_now.  Для создания html-отчета исполнить команду $ python -m pytest --cov . --cov-report html </p> 