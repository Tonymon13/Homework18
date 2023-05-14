price_all = 0
2	while True:
3	    try:
4	        ticket_number = input('Сколько билетов вы хотите приобрести на мероприятие? ')
5	        ticket_number = int(ticket_number)
6	        if type(ticket_number) == int:
7	            break
8	    except ValueError:
9	        print('Введите целое число')
10	for i in range(ticket_number):
11	    i += 1
12	    while True:
13	        try:
14	            age_for_ticket = input(f'Для какого возраста билет №{i}? ')
15	            age_for_ticket = int(age_for_ticket)
16	            if age_for_ticket < 18:
17	                print('Билет бесплатный')
18	            elif 25 > age_for_ticket >= 18:
19	                price_all += 990
20	                print('Стоимость билета: 990 руб.')
21	            else:
22	                price_all += 1390
23	                print('Стоимость билета: 1390 руб.')
24	            if type(age_for_ticket) == int:
25	                break
26	        except ValueError:
27	            print('Введите целое число')
28	if ticket_number > 3:
29	    price_all = price_all - ((price_all / 100) * 10)
30	    print(f'Сумма к оплате {price_all} руб. с учетом 10%-ой скидки на полную стоимость заказа за регистрацию больше 3-х человек')
31	else:
32	    print(f'Сумма к оплате {price_all} руб.')