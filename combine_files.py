#!/usr/bin/python

import pandas as pd
import argparse


def getArguments():
    """
    Run to get the command line arguments for th e
    input and the output file

    :return: Input File names as an array, Output file name
    :rtype: Array of Strings, Strings
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input_file", required=True, nargs='+',
                        help="csv input file (with extension)", type=str)
    parser.add_argument("-o", "--output_file", required=True,
                        help="csv output file (with extension)", type=str)

    args = parser.parse_args()
    input_files = args.input_file
    output_files = args.output_file

    return input_files, output_files


def concatCSV(input_file_names, output_file_name):
    """
    Function to concatenate the CSV Files, and saves them into a
    single CSV File

    :param input_file_names: Input File names as an array
    :type input_file_names: Array of Strings
    :param output_file_name: Output file name
    :type output_file_name: String
    :return: None
    :rtype: None
    """
    # Empty array to store the data frames

    all_df = []

    # Loop through the folder and get all the
    # dataframes and store them in an array

    for f in input_file_names:
        # Reads the CSV File

        df = pd.read_csv(f, sep=',')

        # Splits the name of the CSV File from the input string
        # to add as a column in the merged file

        file_name = f.split("fixtures/")
        df['filename'] = file_name[1]

        # Adds to the list of CSV Files

        all_df.append(df)

    # Concat the dataframes in the list

    merged_df = pd.concat(all_df, ignore_index=True, sort=False)

    # Save them to a merged.csv file

    merged_df.to_csv(output_file_name)


if __name__ == "__main__":
    inp, oup = getArguments()
    concatCSV(inp, oup)
