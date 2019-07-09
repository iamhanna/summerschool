import numpy as np
import random
import ipdb
import matplotlib.pyplot as plt

world = np.load("world.npy")
reward = np.load("reward.npy")
value_function = np.load("value_function.npy")
available_positions = np.where(world)


def pick_random_position(available_positions):
    """
    we can pick a ranom initial position
    """
    number_of_available_positions = available_positions[0].shape[0]
    random_index = random.randint(0, number_of_available_positions-1)
    i_coordinate = available_positions[0][random_index]
    j_coordinate = available_positions[1][random_index]
    return i_coordinate, j_coordinate


def pick_action(agent_position, value_function):
    """
    with the knowledge of the value function,
    we are able to choose th best possible action
    """
    i = agent_position[0]
    j = agent_position[1]
    # please edit here
    possible_actions = {"left": value_function[1, 1],
                        "top": value_function[1, 1],
                        "right": value_function[1, 1],
                        "bottom": value_function[1, 1]}
    # ipdb.set_trace()
    current_value = value_function[i, j]
    if max(possible_actions.values()) > current_value:
        print("agent moves : current value {}".format(current_value))
        sorted_actions = \
            sorted(possible_actions,
                   key=lambda action: possible_actions[action], reverse=True)
        if sorted_actions[0] == "left":
            new_position = [agent_position[0], agent_position[1]-1]
        elif sorted_actions[0] == "top":
            new_position = [agent_position[0]-1, agent_position[1]]
        elif sorted_actions[0] == "right":
            new_position = [agent_position[0], agent_position[1]+1]
        elif sorted_actions[0] == "bottom":
            new_position = [agent_position[0]+1, agent_position[1]]
        # move the agent
        # edit here
        chosen_action = "right"
        print("action : "+chosen_action)
        print("new state value : {}".format(possible_actions[chosen_action]))
        return new_position
    else:
        return agent_position


def plot_position(step, travel,  agent_position, world):
    """
    utility function in order to plot the trajectory
    of our agent
    """
    title = "position of agent at step {}".format(step)
    # we need to make a copy otherwise it will not work
    world_copy = np.copy(world)
    world_copy[agent_position[0], agent_position[1]] = 3
    plt.imshow(world_copy)
    plt.title(title)
    plt.savefig(
        "images/value_iteration_policy/agent_position_travel_{}_step_{}".format(travel, step))
    plt.close()


# we will plot some trajectories of the agent.
for travel in range(1, 10):
    print("---\npick new random position for agent")
    agent_position = pick_random_position(available_positions)
    for step in range(15):
        plot_position(step, travel, agent_position, world)
        agent_position = pick_action(agent_position, value_function)
        print("step {} : agent position {}".format(step, agent_position))
