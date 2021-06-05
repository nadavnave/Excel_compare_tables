import pandas as pd
import argparse

telephone_col_name = "Tel"

parser = argparse.ArgumentParser(description='create excel of phone numbers from last year that were not called to this year')
parser.add_argument('last_year_filename', type=str, help="The excel file name of phone numbers and names of from last year. Columns must contain {}".format(telephone_col_name))
parser.add_argument('cur_year_filename', type=str, help="The excel file name of phone numbers and names of from current year. Columns must contain {}".format(telephone_col_name))
parser.add_argument('result_filename', type=str, help="The excel filename of phone numbers and names output file")

args =parser.parse_args()
last_year_filename = args.last_year_filename
cur_year_filename = args.cur_year_filename
result_filename = args.result_filename

print( "*** Reading {} and {} excel files".format(last_year_filename, cur_year_filename))
last_year_df = pd.read_excel(last_year_filename)
cur_year_df  = pd.read_excel(cur_year_filename)
print("---- Last year excel ----")
print(last_year_df)

print("---- Current year excel ----")
print(cur_year_df)


last_year_tel_numbers = set(last_year_df[telephone_col_name].tolist())
cur_year_tel_numbers = cur_year_df[telephone_col_name].tolist()

result_df = pd.DataFrame()
print("*** Finding not duplicated numbers")
for number in last_year_tel_numbers:
    if number not in cur_year_tel_numbers:
        result_df = result_df.append(last_year_df[last_year_df[telephone_col_name]==number])

print("------ The result excel is -------")
print(result_df)
print("*** Writing result to {}".format(result_filename))
result_df.to_excel(result_filename, index=False)
