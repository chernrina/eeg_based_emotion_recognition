
## Используемые библиотеки

Для основной работы используется **Python 3.7**.
Основные используемые библиотеки: pandas, numpy, scikit-learn, scipy, pytorch.

Установка:
`pip install requirements.txt`

> (!) Для извлечения данных из датасета DEAP используется **Python 2.7** (+ pandas, numpy). 

## Извлечение данных DEAP
Исходные данные DEAP: https://www.eecs.qmul.ac.uk/mmv/datasets/deap/

В директории extact data/deap представлены файлы-пример для извлечения отдельных каналов-ЭЭГ и меток.

>Поместите исходные даныне в директорию **data_preprocessed_python** и выполните `python3 data_eeg_channel_extract.py` для получения файла `eeg_namechannel_all.csv` 

>Получить общий файл labels: `python3 labels_extract.py`

## Извлечение данных SEED
Исходные данные SEED: https://bcmi.sjtu.edu.cn/home/seed/seed.html

>Поместите исходные данные в директорию **Preprocessed_EEG**

## Экперимент Exploring Deep Learning Features

В директории Exploring Deep Learning Features представлен пример кода в формате jupyter notebook (`eeg_paper_f3_channel`) последовательное воспроизведение результататов исследования.

## Эксперимент по объединению симметричных каналов ЭЭГ

В директории **static signs** представлен пример кода в формате jupyter notebook (`static signs`, `static signs seed`) для воспроизведения результатов эксперимента со статическими и частотными признаками симметричных пар каналов ЭЭГ для двух датасетов.

Данный эксперимент заключался в извлечении статических признаков из пары симметричных каналов ЭЭГ. Взятие пары симметричных отведений обусловлено их местоположением и принадлежности к одной группе. Например, каналы fp1 и fp2 являются лобными полюсами и в совокупности дают общее представление об этой части головного мозга.

**Извлекались** следующие значения: среднее, максимальное, минимальное, среднеквадратическое отклонение, логарифм количества пересечений сигналом нулевого значения, мощность частотного спектра для пяти ритмов, максимальное и минимальное значение мощности частот в каждом ритме, среднеквадратическое отклонение мощности частот в каждом ритме, отношение мощностей частотного спектра каждого ритма друг к другу (отношение мощности alpha к мощности beta, затем к delta и так далее).

Таким образом, **для каждой пары отведений получалось 70 признаков** с 1280 экспериментами для датасета DEAP и 675 экспериментами для датасета SEED.

## Результаты эксперимента по объединению симметричные каналов ЭЭГ
На рисунке представлена таблица с результатами эксперимента.
![Image result](https://github.com/chernrina/eeg_based_emotion_recognition/raw/main/resources/result_2eeg.png)
Лучшие результаты значения точности классификаци:
- DEAP, valence 0.65
- DEAP, arousal 0.66
- SEED 0.69

## Эксперимент по группировке каналов ЭЭГ

В директории **eeg froup** представлен пример кода в формате jupyter notebook (`eeg group`, `eeg group seed`) для воспроизведения результатов эксперимента по поиску наиболее информативных каналов ээг для распознавания эмоций.

Эксперимент осуществлялся методом перебора датчиков, показывающих лучшие результаты. Сначала строились модели на каждом датчике отдельно, для 10 лучших выполнялся перебор: признаки выбранного датчика соединялись с признаками остальных по очереди, результаты сортировались и для лучших трех строились дальнейшие модели. Максимально датчики группировались по 7, так как вручную замечено, что далее точность переставала расти.

![Image result](https://github.com/chernrina/eeg_based_emotion_recognition/raw/main/resources/eeg_group.png)

## Результаты эксперимента по группировке каналов ЭЭГ
На рисунках представлены таблицы с результатами экспериментов для диторозависимых и дикторонезависимых моделей.

**Дикторозависимые модели**

![Image result](https://github.com/chernrina/eeg_based_emotion_recognition/raw/main/resources/results_dependent.png)
Лучшие результаты значения точности классификаци:
- DEAP, valence **0.72**
- DEAP, arousal **0.68**
- SEED **0.86**


**Дикторонезависимые модели**

![Image result](https://github.com/chernrina/eeg_based_emotion_recognition/raw/main/resources/results_independent.png) 

Лучшие результаты значения точности классификаци:
- DEAP, valence 0.67
- DEAP, arousal 0.62
- SEED 0.80

## Реальные данные, BIORadio

В процессе исследования проведен эксперимент по сбору данных ЭЭГ (каналов fp1 и fp2) при помощи оборудования BIORadio. За основу методики взят процесс сбора данных для создания датасета DEAP.

В директории **bioradio analysis** представлены исходные файлы для двух участников эксперимента в формате csv, а также исходный код для обработки полученных значений в формате jupyter notebook (`bioradio analysis`). Предобработка ЭЭГ-сигнала осуществлялась в соответствии с предобработкой сигналов датасета DEAP. 

Выполнены следующие действия по предобработке данных:
- сегментирование данных на эксперименты
- удаление аномальных значений
- удаление ЭОГ
- понижение частоты до 128 Гц
- применение полосового фильтра от 4 до 45 Гц

