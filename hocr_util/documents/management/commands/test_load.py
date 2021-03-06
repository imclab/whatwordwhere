
from django.core.management.base import BaseCommand, CommandError
from load_utils.load_document import enter_document
from datetime import datetime


class Command(BaseCommand):
    help = "test by loading a document"
    requires_model_validation = False

    def handle(self, *args, **options):
        

        this_file = "parser/test_hocr/58-1723645_990_201204.html"
        doc_id = "58-1723645_990_201204"
        start = datetime.now()
        enter_document(this_file, doc_id)
        end = datetime.now()
        elapsed = end-start
        print "Time elapsed: %s" % (elapsed)