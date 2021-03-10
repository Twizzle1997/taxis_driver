import csv
from credentials import Credentials as cr
import os

class Splitter:

    def split_datas_keys(self, file, dirname):
        
        '''
        Break raw data into many files
        '''

        os.makedirs(cr.CURATED_PATH + dirname + os.sep, exist_ok=True)

        csv.field_size_limit(10000000)
        with open(file, encoding='utf-8') as file_stream:
            file_stream_reader = csv.DictReader(file_stream, delimiter=',')
            open_files_references = {}

            for row in file_stream_reader:
                # print(row)
                # print(len(open_files_references))
                name_of_file = row['key'][:4]
                # print(name_of_file)
                # Open a new file and write the header
                if name_of_file not in open_files_references:
                    output_file = open(cr.CURATED_PATH + dirname + os.sep + '{}.csv'.format(name_of_file), 'w', encoding='utf-8')
                    dictionary_writer = csv.DictWriter(output_file, fieldnames=file_stream_reader.fieldnames)
                    dictionary_writer.writeheader()
                    open_files_references[name_of_file] = output_file, dictionary_writer
                # Always write the row
                open_files_references[name_of_file][1].writerow(row)
            # Close all the files
            for output_file, _ in open_files_references.values():
                output_file.close()