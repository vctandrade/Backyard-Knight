import pickle
import data

def save(target, fileName, key=data.defaultKey):

    serialTarget = pickle.dumps(target)
    enTarget = data.encrypt(serialTarget, key)

    f = open("../../saves/" + fileName, 'w')
    f.write(enTarget)

def load(fileName, key=data.defaultKey):

    with open("../../saves/" + fileName, 'r') as f:
        enTarget = f.read()

    serialTarget = data.decrypt(enTarget, key)

    return pickle.loads(serialTarget)
