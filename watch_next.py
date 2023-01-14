import spacy # importing spacy
nlp =spacy.load ('en_core_web_md') # specifying the model to use

watched_movie = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, 
the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.""" # watched movie description

# function that takes the description of watched as an argument and  will check similarity of the watcehd movie compared to the descrption of the avaliable movies, to suggest what to watch next.
def watch_next (watched_movie): 
    available_movies = ["Movie A :When Hiccup discovers Toothless isn't the only Night Fury, he must seek \"The Hidden World\", a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.",
    "Movie B :After the death of Superman, several new people present themselves as possible successors.",
    """Movie C :A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, 
    and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up.""",
    "Movie D :A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes and Doctor Watson.",
    "Movie E :A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed.",
    """Movie F :In the last moments of World War II, a young German soldier fighting for survival finds a Nazi captain's uniform.
    Impersonating an officer, the man quickly takes on the monstrous identity of the perpetrators he is trying to escape from.""",
    "Movie G :The world at an end, a dying mother sends her young son on a quest to find the place that grants wishes.",
    "Movie H :A musician helps a young singer and actress find fame, even as age and alcoholism send his own career into a downward spiral.",
    "Movie I :Corporate analyst and single mom, Jen, tackles Christmas with a business-like approach until her uncle arrives with a handsome stranger in tow.",
    """Movie J :Adapted from the bestselling novel by Madeleine St John, 
    Ladies in Black is an alluring and tender-hearted comedy drama about the lives of a group of department store employees in 1959 Sydney."""] # description of avaliable movies
    similar_movie = 0 # to compare the similarty set to 0 "least similar"
    similar_movie_title = "" # to store the title of the similar movie
    token1 = nlp (watched_movie) # tokenizing 
    for token2 in available_movies: 
        token2 = nlp (token2) # tokenizing 
        if similar_movie < (token1.similarity(token2)): # to check if its more than 0 in the first iteration and then the previous value of the last iteration
            similar_movie = (token1.similarity(token2)) # then it assigns the value if it s greater than the previous iteration
            similar_movie_title = token2 [:2] # assigning the title with the most similarity
    return similar_movie_title
            
print (watch_next(watched_movie))