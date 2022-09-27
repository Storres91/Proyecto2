#NEAT
import neat

time_interval_seconds = 0
xor_inputs = [] 
xor_outputs = []

def distance():
    return 

def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = max
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        for xi, xo in zip(xor_inputs, xor_outputs):
            output = net.activate(xi)
            genome.fitness -= (output[0] - xo[0]) ** 2

def run (config_file):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
    
    p = neat.Population(config)
    
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(time_interval_seconds))

    winner = p.run(eval_genomes, 300)

    print('\nBest genome:\n{!S}'.format(winner))

    print ('\nOutput:')
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)

