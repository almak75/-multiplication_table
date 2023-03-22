
#from base64 import b16decode
#from re import X
import streamlit as st
import random

import time
import pandas as pd


#st.set_page_config(page_title='Таблица умножения', page_icon='🖖')
st.set_page_config(page_title='Таблица умножения')
st.title('Таблица умножения')

##MainMenu {visibility: hidden;}
#footer {visibility: hidden;}
m = st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
    height: 48px;
    font-size: 32px;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#ff0000;
    height: 48px;
    font-size: 32px;
    }

</style>""", unsafe_allow_html=True)





def miltiplication(a,b):
    return f'{a} x {b}', a*b
def division(a,b):
    return f'{a*b} : {b}', a

def mistake_test():
   
    if not 'big_stat' in st.session_state:
        return
    df = st.session_state.big_stat
    mist = df['Ошибки'].to_list()
    mist = [tmp for tmp in mist if tmp]
    mist = ','.join(mist)
        
    mist = mist.split(',')
    ##бежим по ошибкам
    #print('mist', mist)
    new_zd = []
    for m in mist:
        if not m:
            continue
        if 'x' in m:
            func = miltiplication
        elif ':' in m:
            func = division
        m = m.replace('x','')
        m = m.replace(':','')
        m = m.replace('=','')
        
        m = m.strip()
        dig = m.split()
        #print('m',m)
        #print('dig', dig)
        if func == miltiplication:
            a = int(dig[0]) #берем первое число
            b = int(dig[1]) #берем второе число
        else: #ДЕЛЕНИЕ! беерем 2 и третье
            a = int(dig[1]) #берем второе число
            b = int(dig[0])//a #берем деление!!!!

        if mutirovat: #переставляем числа местами
            a,b = b,a 

        new_zd.append((a,b,func))
    if len(new_zd)==0:
        
        return
    random.shuffle(new_zd)  #всё перемешаем, чтоб 
    #print(new_zd)
    new_zd = list(set(new_zd))  #это чтобы убрать все дубли. Могли ошибаться на одном примере много раз, но пихать его много раз ненадо в тест
    st.session_state.zadacha = new_zd

    st.session_state.mist = new_zd
    #return

    s = time.ctime()
    start_time = s.split(' ')[3]
    start_time_cek =int(time.time())
    numbers=['тест по ошибкам']
    stat={'good':0, 'wrong':0, 'voprosov':len(new_zd), 'start_time':start_time,'start_time_cek':start_time_cek, 'mistakes':[], 'numbers':numbers, 'деление':'', 'умножение':'', 'wrong_answer':[]}
    st.session_state.stat = stat

    st.session_state.answer='' #тут хранится ответ на тест
    st.session_state.q = '' #тут хранится вопрос и ПРАВИЛЬНЫЙ ответ теста
    st.session_state.last=0
    


def start_test(*current_parameters):

    st.session_state.answer='' #тут хранится ответ на тест
    st.session_state.q = '' #тут хранится вопрос и ПРАВИЛЬНЫЙ ответ теста
    st.session_state.last=0
    #сохраняем параметры текущего теста
    st.session_state.param = current_parameters
        
        
    #генерируем тут сразу новое задание с нужным количеством примеров
    l = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
    numbers = [i+1 for i in range(len(l)) if l[i]]
    n = []
   

    start =[1,2][del1]
    finish=[11,10][del10]
    long = finish - start + 1
    for i in numbers:
        n.extend(list(zip(range(start,finish), [i]*long)))
    n=[(min(i), max(i)) for i in n]
    n = list(set(n))

    zd = n * (N//len(n))
    zd.extend(random.sample(n, N % len(n)))

    #генерируем операции
    oper = []
    if mult:
        oper.append(miltiplication)
    if div:
        oper.append(division)
    oper = oper * N
    oper = oper[:N]

    #соединяем цифры с операциями
    new_zd = []
    for i in range(N):
        tmp= list(zd[i])
        random.shuffle(tmp)
        tmp.append(oper[i])
        new_zd.append(tmp)

    random.shuffle(new_zd)
    st.session_state.zadacha = new_zd




    #ГОТОВИМ ДАННЫЕ В СТАТИСТИКУ
    s = time.ctime()
    start_time = s.split(' ')[3]
    start_time_cek =int(time.time())
    numbers=['x'+str(n) for n in numbers]
    stat={'good':0, 'wrong':0, 'voprosov':N, 'start_time':start_time,'start_time_cek':start_time_cek, 'mistakes':[], 'numbers':numbers, 'деление':div, 'умножение':mult, 'wrong_answer':[]}
    st.session_state.stat = stat

    #сюда будем складывать не правильно отвеченные примеры. Возможно, что их придется добавить в конце на штрафной круг
    st.session_state.crug=[]
    st.session_state.shot =''



with st.expander("НАСТРОЙКИ"):
    st.text('Важно: при изменении настроек теста, текущий тест будет прерван и начнется новый')

    st.write(':blue[Выберите на сколько будем умножать:]')

    col1, col2, col3, col4,col5 = st.columns(5)
    with col1:
        x1 = st.checkbox('x1', value=False)
        x6 = st.checkbox('x6', value=True)
    with col2:
        x2 = st.checkbox('x2', value=True)
        x7 = st.checkbox('x7', value=True)
    with col3:
        x3 = st.checkbox('x3', value=True)
        x8 = st.checkbox('x8', value=True)
    with col4:
        x4 = st.checkbox('x4', value=True)
        x9 = st.checkbox('x9', value=True)
    with col5:
         x5 = st.checkbox('x5', value=True)
         x10 = st.checkbox('x10', value=False)
    
         
    st.write(':blue[Выберите операцию:]')
    op1, op2 = st.columns(2)
    with op1:
         mult = st.checkbox('Умножение', value=True)
    with op2:
         div = st.checkbox('Деление', value=False)
    if not mult and not div:
        st.write(':red[необходимо выбрать хотя бы одну операцию умножение или деление]')
    
    N =st.slider(':blue[Количество примеров:]', 5, 100,10)
    
    inp = st.selectbox(':blue[Ввод ответа]', ('выбор из четырех предложенных','ввод числа'))
    
    st.write(':blue[Дополнительные параметры:]')
    del1 = st.checkbox('исключить умножение на 1 из х2....x10', value=True)
    del10 = st.checkbox('исключить умножение на 10 из х1....x9', value=True)
    shtraf = st.checkbox('дополнительно повторить ошибочные примеры в конце теста', value=False, disabled=False, help = 'Вопрос будет добавлен в конец теста и будет появляться пока не будет получен верный ответ')
    right_answer = st.checkbox('показать правильный ответ, если ошибка', value=True)




current_parameters = (x1,x2,x3,x4,x5,x6,x7,x8,x9,x10, mult, div, N, inp)
but = 0
if 'param' not in st.session_state or st.session_state.param !=current_parameters:
    but = 1



if but:
    #st.write('Текущие',current_parameters)
    #if 'param' in st.session_state:
    #    st.write('Прошлые', current_parameters.param)
    
    start = st.button('Новый тест', on_click=start_test, args=current_parameters, type='secondary')
    #if start:
    #    st.session_state.param = current_parameters
        
    #    st.experimental_rerun()
#у нас уже идет тест
#пока есть вопросы - мы их задаем
else:
    placeholder_big = st.empty()
    with placeholder_big.container():
        zd = st.session_state.zadacha
        if (len(zd)>0) or (shtraf and len(st.session_state.crug)>0):
            #st.title(zd)
            if len(zd)>0:
                vopros = list(st.session_state.zadacha[0])
                st.session_state.zadacha = st.session_state.zadacha[1:]
            else: #начинаем брать вопросы из штрафного круша
                vopros = list(st.session_state.crug[0])
                vopros=[vopros[1], vopros[0], vopros[2]]  #меняем местами цифры, чтобы жизнь легкой не казалась
                st.session_state.crug = st.session_state.crug[1:] #удаляем из очереди взятый пример
                st.session_state.stat["voprosov"] +=1
            
            st.session_state.current_example = vopros #возможно, что пример придется вернуть в очередб
       
        
           
            func = vopros[2] #получаем функцию
            a,b = vopros[0],vopros[1] #получаем 2 числа
            q,otv = func(a,b)  # q = это запись примера, otv - это ответ в примере
        
            def click_b(*answer):
                st.session_state.shot = st.session_state.current_example
                st.session_state.answer=answer
                st.session_state.q = answer[:2]
                if inp!='ввод числа':
                    st.session_state.last=1


        
            answer=-1
            if inp=='ввод числа': 
                with st.form(key='qwe', clear_on_submit=True):
                    st.title(q)
                    answer = st.number_input('Введите ответ',step=1, format='%i') #%d %e %f %g %i %u

                    s_b = st.form_submit_button("Готово", on_click=click_b, args=(q,otv, answer))
                
                    if s_b:
                        #click_b(st.session_state.q,answer)
                        tmp=list(st.session_state.q)
                        tmp.append(answer)
                        st.session_state.answer=tuple(tmp)
                        #st.write('ответ принят1', answer)
                        #st.session_state.answer=answer

            else: #кнопки
                 candidat = [otv-1,otv-2, otv-3,otv+1,otv+2, otv+3]
                 candidat = random.sample(candidat, 3)
                 candidat.append(otv)
                 random.shuffle(candidat)
                 st.session_state.last=0
                
                 with st.form(key='qwe2'):
                    st.title(q)
                    st.write('Нажмите кнопку с ответом')
                    column1, column2, column3, column4 = st.columns(4)
                    with column1:  
                        otv0 = st.form_submit_button(use_container_width=True, label = str(candidat[0]), on_click=click_b, args=(q, otv, candidat[0]))
                    with column2:  
                        otv1 = st.form_submit_button(use_container_width=True, label = str(candidat[1]), on_click=click_b, args=(q, otv, candidat[1]))
                    with column3:  
                        otv2 = st.form_submit_button(use_container_width=True, label = str(candidat[2]), on_click=click_b, args=(q, otv, candidat[2]))
                    with column4:  
                        otv3 = st.form_submit_button(use_container_width=True, label = str(candidat[3]), on_click=click_b, args=(q, otv, candidat[3]))
        else:#вопросы закончились, подводим итоги
           
            
            
            #st.title('Всего примеров: '+str(st.session_state.stat['voprosov']))
            st.title(f':green[Правильных ответов: {st.session_state.stat["voprosov"] - st.session_state.stat["wrong"]}]')
            st.title(f':red[Ошибочных ответов: {st.session_state.stat["wrong"]}]')
            t = end_time_cek =int(time.time()) - int(st.session_state.stat['start_time_cek'])
            #st.title('Время прохождения: '+str( f'{t//60} м. {t%60} сек.'))
            if st.session_state.stat['wrong'] !=0:
                st.title(':blue[Запомни эти примеры:]')
                tmp = set(st.session_state.stat['mistakes']) #так как может быть штрафной круг, то надо убрать дубли
                for m in tmp:
                    st.title(f'   {m}')
            
            start = st.button('Новый тест', on_click=start_test, args=current_parameters)
            tmp_dict=st.session_state.stat
            zad=' '.join(tmp_dict['numbers'])
            wrong_answer = ', '.join(tmp_dict['wrong_answer'])
            for_big_stat={'Начало':tmp_dict['start_time'], 'Длит.':f'{t//60} м. {t%60} сек.', 'Задание': zad, 'Вопросов':tmp_dict['voprosov'], 'Ошибок':tmp_dict['wrong'], 'Ошибки':wrong_answer}
            df_for_big_stat = pd.DataFrame(for_big_stat, index=[0])
            #st.dataframe(df_for_big_stat)
            #st.write(for_big_stat)
            #st.write(tmp_dict['numbers'])
            if 'big_stat' in st.session_state:
                st.session_state.big_stat = pd.concat([st.session_state.big_stat[st.session_state.big_stat['Начало'] !=tmp_dict['start_time']], df_for_big_stat])
            else:
                st.session_state.big_stat = df_for_big_stat

           
            #это жуткий костыль для того, чтобы узнать последнее введенное число
            #выводим форму, получаем ответ и тут же форму стираем...другого способа не нашлось...
            #=========================================================================================================================
            #=========================================================================================================================
            #=========================================================================================================================
            if inp=='ввод числа': 
                placeholder = st.empty()
                with placeholder.container():
                    with st.form(key='qwe', clear_on_submit=True):
                        answer = st.number_input('Введите ответ',step=1, format='%i') #%d %e %f %g %i %u

                       
                        s_b = st.form_submit_button("Готово")
                
                        if s_b:
                            #click_b(st.session_state.q,answer)
                            tmp=list(st.session_state.q)
                            tmp.append(answer)
                            st.session_state.answer=tuple(tmp)
                            st.session_state.last=1
                placeholder.empty()
            #=========================================================================================================================
            #=========================================================================================================================
            #=========================================================================================================================
def next_example():
    
    #возвращаем текущий пример в очередь. НЕ НЕПРАВИЛЬНЫЙ, А ТЕКУЩИЙ, КОТОРЫЙ УЖЕ ВЫВЕДЕН НА ЭКРАН
    
    all_example = st.session_state.zadacha
    #if len(all_example)>0: #возвращаем только если не один
    zd = st.session_state.current_example
    all_example.append(zd)
    st.session_state.zadacha = all_example

#ВЫВОДИМ ИНФОРМАЦИЮ ОБ ОШИБОЧНОМ ОТВЕТЕ....УДАЛЯЯ ТЕКУШИЙ ПРИМЕР и ВОЗВРАЩАЯ ЕГО В ОЧЕРЕДЬ 
if 'answer' in st.session_state:
    last_example = st.session_state.answer
    if type(last_example) is tuple:
        #st.write(last_example, len(last_example), type(last_example))
        if last_example[-1] != last_example[-2]: #если ответы не сходятся
            st.session_state.stat['wrong'] +=1 #считаем ошибку
            st.session_state.stat['mistakes'].append(f'{last_example[0]} = {last_example[-2]}')
            st.session_state.stat['wrong_answer'].append(f'{last_example[0]} = {last_example[-1]}')

            
            st.session_state.crug.append(st.session_state.shot)


            if right_answer: #надо сообщить верный ответ
                placeholder_big.empty()
                if st.session_state.last !=1:
                    next_example()
                st.session_state.answer='' #тут хранится ответ на тест
                st.session_state.q = '' #тут хранится вопрос и ПРАВИЛЬНЫЙ ответ теста  
                st.title(f':red[Ответ неверный]')
                st.title(f'Запомни: {last_example[0]} = {last_example[-2]}')
                st.button('Дальше')
        else: #ответ верный, надо посчитать
            st.session_state.stat['good'] +=1

            
          

with st.expander("СТАТИСТИКА"):
    if 'big_stat' in st.session_state:
           st.write('Статистика тестов:')
           df = st.session_state.big_stat
           if df.shape[0]>0:
               st.dataframe(st.session_state.big_stat)
               c1, c2 = st.columns(2)
               with c1:
                   hard_test = st.button('Запуcтить тест по ошибкам', on_click =mistake_test, disabled=False)
               with c2:
                   mutirovat = st.checkbox('мутировать примеры', help='примеры будут изменены, например:\nвместо 3х5 будет 5х3, вместо 24:3 будет 24:8')
    else:
           st.write('Здесь будет статистика полностью пройденных тестов')
with st.expander("Инструкция для родителей"):
    st.write('Программа не претендует на красоту, анимацию, развлечение.')
    st.write('Возможности смотрите в видео ролике.')
    st.write('Вопросы, отзывы и пожелания отправляйте в telegram:  @makarov75')
    st.video('https://youtu.be/pt51aVIDpFA')
 
#if 'stat' in st.session_state:
#    st.write(st.session_state.stat)
##if 'mist' in st.session_state:
##    st.write(st.session_state.mist)
#if 'crug' in st.session_state:
#    st.write(st.session_state.crug)

#if 'shot' in st.session_state:
#    st.write(st.session_state.shot)