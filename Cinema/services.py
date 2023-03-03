from Cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession, User, Order, Ticket


def create_new_genre(name: str) -> str:
    already_exists = Genre.objects.filter(name=name).exists()

    if already_exists:
        return f"{name} already exists!"
    else:
        Genre.objects.create(name=name)
        return f"{name} was successfully added"


def get_genres(name: str = None) -> list:
    if name is None:
        genre_query = Genre.objects.all()
    else:
        genre_query = Genre.objects.filter(name=name)

    genre_query = list(genre_query)

    return genre_query


def delete_genre(name: str) -> str:
    try:
        Genre.objects.filter(name=name).delete()
    except Genre.DoesNotExist:
        return f"{name} does not exist!"

    return f"{name} was successfully deleted"


def create_new_actor(first_name: str, last_name: str):
    already_exists = Actor.objects.filter(first_name=first_name, last_name=last_name).exists()
    if already_exists:
        return f"{first_name} {last_name} already exists!"
    else:
        Actor.objects.create(first_name=first_name, last_name=last_name)
        return f"'{first_name} {last_name}' was successfully added"


def get_actor(first_name: str = None, last_name: str = None):
    if first_name is None or last_name is None:
        actor_query = Actor.objects.all()

    if first_name is not None:
        actor_query = Actor.objects.filter(first_name=first_name)

    if last_name is not None:
        actor_query = Actor.objects.filter(last_name=last_name)

    actor_query = list(actor_query)

    return actor_query


def update_actor(last_name: str, first_name: str, new_last_name: str):
    exists = Actor.objects.filter(first_name=first_name, last_name=last_name).exists()
    if exists:
        query = Actor.objects.filter(first_name=first_name, last_name=last_name)
        query.update(last_name=new_last_name)
        return f"'{first_name} {last_name}' updated to '{first_name} {new_last_name}'"
    else:
        return f"{first_name} {last_name} does not exist!"


def delete_actor(first_name: str, last_name: str):
    exists = Actor.objects.filter(first_name=first_name, last_name=last_name).exists()
    if exists:
        Actor.objects.filter(first_name=first_name, last_name=last_name).delete()
        return f"'{first_name} {last_name}' was successfully deleted"
    else:
        return f"{first_name} {last_name} does not exist!"


def create_new_cinema_hall(name: str, rows: int, seats_in_row: int):
    already_exists = CinemaHall.objects.filter(name=name).exists()

    if already_exists:
        return f"Cinema hall with this name already exists!"
    else:
        CinemaHall.objects.create(
            name=name,
            rows=rows,
            seats_in_row=seats_in_row
        )
        return f"Cinema hall: '{name}' was successfully added"


def get_cinema_hall(name: str = None):
    if name is None:
        query = CinemaHall.objects.all()

    if name is not None:
        query = CinemaHall.objects.filter(name=name)

    query = list(query)

    return query


def delete_cinema_hall(name: str):
    exists = CinemaHall.objects.filter(name=name)
    if exists:
        CinemaHall.objects.filter(name=name).delete()
        return f"Cinema hall: '{name}' was successfully deleted"
    else:
        return f"Cinema hall: '{name}' does not exist!"


def create_new_movie(title: str, description: str, genre: str, actors: list[str]):
    exists = Movie.objects.filter(title=title).exists()
    if exists:
        return f"'{title}' already exists!"
    else:
        movie = Movie.objects.create(
            title=title,
            description=description
        )
        exists_genre = Genre.objects.filter(name=genre).exists()
        if exists_genre:
            genres = Genre.objects.get(name=genre)
        else:
            genres = Genre.objects.create(name=input("Enter the name of the genre: "))

        movie.genres.add(genres)

        for actors_f_l_name in actors:
            first_name, last_name = actors_f_l_name.split(" ")
            exists_actor = Actor.objects.filter(first_name=first_name, last_name=last_name).exists()
            if exists_actor:
                first_name, last_name = actors_f_l_name.split(" ")
                actor = Actor.objects.get(first_name=first_name, last_name=last_name)
            else:
                actor = Actor.objects.create(
                    first_name=input("Enter actor's name: "),
                    last_name=input("Enter the actor's last name: ")
                )
            movie.actors.add(actor)

    return f"{movie} \n was successfully added"


def delete_movie(title: str):
    exists = Movie.objects.filter(title=title).exists()
    if exists:
        Movie.objects.filter(title=title).delete()
        return f"'{title}' was successfully deleted"
    else:
        return f"'{title}' does not exist!"


def create_new_movie_session(title: str, name: str, show_time: str):
    exists_cinema_hall = CinemaHall.objects.filter(name=name).exists()
    if exists_cinema_hall:
        new_movie_session = MovieSession.objects.create(
            movie=Movie.objects.get(title=title),
            cinema_hall=CinemaHall.objects.get(name=name),
            show_time=show_time
        )
    elif exists_movie is True and exists_cinema_hall is False:
        cinema_hall = CinemaHall.objects.create(
            name=input("Enter the name of the movie theater: "),
            rows=int(input("Enter the number of rows: ")),
            seats_in_row=int(input("Enter the number of seats in the row: "))
        )
        new_movie_session = MovieSession.objects.create(
            movie=Movie.objects.filter(title=title),
            cinema_hall=cinema_hall,
            show_time=show_time
        )

    return new_movie_session


def delete_movie_session(movie_session_id: int):
    exists = MovieSession.objects.filter(pk=movie_session_id).exists()
    if exists:
        MovieSession.objects.filter(pk=movie_session_id).delete()
        return f"Movie session with (id: {movie_session_id}) was successfully deleted"
    else:
        return f"Movie session with (id: {movie_session_id}) does not exist!"


def create_user(username: str, password: str):
    exists = User.objects.filter(username=username).exists()
    if exists:
        return f"User {username} already exists!"
    else:
        User.objects.create(username=username, password=password)
        return f"User {username} was successfully added"


def change_password(username: str, password: str, new_password: str):
    exists = User.objects.filter(username=username).exists()
    if exists:
        valid_password = User.objects.filter(username=username)
        valid_password.filter(password=password).exists()
        if valid_password:
            user_w_new_password = User.objects.filter(username=username, password=password)
            user_w_new_password.update(password=new_password)
            return f"Password for (username: {username}) was successfully changed"
        else:
            return f"Wrong password!"
    else:
        return f"User {username} does not exists!"


def delete_user(username: str, password: str):
    exists = User.objects.filter(username=username).exists()
    if exists:
        valid_password = User.objects.filter(username=username)
        valid_password.filter(password=password).exists()
        if valid_password:
            User.objects.filter(username=username, password=password).delete()
            return f"User {username} was successfully deleted"
        else:
            return f"Wrong password!"
    else:
        return f"User {username} does not exists!"


def get_users(username: str = None):
    if username is None:
        query = User.objects.all()

    if username is not None:
        query = User.objects.filter(username=username)

    query = list(query)

    return query


def create_order(username: str):
    exists_user = User.objects.filter(username=username).exists()
    if exists_user:
        user = User.objects.get(username=username)
        Order.objects.create(user=user)
        return f"Order was successfully created"
    else:
        return f"User {username} does not exists!"


def delete_order(order_id):
    exists = Order.objects.filter(user__order=order_id).exists()
    if exists:
        Order.objects.filter(user__order=order_id).delete()
        return f"Order with (id: {order_id}) was successfully deleted"
    else:
        return f"Order with (id: {order_id}) does not exists!"


def create_ticket(row: int, seat: int, movie_session: int, order: int):
    exists_movie_session = MovieSession.objects.filter(pk=movie_session)
    exists_order = Order.objects.filter(pk=order)
    if exists_movie_session and exists_order:
        Ticket.objects.create(
            row=row,
            seat=seat,
            movie_session=MovieSession.objects.get(pk=movie_session),
            order=Order.objects.get(pk=order)
        )
        return f"Ticket for the {seat} place of the {row} row"
