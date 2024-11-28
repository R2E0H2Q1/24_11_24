# Work with set
# Here are the following lists:

oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", \
                 "Natalie Portman",
                 "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", \
                   "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}

# a. Add actress Emma Watson to the list of Oscar winners
print(f'The original set of Oscar Winners is: {oscar_winners}')
oscar_winners.add('Emma Watson')
print(f'a. After adding Emma Watson: {oscar_winners}')

# b. Make a copy of the list of Oscar winners. In the copy list:

oscar_winners_copy = oscar_winners.copy()
print(f'b. This is a copy of the O.W set: {oscar_winners_copy}')

#  b.1. Remove actress Meryl Streep

oscar_winners_copy.remove('Meryl Streep')
print(f'b.1. After removing Meryl Streep: {oscar_winners_copy}')

#  b.2. Clear all members in the list

oscar_winners_copy.clear()
print(f'b.2. After clearing the copy set: ')

# c. Which actors appeared in both Titanic and The Dark Knight?

actors_T_DK = titanic_actors.intersection(dark_knight_actors)
print(f'c. The actors that were present in both Titanic and DK are: {actors_T_DK}')

# d. Are there any actors who appear in iron man and avengers?

actors_m_r = iron_man_actors.intersection(avengers_actors)
print(f'c. The actors that were present in both Iron man and Avengers are: {actors_m_r}')

# e. Have all the actors in the "actor_list" list won an Oscar?

winners_check = actor_list.issubset(oscar_winners)
print(f'e. {winners_check}, not all the actors present on the set actor_list are present on the set Oscar Winners')

# f. Does "actor_list" include all the actors who appeared in the Avengers?

all_Avengers_inalist = avengers_actors.issuperset(actor_list)
print(f'f. {all_Avengers_inalist}, actor list doesnt include all actors that appear on Avengers!')

# g. Randomly remove one actor from the actor set "movie_cast"
#.pop: removes and returns a random element, Since sets are unordered, the element removed is random

random_pop = movie_cast.pop()
print(f'g. Element {random_pop} was remove from the set {movie_cast}')

# h. Remove actor Matt Damon from movie_cast list

damon_gone = movie_cast.remove("Matt Damon")
print(f'h. Set movie_cast after Matt Damon was removed: {movie_cast}')

# i. Which actors who played in Titanic did not win an Oscar?

dif_titanic_oscar = titanic_actors.difference(oscar_winners)
print(f'i. From the Titanic cast the following arent Oscar winners: {dif_titanic_oscar}')

# j. Which actors only appeared in one of the movies, Titanic or The Dark Knight?

unique = titanic_actors.symmetric_difference(dark_knight_actors)
print(f'j. Actors that only appeared on either Titanic or DK: {unique}')

# k. Update the list of Oscar winners and add Cate Blanchett  and Daniel Day-Lewis.

oscar_winners.update(["Cate Blanchett", "Daniel Day-Lewis"])
print(f'k. Updated Oscar winners set: {oscar_winners}')

# l. Combine the Titanic and the Dark Knight cast list to see their names. all the players

combined_set = titanic_actors | dark_knight_actors
print(combined_set)