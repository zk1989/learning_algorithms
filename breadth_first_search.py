""" Python implementation of breadth-first search (graph) algorithm """


from collections import deque

# hash tables are data structures that express relationships
# graphs are expressed in the code in a form of hash tables
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "johnny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johnny"] = []

def person_is_mango_seller(name: str) -> bool:
    return name[-1] == "m"

def breadth_first_search(name: str) -> bool:
    """
    Finds person whose last letter in a name is 'm' (called 'mango-seller').

    @param name: string that is one of the names from above graph
    @return information whether there is a 'mango seller' in the given graph
    """
    queue = deque()
    queue += graph[name]
    searched = set()
    # while queue isn't empty
    while queue:
        # takes the first item from the beginning of the queue
        person = queue.popleft()
        if person not in searched:
            if person_is_mango_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                queue += graph[person]
                searched.add(person)
    print("No mango sellers in this graph :(")
    return False

breadth_first_search("you")
breadth_first_search("anuj")
