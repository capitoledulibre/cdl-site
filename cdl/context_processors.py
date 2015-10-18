from cdl.proposals.models import ProposalCategory


def categories(request):
    """Get all categories
    """

    categories = ProposalCategory.objects.all()

    return { "categories" : categories }
