from .models import Rating
import pandas as pd
import json
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from survey.models import Answer


def json_maker():
    rating = Rating.objects.all()
    json_data = []
    for rate in rating:
        data = {
            "id": rate.id,
            "salesperson": rate.salesperson.name,
            'region': rate.salesperson.region.name,
            "rating": rate.rating,
            "price": rate.price,
            "sent_time": rate.sent_time.strftime("%d/%m/%Y %H:%M:%S"),
        }
        json_data.append(data)
    return json.dumps(json_data, indent=4, sort_keys=True, default=str)


# def survey_json():
#     answer = Answer.objects.all()
#     json_data = []
#     for ans in answer:
#         data = {
#             "question": ans.question.text,
#             "body": ans.body,
#         }
#         json_data.append(data)
#     return json.dumps(json_data, indent=4, sort_keys=True, default=str)

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph
    

def get_plot():
    """Preparing data for plotting and making plots"""

    data = json_maker() # get data from function
    df = pd.read_json(data) # read json
    # Get rid of commas in prices and convert strings to integers
    for i in range(len(df['price'])):
        new_type = int(df['price'][i].replace(',', ''))
        df.loc[i, 'price'] = new_type

    region_group = df.groupby('region') # Grouping datas by region
    # Getting regions separately
    samarkand = region_group.get_group('Samarqand')
    fergana = region_group.get_group("Farg'ona")

    # Getting sales statistics of regions separately
    samarkand_sales = samarkand.groupby('salesperson')
    fergana_sales = fergana.groupby('salesperson')

    plt.style.use('seaborn')
    plt.switch_backend('AGG')

    # Needed datas of Samarkand for plots
    sam_averages = samarkand_sales['price'].mean().round(2).to_list()
    sam_labels = samarkand['salesperson'].unique()
    sam_counts = samarkand['salesperson'].value_counts(sort=False)
    sam_ratings = samarkand_sales['rating'].mean().round(2).to_list()

    # Needed datas of Fergana for plots
    fer_averages = fergana_sales['price'].mean().round(2).to_list()
    fer_labels = fergana['salesperson'].unique()
    fer_counts = fergana['salesperson'].value_counts(sort=False)
    fer_ratings = fergana_sales['rating'].mean().round(2).to_list()

    # PLOTS!
    fig, ax = plt.subplots(2, 3, figsize=(16, 8))

    ax[0, 0].bar(sam_labels, sam_averages, color='green')
    ax[1, 0].bar(fer_labels, fer_averages)
    ax[0, 1].bar(sam_labels, sam_counts, color='green')
    ax[1, 1].bar(fer_labels, fer_counts)
    ax[0, 2].bar(sam_labels, sam_ratings, color='green')
    ax[1, 2].bar(fer_labels, fer_ratings)

    ax[0, 0].set_title('Средний объем продаж продавцов [Самарканд]', pad=20, weight='bold')
    ax[0, 0].set_ylabel('Сумма', fontsize=16, weight='bold')
    ax[0, 0].set_xlabel('Имя продавца', fontsize=16, weight='bold')

    ax[0, 1].set_title('Общее количество оказанных услуг [Самарканд]', pad=20, weight='bold')
    ax[0, 1].set_ylabel('Количество (шт)', fontsize=16, weight='bold')
    ax[0, 1].set_xlabel('Имя продавца', fontsize=16, weight='bold')

    ax[0, 2].set_title('Средний рейтинг продавцов [Самарканд]', pad=20, weight='bold')
    ax[0, 2].set_ylabel('Рейтинг (5 баловый)', fontsize=16, weight='bold')
    ax[0, 2].set_xlabel('Имя продавца', fontsize=16, weight='bold')

    ax[1, 0].set_title('Средний объем продаж продавцов [Фергана]', pad=20, weight='bold')
    ax[1, 0].set_ylabel('Сумма', fontsize=16, weight='bold')
    ax[1, 0].set_xlabel('Имя продавца', fontsize=16, weight='bold')

    ax[1, 1].set_title('Общее количество оказанных услуг [Фергана]', pad=20, weight='bold')
    ax[1, 1].set_ylabel('Количество (шт)', fontsize=16, weight='bold')
    ax[1, 1].set_xlabel('Имя продавца', fontsize=16, weight='bold')

    ax[1, 2].set_title('Средний рейтинг продавцов [Фергана]', pad=20, weight='bold')
    ax[1, 2].set_ylabel('Рейтинг (5 баловый)', fontsize=16, weight='bold')
    ax[1, 2].set_xlabel('Имя продавца', fontsize=16, weight='bold')

    for i in range(len(sam_labels)):
        ax[0, 0].text(i, sam_averages[i], str(sam_averages[i]), ha="center", va="bottom", weight='bold', color='red')

    for i in range(len(fer_labels)):
        ax[1, 0].text(i, fer_averages[i], str(fer_averages[i]), ha="center", va="bottom", weight='bold', color='red')

    for i in range(len(sam_labels)):
        ax[0, 1].text(i, sam_counts[i], str(sam_counts[i]), ha="center", va="bottom", weight='bold', color='red')

    for i in range(len(fer_labels)):
        ax[1, 1].text(i, fer_counts[i], str(fer_counts[i]), ha="center", va="bottom", weight='bold', color='red')

    for i in range(len(sam_labels)):
        ax[0, 2].text(i, sam_ratings[i], str(sam_ratings[i]), ha="center", va="bottom", weight='bold', color='red')

    for i in range(len(fer_labels)):
        ax[1, 2].text(i, fer_ratings[i], str(fer_ratings[i]), ha="center", va="bottom", weight='bold', color='red')
    plt.tight_layout()
    graph = get_graph()
    return graph





