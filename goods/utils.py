from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from goods.models import Products

def q_search(query):

    #Точное совпадение
    if query.isdigit() and len(query) <=5:
        return Products.objects.filter(id=int(query))
    
    vector = SearchVector('name', 'description')
    query=SearchQuery(query)

    return Products.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by('-rank')

    
    
    #Cовпадение по словам 
    # keywords = [word for word in query.split() if len(word)>2 ]

    # q_obj=Q()
    
    # for key in keywords:
    #     q_obj |= Q(description__icontains=key)
    #     q_obj |= Q(name__icontains=key)
    
    # return Products.objects.filter(q_obj)