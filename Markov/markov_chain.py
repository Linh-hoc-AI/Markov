import numpy as np

class MarkovChain:
    def __init__(self, transition_matrix, states):
        self.transition_matrix = np.array(transition_matrix)
        self.states = states
        self.current_state = np.random.choice(states)

    def next_state(self):
        next_state = np.random.choice(self.states,\
                                      p=self.transition_matrix[self.states.index(self.current_state)])
        self.current_state = next_state
        return self.current_state

# ma trận xác suất chuyển trạng thái
transition_matrix = [
    [0.5, 0.4, 0.1],
    [0.3, 0.5, 0.2],
    [0.1, 0.4, 0.5]
]

# các trạng thái
states = ['nắng', 'bình thường', 'mưa']

# tạo mô hình Markov
weather_chain = MarkovChain(transition_matrix, states)

# in trạng thái hiện tại và trạng thái tiếp theo
print(weather_chain.current_state)
for i in range(20):
    print(weather_chain.next_state())