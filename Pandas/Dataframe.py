import pandas as pd

data={"shapes":["triangle","circle","arrow"],
      "images":["📐","⭕","➡️"]}

pr=pd.DataFrame(data)
print(pr)