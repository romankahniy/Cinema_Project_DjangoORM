import init_django_orm

from datetime import datetime
from Cinema.services import (
    create_new_genre,
    get_genres,
    delete_genre,
    create_new_actor,
    get_actor,
    update_actor,
    delete_actor,
    create_new_cinema_hall,
    get_cinema_hall,
    delete_cinema_hall,
    create_new_movie,
    delete_movie,
    create_new_movie_session,
    delete_movie_session,
    create_user,
    change_password,
    delete_user,
    get_users,
    create_order,
    delete_order,
    create_ticket

)


def main():
    while True:
        print("Main menu:")
        print("1 - Genres / Actors / Movies")
        print("2 - Cinemas / Sessions")
        print("3 - Users / Tickets / Orders")
        print("0 - Exit")
        choice_1 = input("Enter the command: ")

        if choice_1 == "1":

            print("Menu Genres / Actors / Movies:")
            print("1 - Genres")
            print("2 - Actors")
            print("3 - Movies")
            print("0 - Exit")

            choice_2 = input("Enter the command: ")

            if choice_2 == "1":

                print("Genres menu:")
                print("1 - Create a new genre")
                print("2 - Get genre (by name / all)")
                print("3 - Remove genre")
                print("0 - Exit")
                choice_3 = input("Enter the command: ")

                if choice_3 == "1":
                    name = input("Enter the name of the genre: ")
                    print(create_new_genre(name=name))

                elif choice_3 == "2":
                    name = input("Enter the name of the genre: ")
                    print(get_genres(name=name))

                elif choice_3 == "3":
                    name = input("Enter the name of the genre: ")
                    print(delete_genre(name=name))

                elif choice_3 == "0":
                    break

            elif choice_2 == "2":

                print("Actors menu:")
                print("1 - Create a new actor")
                print("2 - Get actor (by first/last name / all)")
                print("3 - Update actor's last name")
                print("4 - Remove actor")
                print("0 - Exit")
                choice_4 = input("Enter the command: ")

                if choice_4 == "1":
                    first_name = input("Enter the name of the actor: ")
                    last_name = input("Enter the actor's last name: ")
                    print(create_new_actor(first_name=first_name, last_name=last_name))

                elif choice_4 == "2":
                    first_name = input("Enter the name of the actor: ")
                    last_name = input("Enter the actor's last name: ")
                    print(get_actor(first_name=first_name, last_name=last_name))

                elif choice_4 == "3":
                    first_name = input("Enter the name of the actor: ")
                    last_name = input("Enter the actor's last name: ")
                    new_last_name = input("Enter the actor's new last name: ")
                    print(update_actor(last_name=last_name, first_name=first_name, new_last_name=new_last_name))

                elif choice_4 == "4":
                    first_name = input("Enter the name of the actor: ")
                    last_name = input("Enter the actor's last name: ")
                    print(delete_actor(first_name=first_name, last_name=last_name))

                elif choice_4 == "0":
                    break

            elif choice_2 == "3":

                print("Movies menu:")
                print("1 - Create movie")
                print("2 - Delete movie")
                print("0 - Exit")
                choice_5 = input("Enter the command: ")

                if choice_5 == "1":
                    title = input("Enter the name of the movie: ")
                    description = input("Enter a description of the movie: ")
                    genre = input("Enter the movie genre: ")
                    actors = input("Enter actors via ', ': ").split(", ")
                    print(create_new_movie(title=title, description=description, genre=genre, actors=actors))

                elif choice_5 == "2":
                    movie_session_id = int(input("Enter the session ID: "))
                    print(delete_movie_session(movie_session_id=movie_session_id))

                elif choice_5 == "0":
                    break

            elif choice_2 == "0":
                break

        elif choice_1 == "2":

            print("Menu Cinemas / Sessions:")
            print("1 - Cinemas")
            print("2 - Sessions")
            print("0 - Exit")

            choice_5 = input("Enter the command: ")

            if choice_5 == "1":
                print("Menu Cinemas:")
                print("1 - Create cinema hall")
                print("2 - Get cinema hall by name / all")
                print("3 - Delete cinema hall")
                print("0 - Exit")

                choice_6 = input("Enter the command: ")

                if choice_6 == "1":
                    name = input("Enter the name of the hall: ")
                    rows = int(input("Enter the number of rows in the hall: "))
                    seats_in_row = int(input("Enter the number of seats in the row: "))
                    print(create_new_cinema_hall(name=name, rows=rows, seats_in_row=seats_in_row))

                elif choice_6 == "2":
                    name = input("Enter the name of the hall: ")
                    print(get_cinema_hall(name=name))

                elif choice_6 == "3":
                    name = input("Enter the name of the hall: ")
                    print(delete_cinema_hall(name=name))

                elif choice_6 == "0":
                    break

            elif choice_5 == "2":
                print("Menu Sessions:")
                print("1 - Create movie session")
                print("2 - Delete movie session")
                print("0 - Exit")

                choice_7 = input("Enter the command: ")
                if choice_7 == "1":
                    title = input("Enter the name of the movie: ")
                    name = input("Enter the name of the hall: ")
                    show_time = input("Enter the date in YYYY-MM-DD HH:MM format: ")
                    print(create_new_movie_session(title=title, name=name, show_time=show_time))

                elif choice_7 == "2":
                    movie_session_id = int(input("Enter the session ID to delete: "))
                    print(delete_movie_session(movie_session_id=movie_session_id))

                elif choice_7 == "0":
                    break

            elif choice_5 == "0":
                break

        elif choice_1 == "3":

            print("Menu Users / Tickets / Orders:")
            print("1 - Users")
            print("2 - Tickets")
            print("3 - Orders")
            print("0 - Exit")

            choice_8 = input("Enter the command: ")

            if choice_8 == "1":
                print("Menu Users:")
                print("1 - Create user")
                print("2 - Change password")
                print("3 - Delete user")
                print("0 - Exit")

                choice_9 = input("Enter the command: ")
                if choice_9 == "1":
                    username = input("Enter a username: ")
                    password = input("Enter a password: ")
                    print(create_user(username=username, password=password))

                elif choice_9 == "2":
                    username = input("Enter a username: ")
                    password = input("Enter a password: ")
                    new_password = input("Enter a new password: ")
                    print(change_password(username=username, password=password, new_password=new_password))

                elif choice_9 == "3":
                    username = input("Enter a username: ")
                    password = input("Enter a password: ")
                    print(delete_user(username=username, password=password))

                elif choice_9 == "0":
                    break

            elif choice_8 == "2":
                print("Menu Tickets:")
                print("1 - Create tickets")
                print("0 - Exit")

                choice_10 = input("Enter the command: ")
                if choice_10 == "1":
                    row = int(input("Select a row: "))
                    seat = int(input("Choose a place: "))
                    movie_session_id = int(input("Enter the session id: "))
                    order_id = int(input("Enter the order id: "))
                    print(create_ticket(row=row, seat=seat, movie_session=movie_session_id, order=order_id))

                elif choice_10 == "0":
                    break

            elif choice_8 == "3":
                print("Menu Orders:")
                print("1 - Create order")
                print("2 - Delete order")
                print("0 - Exit")

                choice_11 = input("Enter the command: ")
                if choice_11 == "1":
                    username = input("Enter a username: ")
                    print(create_order(username=username))

                elif choice_11 == "2":
                    order_id = int(input("Enter the order id: "))
                    print(delete_order(order_id=order_id))

                elif choice_11 == "0":
                    break

        elif choice_1 == "0":
            break


if __name__ == '__main__':
    main()
