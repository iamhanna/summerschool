import numpy as np
import random
import ipdb
import matplotlib.pyplot as plt

world = np.load("world.npy")
reward = np.load("reward.npy")
gamma = 0.8

value_function = np.zeros(world.shape)
# the reward from the point of view of the agent
known_reward = np.zeros(world.shape)
# ipdb.set_trace()

available_positions = np.where(world)


def pick_random_position(available_positions):
    """
    pick a random position in order to initialize the position of our agent
    """
    number_of_available_positions = available_positions[0].shape[0]
    random_index = random.randint(0, number_of_available_positions-1)
    i_coordinate = available_positions[0][random_index]
    j_coordinate = available_positions[1][random_index]
    return i_coordinate, j_coordinate


def plot_position(agent_position, world, step):
    """
    plot the agent in its environment
    """
    title = "position of agent at step {}".format(step)
    # we need to make a copy otherwise it will not work
    world_copy = np.copy(world)
    world_copy[agent_position[0], agent_position[1]] = 3
    plt.imshow(world_copy)
    plt.title(title)
    plt.savefig("images/value_iteration/agent_position_step_{}.pdf".format(step))
    plt.close()


def plot_value_function(value_function, step):
    """
    plot the value function while we compute it
    """
    title = "value function at step {}".format(step)
    plt.imshow(value_function)
    plt.colorbar()
    plt.title(title)
    plt.savefig("images/value_iteration/value_function_step_{}.pdf".format(step))
    plt.close()


def new_position_available(new_position, world):
    """
    check if the position new_position is compatible with
    the world we created
    """
    # in python, this can be interpreted as a boolean
    return world[new_position[0], new_position[1]]


def move_agent(agent_position, world):
    """
    determine a new position for the agent,
    in order to continue the exploration of the environment,
    possibly to find rewards at new positions.
    """
    # boolean representing if we moved the agent
    moved_agent = False
    # try to move the agent until it moves
    while not moved_agent:
        direction = random.randint(0, 3)
        if direction == 0:
            # try to go left
            # please edit here
            new_position = [1, 1]
        elif direction == 1:
            # try to go top
            # please edit here
            new_position = [1, 1]
        elif direction == 2:
            # try to go right
            # please edit here
            new_position = [1, 1]
        elif direction == 3:
            # try to go bottom
            # please edit here
            new_position = [1, 1]
        # check if position is available
        if new_position_available(new_position, world):
            # go out of the loop
            moved_agent = True
    return new_position


def get_reward(agent_position):
    """
    when the agent starts exploring the environment,
    it does not know where the rewards are !
    """
    return reward[agent_position[0], agent_position[1]]


def update_value_function(value_function, known_reward):
    """
    Update the value function according to the Bellman equation
    """
    for i in range(1, world.shape[0]-1):
        for j in range(1, world.shape[0]-1):
            # still check that the position is available
            # otherwise, the value should stay at 0
            # please edit here
            if 0:
                # please edit also here
                value_function[i, j] = known_reward[i, j] +\
                    max(gamma*0.1,
                        gamma*0.2,
                        gamma*0.1,
                        gamma*0.4)
    return value_function


agent_position = pick_random_position(available_positions)
for step in range(100):
    print("step {} : agent position {}".format(step, agent_position))
    plot_position(agent_position, world, step)

    # move the agent randomly
    agent_position = move_agent(agent_position, world)

    # cherck if there is a reward at that position
    obtained_reward = get_reward(agent_position)
    if obtained_reward > 0:
        print("found reward in position {}".format(agent_position))
        known_reward[agent_position[0], agent_position[1]] = obtained_reward

    # update with the Bellmann equation
    value_function = update_value_function(value_function, known_reward)
    plot_value_function(value_function, step)

    # sometimes reinitialize the position of the agent.
    if step % 15 == 0:
        print("re initialize agent position")
        agent_position = pick_random_position(available_positions)

# safe our evaluation for usage later
np.save("value_function.npy", value_function)
