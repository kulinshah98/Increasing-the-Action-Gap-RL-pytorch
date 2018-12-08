import gym
import torch.optim as optim

from dqn_model import DQN
from dqn_learn import OptimizerSpec, dqn_learing
from utils.gym_file import get_env, get_wrapper_by_name
from utils.schedule import LinearSchedule

BATCH_SIZE = 32
GAMMA = 0.99
REPLAY_BUFFER_SIZE = 300000
LEARNING_STARTS = 50000
LEARNING_FREQ = 4
FRAME_HISTORY_LEN = 4
TARGER_UPDATE_FREQ = 1000
LEARNING_RATE = 0.00025
ALPHA = 0.95
EPS = 0.01

def main(env, num_timesteps):

    def stopping_criterion(env):
        return get_wrapper_by_name(env, "Monitor").get_total_steps() >= num_timesteps

    optimizer_spec = OptimizerSpec(
        constructor=optim.RMSprop,
        kwargs=dict(lr=LEARNING_RATE, alpha=ALPHA, eps=EPS),
    )

    exploration_schedule = LinearSchedule(2000000, 0.05)

    dqn_learing(
        env=env,
        q_func=DQN,
        optimizer_spec=optimizer_spec,
        exploration=exploration_schedule,
        stopping_criterion=stopping_criterion,
        replay_buffer_size=REPLAY_BUFFER_SIZE,
        batch_size=BATCH_SIZE,
        gamma=GAMMA,
        learning_starts=LEARNING_STARTS,
        learning_freq=LEARNING_FREQ,
        frame_history_len=FRAME_HISTORY_LEN,
        target_update_freq=TARGER_UPDATE_FREQ,
    )

if __name__ == '__main__':


    #task = benchmark.tasks[3]
    #task = 'AsterixNoFrameskip-v4'
    task = 'SpaceInvadersNoFrameskip-v4'

    # Run training
    seed = 0 # Use a seed of zero (you may want to randomize the seed!)
    env = get_env(task, seed)




    main(env, 40000000)
