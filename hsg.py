dbt=float(input('Mời bạn nhập điểm trung bình:'))
if dbt >=9.0:
    print('Loại xuất sắc')
elif dbt>=8.0 and dbt<9.0:
    print('Loại giỏi')
elif dbt>=6.5 and dbt<8.0:
    print('Loại khá')
elif dbt>=5.0 and  dbt<6.5:
    print('Loại yếu')
else:
    print('Loại yếu')