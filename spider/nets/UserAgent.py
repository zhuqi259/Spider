# -*- coding: utf-8 -*-
__author__ = 'zhuqi259'

"""
User-Agent
"""
from utils.FileUtils import *
import random

__pkl__ = os.path.join(os.path.pardir, "data/user_agents.pkl")
__filenames__ = [os.path.join(os.path.pardir, "data/clientUA.txt"),
                 os.path.join(os.path.pardir, "data/mobileUA.txt")]


def get_user_agent_data(filenames):
    agents = []
    if filenames:
        for filename in filenames:
            contents = read_data(filename).decode("utf-8")
            for ua in contents.splitlines():
                if not ua.startswith("#"):
                    agents.append(ua)

    return agents


def save_user_agent_data(pkl, filenames):
    agents = get_user_agent_data(filenames)
    save_pickle(agents, pkl)


def get_user_agent(pkl=__pkl__, filenames=__filenames__):
    if not exists(pkl):
        save_user_agent_data(pkl, filenames)
    agents = load_pickle(pkl)
    return random.choice(agents)


if __name__ == "__main__":
    agent = get_user_agent()
    print(agent)
