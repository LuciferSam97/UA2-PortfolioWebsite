import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_context('notebook')
sns.set_theme(style="darkgrid")


class RandomWalk:
    def __init__(self,
                 p_value: float = 0.5,
                 n_events: int = 100,
                 n_simulations: int = 10,
                 initial_conditions: int | float | tuple[int | float, int | float] = 0,
                 boundary: tuple[int | float, int | float | bool] | None = None):
        """
        The initialiser for a random walk object. This computes the positions for each event in all simulated random walks,
        as well as the mean position across all simulations, and the mean square displacement over all simulations at a given event.

        :param p_value: the probability that the random walk steps down by one.
        :param n_events: the number of probabilistic events i.e. the number of steps performed by the walk.
        :param n_simulations: the number of simulations ran of the random walk.
        :param initial_conditions: the starting position, or bounded interval within which a random starting position
        is chosen, for a random walk.
        :param boundary: a 2-tuple: tuple[int | float, int | float | bool]. In the simplest case, we have a 2-tuple of
        integers or floats which are treated as lower and upper bounds. For a symmetric bound about 0, the first item is
        treated as the positive boundary value, and the second item is an indicator for whether this is to be mirrored
        across y = 0 (True) or whether this is an individual boundary (False).
        """

        self.p_value = p_value
        self.n_events = n_events
        self.n_simulations = n_simulations
        self.initial_conditions = initial_conditions
        self.boundary = boundary
        self.boundary = self._calibrate_boundaries()

        self.sim_positions = np.zeros((n_simulations, n_events))

        if type(initial_conditions) is float or type(initial_conditions) is int:
            self.sim_positions[:, 0] = [initial_conditions]*n_simulations
        elif type(initial_conditions) is tuple:
            self.sim_positions[:, 0] = np.random.randint(initial_conditions[0], initial_conditions[1], size=n_simulations)
        else:
            raise TypeError(f'initial_conditions must be an integer, a float, or a 2-tuple of integers or floats. Type given was {type(initial_conditions)}')

        self.time_steps = np.arange(0, n_events, 1)
        self.up_down = np.zeros((n_simulations, 2))

        if self.boundary is None:
            self.sim_positions = self._generate()
        else:
            self.sim_positions = self._generate_bounded()

        self.mean_positions = np.zeros(n_events)
        for i in range(n_events):
            self.mean_positions[i] = np.mean(self.sim_positions[:, i])

        self.msd = np.zeros(n_events)
        for i in range(n_events):
            self.msd[i] = np.mean(self.sim_positions[:, i] ** 2)


    def _generate(self) -> np.ndarray:
        for i in range(self.n_simulations):
            for j in range(1, self.n_events):
                flip = np.random.rand()
                if flip < self.p_value:
                    step = -1
                    self.up_down[i][0] += 1
                else:
                    step = 1
                    self.up_down[i][1] += 1
                self.sim_positions[i, j] = self.sim_positions[i, j - 1] + step
        return self.sim_positions


    def _generate_bounded(self) -> np.ndarray:
        for i in range(self.n_simulations):
            step_tracker = np.zeros(self.n_events)
            for j in range(1, self.n_events):
                flip = np.random.rand()
                if flip < self.p_value:
                    step = -1
                    self.up_down[i][0] += 1
                else:
                    step = 1
                    self.up_down[i][1] += 1
                step_tracker[j] = step
                self.sim_positions[i, j] = self.sim_positions[i, j - 1] + step

                if type(self.boundary) == tuple:
                    # for k in range(0, len(boundary)):
                    #     if self.sim_positions[i, j - 1] == boundary[k]:
                    #         if step_tracker[j - 1] == -1:
                    #             self.sim_positions[i, j] = self.sim_positions[i, j - 1] + 1
                    #         elif step_tracker[j-1] == 1:
                    #             self.sim_positions[i, j] = self.sim_positions[i, j - 1] - 1

                    if self.sim_positions[i, j - 1] == self.boundary[0]:
                        if step_tracker[j-1] == -1:
                            self.sim_positions[i, j] = self.sim_positions[i, j - 1] + 1
                        elif step_tracker[j-1] == 1:
                            self.sim_positions[i, j] = self.sim_positions[i, j - 1] - 1
                    elif self.sim_positions[i, j - 1] == self.boundary[1]:
                        if step_tracker[j - 1] == -1:
                            self.sim_positions[i, j] = self.sim_positions[i, j - 1] + 1
                        elif step_tracker[j - 1] == 1:
                            self.sim_positions[i, j] = self.sim_positions[i, j - 1] - 1
                    else:
                        self.sim_positions[i, j] = self.sim_positions[i, j - 1] + step
                elif type(self.boundary) == float or type(self.boundary) == int:
                    if self.sim_positions[i, j-1] == self.boundary:
                        if step_tracker[j-1] == -1:
                            self.sim_positions[i, j] = self.sim_positions[i, j - 1] + 1
                        elif step_tracker[j-1] == 1:
                            self.sim_positions[i, j] = self.sim_positions[i, j - 1] - 1
                    else:
                        self.sim_positions[i, j] = self.sim_positions[i, j - 1] + step

        return self.sim_positions


    def _calibrate_boundaries(self) -> tuple[int | float, int | float] | int | float | None:
        if self.boundary is not None:
            if type(self.boundary[1]) == bool:
                if self.boundary[1]:
                    if self.boundary[0] > 0:
                        return -self.boundary[0], self.boundary[0]
                    elif self.boundary[0] < 0:
                        return self.boundary[0], -self.boundary[0]
                    else:
                        return None
                else:
                    return self.boundary[0]

            elif type(self.boundary[1]) == int or type(self.boundary[1]) == float:
                if self.boundary[1] > self.boundary[0]:
                    return self.boundary[0], self.boundary[1]
                elif self.boundary[1] < self.boundary[0]:
                    return self.boundary[1], self.boundary[0]
                else:
                    return self.boundary[0]

            else:
                if type(self.boundary) != tuple:
                    bad_type = type(self.boundary)
                else:
                    bad_type = (type(self.boundary[0]), type(self.boundary[1]))
                raise TypeError(f"boundary parameter expects type tuple[int | float, int | float | bool]. Got type {bad_type}.")
        else:
            return None


    def __str__(self):
        return (f"A random walk with probability {self.p_value} of stepping down, run over "
                f"{self.n_events} events for {self.n_simulations} simulations.")


    def plot_process(self,
                     plot_range : str | tuple[int, int, int] = "all",
                     plot_mean_pos : bool = False,
                     return_obj : bool = False) -> None | tuple[plt.Figure, plt.Axes]:

        if type(plot_range) == str:
            if plot_range == "all":
                r_start = 0
                r_stop = self.n_simulations
                r_step = 1
            else:
                raise ValueError("plot_range must be either 'all' or a tuple of inputs for the range() function.")
        else:
            r_start = plot_range[0]
            r_stop = plot_range[1]
            r_step = plot_range[2]

        fig, ax = plt.subplots()

        if type(self.boundary) == tuple:
            ax.axhline(self.boundary[0], lw=2, linestyle="--", color="black")
            ax.axhline(self.boundary[1], lw=2, linestyle="--", color="black")
        elif type(self.boundary) == float or type(self.boundary) == int:
            ax.axhline(self.boundary, lw=2, linestyle="--", color="black")

        for i in range(r_start, r_stop, r_step):
            ax.plot(self.time_steps, self.sim_positions[i, :])

        if plot_mean_pos:
            ax.plot(self.time_steps, self.mean_positions, 'r-')

        plt.xlabel("Time")
        plt.ylabel("Position")

        if return_obj:
            return fig, ax
        else:
            plt.show()
            return None


    def plot_msd(self, return_obj : bool = False) -> None | tuple[plt.Figure, plt.Axes]:
        fig, ax = plt.subplots()
        ax.plot(self.time_steps, self.msd)
        plt.xlabel("Time")
        plt.ylabel("Mean Square Displacement")
        plt.ylim([0, self.n_simulations + int(self.n_simulations / 10)])
        if return_obj:
            return fig, ax
        else:
            plt.show()
            return None


    def slice_distribution(self, t_slice : int, return_obj : bool = False) -> None | tuple[plt.Figure, plt.Axes]:
        fig, ax = plt.subplots()
        ax.hist(self.sim_positions[:, t_slice - 1], bins=20, density=True)
        plt.xlabel("Position")
        plt.ylabel("Probability")
        plt.xlim([-100, 100])
        if return_obj:
            return fig, ax
        else:
            plt.show()
            return None


    def test_simulation(self, simulation_number : int) -> str:
        p_sim = self.up_down[simulation_number][0] / self.n_events
        return f"Expected p = {self.p_value}, Simulated p = {p_sim}"


def main():
    walk = RandomWalk(p_value=0.5,
                      n_events=1000,
                      n_simulations=10,
                      initial_conditions=(-10,10),
                      boundary=(-2, 8))
    walk.plot_process()
    print(walk.test_simulation(5))
    print(walk)


if __name__ == "__main__":
    main()