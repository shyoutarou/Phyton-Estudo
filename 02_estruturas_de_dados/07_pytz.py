from datetime import datetime
from pytz import timezone

# obter a data e hora em um timezone específico
d = datetime.fromtimestamp(1556322834.483199999, tz=timezone('America/Sao_Paulo'))
print(d)  # 2019-04-26 20:53:54.483200-03:00

# obter o timestamp a partir de uma data/hora e timezone
d = timezone('America/Sao_Paulo').localize(datetime(2019, 4, 26, 10, 30, 0, 0))
print(d.timestamp()) # 1556285400.0