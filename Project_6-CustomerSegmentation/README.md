# Проект 4. Сегментирование клиентов

## Оглавление  
[1. Описание проекта](./README.md#Описание-проекта)  
[2. Какой кейс решаем?](./README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](./README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](./README.md#Этапы-работы-над-проектом)  
[5. Результаты](./README.md#Результаты)   

### 1. Описание проекта   

Сегментация клиентов онлайн-магазина подапков на основе их покупательской способности, частоты совершения заказов и срока давности последнего заказа.

Маркетинг — неотъемлемая часть любого бизнеса. Для повышения прибыли компании важно понимать своего клиента, его пожелания и предпочтения. С появлением электронной коммерции, или онлайн-продаж, стало намного проще собирать данные о клиентах, анализировать их, находить закономерности и реализовывать маркетинговые кампании.

Большинство интернет-магазинов используют инструменты веб-аналитики, чтобы отслеживать просмотры страниц, количество и поведение посетителей и коэффициент отказов. Но отчёта из Google Analytics или аналогичной системы может быть недостаточно для полного понимания того, как клиенты взаимодействуют с сайтом. Компаниям важно иметь возможность быстро и точно реагировать на перемены в поведении клиентов, создавая инструменты, которые обнаруживают эти изменения практически в режиме реального времени.

Машинное обучение помогает поисковой системе анализировать огромное количество данных о посетителях платформы, узнавать модели поведения профессиональных покупателей, определять категорию клиентов (например, лояльные/перспективные/новички/«спящие»/ушедшие) и выбирать правильную стратегию взаимодействия с ними.

Стоит также отметить, что компании, использующие машинное обучение на своих платформах электронной коммерции, могут постоянно повышать эффективность бизнес-процессов: настраивать товарную выборку персонально для каждого покупателя и предлагать выгодную цену в соответствии с бюджетом клиента и т. д. Эта задача относится к категории построения рекомендательных систем, 

:arrow_up: [к оглавлению](./README.md#Оглавление)

### 2. Какой кейс решаем?  

Кластерный анализ.

**Бизнес-задача:** произвести сегментацию существующих клиентов, проинтерпретировать эти сегменты и определить стратегию взаимодействия с ними.

**Техническая задача специалиста Data Science:**  построить модель кластеризации клиентов на основе их покупательской способности, частоты заказов и срока давности последней покупки, определить профиль каждого из кластеров (RFM-кластеризация).

:arrow_up: [к оглавлению](./README.md#Оглавление)

### 3. Краткая информация о данных
Как правило, наборы данных для электронной коммерции являются частной собственностью и, следовательно, их трудно найти среди общедоступных данных.

Однако в [UC Irvine Machine Learning Repository](http://archive.ics.uci.edu/ml/index.php) создали набор данных, содержащий фактические транзакции для базирующейся в Великобритании компании, занимающейся розничной онлайн-торговлей. Компания в основном продаёт уникальные подарки на все случаи жизни. Многие клиенты являются оптовиками.за 2010 и 2011 годы. [Датасет](https://drive.google.com/file/d/1Axlknf1Rd6T6UFRzWWZA_gBbfN2g9r3v/view?usp=sharing) содержит все транзакции, произошедшие за период с 01/12/2010 по 09/12/2011.

:arrow_up: [к оглавлению](./README.md#Оглавление)

### 4. Этапы работы над проектом  

1. Базовый анализ и знакомство с данными
2. Предобработка и очистка данных
3. Разведывательный анализ данных (EDA)
4. RFM-сегментация клиентов. Часть I. Традиционные методы.
5. RFM-сегментация клиентов. Часть II. Кластеризация с нелинейным преобразованием размерностей (t-SNE).
6. RFM-сегментация клиентов. Часть III. Модель классификации.

:arrow_up: [к оглавлению](./README.md#Оглавление)

### 5. Результаты  
* Проведена предобработка и очистка данных: удалены пропуски и дубликаты; идентифицированы и удалены транзакции-возвраты, количество возвращенного товара по заказам выделено в отдельный признак; идентифицированы и удалены транзакции специального характера, не представляющие интереса для кластерного анализа клиентов.
* Рассмотрены распределения клиентов, количества заказов и выручки по странам. Проанализировано количество продаж по месяцам, дням недели, времени суток.
* Сформирован датасет для анализа клиентов по модели RFM: Recency-Frequency-Monetary Value. Проведено PCA-снижение размерности до двух компонент, проведена кластеризация несколькими методами, выбран оптимальный алгоритм. Проведен анализ отличий в разных кластерах.
* Аналогичные шаги кластеризации повторены для нелинейного снижения размерности методом t-SNE.
* Построены модели классификации клиентов.

:arrow_up: [к оглавлению](./README.md#Оглавление)
