MENU_PROMPT = "\nEnter 'a' to add movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
    # You may want to create a function for this code
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def show_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release Year: {movie['year']}")


def find_movies():
    search_tile = input("Enter movie title you're looking for: ")
    for movie in movies:
        if movie["title"] == search_tile:
            print_movie(movie)


# Create other functions for:
# - Listing movies
# - finding movies

# First class functions
user_options = {
    "a": add_movie(),
    "l": show_movies(),
    "f": find_movies()
}


def menu():
    # And another function here for the user menu
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print("Unknown command.please try again.")

        selection = input(MENU_PROMPT)

menu()