from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended

from face.models import Face

class FaceHandler(BaseHandler):
    """
    Authenticated entrypoint
    """
    model = Face
    
    def read(self, request):
        
        pass
    
    def create(self, request):

        pass
 
