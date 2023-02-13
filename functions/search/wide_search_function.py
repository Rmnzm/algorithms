from collections import deque

graph = {
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}


def person_is_seller(name):
    return name[-1] == 'm'


def wide_search_function(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                result = person + " is a mango seller"
                return True, result
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


wide_search_function("you")
