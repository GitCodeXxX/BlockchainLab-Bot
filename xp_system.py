user_xp = {}

def add_xp(user_id, amount):
    if user_id not in user_xp:
        user_xp[user_id] = 0
    user_xp[user_id] += amount
    return user_xp[user_id]

def get_xp(user_id):
    return user_xp.get(user_id, 0)
