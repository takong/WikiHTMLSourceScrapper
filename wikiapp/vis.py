from pyramid.view import (view_config, view_defaults)
from pyramid.response import Response



@view_defaults(renderer='home.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request

    # First view, available at http://localhost:6543/ or http://0.0.0.0:6543
    @view_config(route_name='home', renderer='templates/mytemplate.pt')
    def home(self):
        return {'name': 'Home View'}

    # View available at  http://0.0.0.0:6543/wikitoc
    @view_config(route_name='ScrappedWikiPageTOC', renderer='templates/page2.pt')
    def wiki_toc(self):
        return {'name': 'Wiki TOC View'}
        
        
        


 

    
#@view_config(route_name='result_page', renderer='templates/mytemplate.pt')
#def wikipage_download(request):
#    url=request.params['wikiurl']
#    return Response(url)

