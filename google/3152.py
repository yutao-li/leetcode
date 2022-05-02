from collections import defaultdict


class Question:
    def __init__(self, id, title, tags):
        self.id = id
        self.title = title
        self.tags = tags


class Volunteer:
    def __init__(self, id, tags):
        self.id = id
        self.tags = tags


class Assignment:
    def __init__(self, question, volunteer):
        self.question = question
        self.volunteer = volunteer


def questionVolunteerMatch(questions, volunteers):
    def removeNode(n):
        for n1 in adjList[n]:
            adjList[n1].remove(n)
            if not adjList[n1]:
                del adjList[n1]
        del adjList[n]

    questions = [[q.id, set(q.tags)] for q in questions]
    volunteers = [[v.id, set(v.tags)] for v in volunteers]
    lenQ = len(questions)
    adjList = defaultdict(list)
    for i, (q, qTags) in enumerate(questions):
        for j, (v, vTags) in enumerate(volunteers, start=lenQ):
            if qTags & vTags:
                adjList[i].append(j)
                adjList[j].append(i)
    matched = []
    while adjList:
        pick = None
        for k, v in adjList.items():
            if len(v) == 1:
                pick = k
                break
        if not pick:
            pick = next(iter(adjList))
        neigh = adjList[pick][0]
        removeNode(pick)
        removeNode(neigh)
        if pick > neigh:
            pick, neigh = neigh, pick
        matched.append([questions[pick][0], volunteers[neigh - lenQ][0]])
    return [Assignment(question, volunteer) for question, volunteer in matched]


sample = {
    "questions": [
        {
            "id": "0",
            "title": "how do i install vs code",
            "tags": ["mac", "vs code"]
        },
        {
            "id": "1",
            "title": "my program is too slow please help",
            "tags": ["python", "ai"]
        },
        {
            "id": "2",
            "title": "why is the hitbox off by 2 pixels",
            "tags": ["c#", "game"]
        },
        {
            "id": "3",
            "title": "my dependency injection stack trace is strange",
            "tags": ["java", "oop"]
        },
        {
            "id": "4",
            "title": "socket.recv is freezing",
            "tags": ["python", "networking"]
        },
        {
            "id": "5",
            "title": "i have a memory leak",
            "tags": ["c++", "networking"]
        }
    ],
    "volunteers": [
        {
            "id": "sam5k",
            "tags": ["python", "networking"]
        },
        {
            "id": "djpat",
            "tags": ["ai"]
        },
        {
            "id": "jessg",
            "tags": ["java", "networking"]
        },
        {
            "id": "rayo",
            "tags": ["java", "networking"]
        }
    ]
}
questions = [Question(q['id'], q['title'], q['tags']) for q in sample['questions']]
volunteers = [Volunteer(v['id'], v['tags']) for v in sample['volunteers']]
print(questionVolunteerMatch(questions, volunteers))
