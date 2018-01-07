import os
from project.documents.document import Document
from configparser import ConfigParser, ExtendedInterpolation

config = ConfigParser(interpolation=ExtendedInterpolation())
config.read('../../config.ini')
IN_PROGRESS_PATH = config['DOCX']['IN_PROGRESS_PATH']
COMPLETED_PATH = config['DOCX']['COMPLETED_PATH']


def extract_document_text():
    for path in os.listdir(IN_PROGRESS_PATH):
        in_progress_doc_path = os.path.join(IN_PROGRESS_PATH, path)
        completed_doc_path = os.path.join(COMPLETED_PATH, path)

        # add logging

        # create document
        document = Document(in_progress_doc_path, completed_path=completed_doc_path)

        yield document

        # move document from in_progress dir to completed dir
        # after all file processing is complete
        os.rename(document.path, document.completed_path)

        # add logging


if __name__ == "__main__":
    for doc in extract_document_text():
        print(doc)
        print()