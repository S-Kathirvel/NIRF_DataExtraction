from api import extract
import pandas as pd
# from link_extractor import file_names
import os

source_folder = "Cropped_Images/2022-1/"
def parser(input_string):
    # Extract ParsedText
    start_marker = '"ParsedText":"'
    end_marker = 'ErrorMessage'

    start_index = input_string.find(start_marker) + len(start_marker)
    end_index = input_string.find(end_marker, start_index)
    parsed_text = input_string[start_index:end_index].replace('\\r\\n', ' ')
    return parsed_text

def extract_numbers(data):
    rm_words = "Total SS FSR FQE FRU PU QP IPR FPPP GPH GUE MS GPHD RD WD ESCS PCS PR SCORE".split()
    data.pop()
    for i in data:
        if i.upper() in rm_words:
            data.remove(i)
    data.pop(0)

    # print(data)
    values=[]
    for i in range(0,len(data)-1,2):
        values.append(data[i])
    return values

images = os.listdir(source_folder)

dataframe = []
image_id = []

for img in images:
    input_string= extract(source_folder+img)

    parsed_text = parser(input_string)

    data=parsed_text.split()

    result = extract_numbers(data)
    dataframe.append(result)
    image_id.append(img)

txt = "SS FSR FQE FRU PU QP IPR FPPP GPH GUE MS GPHD RD WD ESCS PCS PR"
columns = txt.split()
df = pd.DataFrame(dataframe, columns=columns)
df.insert(0,"Image ID",image_id)
df.to_csv('Datasets/TN_engg_2022_1.csv', index=False)
# print(result)