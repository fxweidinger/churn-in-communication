import pandas
import numpy as np

import plotly.express as px
import matplotlib.pyplot as plt

pandas.set_option('display.max_columns', None)
dataframe = pandas.read_csv("../churn-in-communication/telecom_churn.csv")


def data_dump(df, message):
    print(f'{message}:\n')
    print('Number of rows: ', df.shape[0])
    print("\nNumber of features:", df.shape[1])
    print("\nData Features:")
    print(df.columns.tolist())
    print("\nMissing values:", df.isnull().sum().values.sum())
    print("\nUnique values:")
    print(df.nunique())


data_dump(dataframe, "Ueberblick über Datensatz")

target = dataframe["Churn"].value_counts().to_frame()
target = target.reset_index()
target = target.rename(columns={'index': 'Category'})
figure = px.pie(target, values='Churn', names='Category', color_discrete_sequence=["blue", "red"],
                title='Distribution of Churn')

figure.show()


# target = dataframe["ContractRenewal"].value_counts().to_frame()
# print(target)
# target = target.reset_index()
# target = target.rename(columns={'index': 'Category'})
# figure = px.pie(target, values='ContractRenewal', names='Category', color_discrete_sequence=["blue", "red"],
#                 title='Distribution of ContactRenewal')
#
# figure.show()


def bar_graph(feature, df=dataframe):
    temp_df = df.groupby([feature, 'Churn']).size().reset_index()
    temp_df = temp_df.rename(columns={0: 'Count'})
    value_counts_df = df[feature].value_counts().to_frame().reset_index()
    categories = [cat[1][0] for cat in value_counts_df.iterrows()]
    num_list = [num[1][1] for num in value_counts_df.iterrows()]
    div_list = [element / sum(num_list) for element in num_list]
    percentage = [round(element * 100, 1) for element in div_list]

    def num_format(list_instance):
        formatted_str = ''
        for index, num in enumerate(list_instance):
            if index < len(list_instance) - 2:
                formatted_str = formatted_str + f'{num}%, '  # append to empty string(formatted_str)
            elif index == len(list_instance) - 2:
                formatted_str = formatted_str + f'{num}% & '
            else:
                formatted_str = formatted_str + f'{num}%'
        return formatted_str

    # Categorical section
    def str_format(list_instance):
        formatted_str = ''
        for index, cat in enumerate(list_instance):
            if index < len(list_instance) - 2:
                formatted_str = formatted_str + f'{cat}, '
            elif index == len(list_instance) - 2:
                formatted_str = formatted_str + f'{cat} & '
            else:
                formatted_str = formatted_str + f'{cat}'
        return formatted_str

    # Running the formatting functions
    num_str = num_format(percentage)
    cat_str = str_format(categories)

    # Setting graph framework
    fig = px.bar(temp_df, x=feature, y='Count', color='Churn', title=f'Churn rate by {feature}', barmode="group",
                 color_discrete_sequence=["green", "red"])
    fig.add_annotation(
        text=f'Value count of distribution of {cat_str} are<br>{num_str} percentage respectively.',
        align='left',
        showarrow=False,
        xref='paper',
        yref='paper',
        x=1.4,
        y=1.3,
        bordercolor='black',
        borderwidth=1)
    fig.update_layout(
        # margin space for the annotations on the right
        margin=dict(r=400),
    )
    return fig.show()


# dataframe.loc[dataframe.DataPlan == 0, 'DataPlan'] = "No"
# dataframe.loc[dataframe.DataPlan == 1, 'DataPlan'] = "Yes"

bar_graph('ContractRenewal')
