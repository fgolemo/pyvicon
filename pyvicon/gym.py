import gym

from pyvicon.tracker import Tracker


class DistanceRewardWrapper(gym.core.Wrapper):
    def __init__(self, env, ipport, objs, threshold):
        super().__init__(env)
        self.objs = objs
        self.thresh = threshold
        self.tracker = Tracker(ipport, objs)

    def step(self, action):
        obs, _, _, info = self.env.step(action)
        dist = self.tracker.get_dist(self.objs)

        done = False
        if dist <= self.thresh:
            done = True

        reward = dist * -1

        print('{:.5f}'.format(reward))

        return obs, reward, done, info
