import pandas as pd

# 요일별로 DataFrame 생성 및 엑셀로 저장
with pd.ExcelWriter('schedule.xlsx') as writer:
    for i, day_data in enumerate(data, start=1):
        df = pd.DataFrame(day_data, columns=['과목명', '강사명', '위치'])
        df.to_excel(writer, sheet_name=f'요일{i}', index=False)