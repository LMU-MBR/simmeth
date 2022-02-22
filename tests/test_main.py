import time

from simmeth.simulation import Simulation


def test_basic_simulation():
    start = time.time()
    env_scenarios = [
        {
            'turb': 0,
            'max_confidence': 1,
            'unlearn': True
        }
    ]
    sim = Simulation(scenarios=env_scenarios, n_strategies=3, t=500, n=1000)

    sim.run()

    end = time.time()

    print(end - start)


test_basic_simulation()
