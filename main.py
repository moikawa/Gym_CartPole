import gym

env = gym.make('CartPole-v1', render_mode='human')

for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, truncated, info = env.step(action)
        print(f'i_episode={i_episode}, observation={observation}, done={done}, trunc={truncated}, info={info}')
        if done:
            print(F'Episode finished after {t+1} timesteps".')
            break