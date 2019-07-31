import os

DIRNAME = os.path.abspath(os.path.join(os.path.dirname(__file__), '../searchyption'))


class IOManager:

    @staticmethod
    def file_and_extension(file):
        filename, file_extension = os.path.splitext(file)
        return filename, file_extension

#     @staticmethod
#     def init_directories(folder_name):
#         try:
#             os.makedirs(folder_name)
#         except OSError as e:
#             if e.errno != errno.EEXIST:
#                 raise

    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as content_file:
            content = content_file.read()
        return content
