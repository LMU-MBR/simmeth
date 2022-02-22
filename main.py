from simmeth.simulation.simulation import Simulation

if __name__ == "__main__":
    env_scenarios = [
        {
            'turb': 0,
            'max_confidence': 1,
            'unlearn': True
        },
    ]
    sim = Simulation(scenarios=env_scenarios, n_strategies=3, t=100, n=100)
    sim.run()
    sim.plot_scenarios()
    sim.get_env_strategy_dfs()
    print(sim)
