blogs = dict()  # blog name : Blog object


def menu():
    # Show the user the availeble blogs
    # Let the user make a choice
    # Do something with that choice
    # Eventually exit
    print_blogs()


def print_blogs():
    for key, blog in blogs.items():
        print('-{}'.format(blog))
    